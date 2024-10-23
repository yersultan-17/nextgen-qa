import requests
import sys
import json
from playwright.sync_api import sync_playwright, Playwright
import dotenv
import os

dotenv.load_dotenv()


def create_session(project_id, api_key):
    url = "https://www.browserbase.com/v1/sessions"
    payload = {"projectId": project_id}
    headers = {
        "X-BB-API-Key": api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["id"]
    except requests.exceptions.RequestException as e:
        print(f"Error creating session: {e}", file=sys.stderr)
        return None

def get_debug_url(session_id, api_key):
    url = f"https://www.browserbase.com/v1/sessions/{session_id}/debug"
    headers = {"X-BB-API-Key": api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting debug URL: {e}", file=sys.stderr)
        return None
    
def connect_to_browserbase(playwright: Playwright, api_key, session_id):
    chromium = playwright.chromium
    browser = chromium.connect_over_cdp(f'wss://connect.browserbase.com?apiKey={api_key}&sessionId={session_id}')
    return browser

def main():
    print("Starting browserbase.py script", file=sys.stderr)

    project_id = os.environ["BROWSERBASE_PROJECT_ID"]
    api_key = os.environ["BROWSERBASE_API_KEY"]

    session_id = create_session(project_id, api_key)
    if session_id:
        print(f"Session ID: {session_id}")

        print("Connecting to Browserbase", file=sys.stderr)
        with sync_playwright() as playwright:
            print("Connected to Browserbase", file=sys.stderr)
            browser = connect_to_browserbase(playwright, api_key, session_id)
            context = browser.contexts[0]
            page = context.pages[0]
            
            print("Going to google", file=sys.stderr)
            page.goto('https://www.google.com')
            
            print("Getting debug URL", file=sys.stderr)
            debug_info = get_debug_url(session_id, api_key)
            if debug_info:
                print(json.dumps(debug_info, indent=2))
                with open('/tmp/debugger_url.txt', 'w') as f:
                    f.write(debug_info['debuggerFullscreenUrl'])
                print("Debug URL saved to /tmp/debugger_url.txt", file=sys.stderr)
            else:
                print("Failed to get debug URL", file=sys.stderr)
            
            print("Browser session is still active. Press Ctrl+C to exit.", file=sys.stderr)
            try:
                # Keep the script running
                while True:
                    page.wait_for_timeout(1000)  # Wait for 1 second
            except KeyboardInterrupt:
                print("Closing browser and exiting", file=sys.stderr)
            finally:
                browser.close()

        print("Finished browserbase.py script", file=sys.stderr)
    else:
        print("Failed to create session", file=sys.stderr)

if __name__ == "__main__":
    main()

