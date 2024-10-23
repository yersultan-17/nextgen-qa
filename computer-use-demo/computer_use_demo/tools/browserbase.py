import requests
import sys
import json


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

def main():
    print("Starting browserbase.py script", file=sys.stderr)

    project_id = "your-project-id"
    api_key = "your-api-key"

    session_id = create_session(project_id, api_key)
    if session_id:
        print(f"Session ID: {session_id}")

        debug_info = get_debug_url(session_id, api_key)
        if debug_info:
            print(json.dumps(debug_info, indent=2))
            # Save the debuggerFullscreenUrl to a file
            with open('/tmp/debugger_url.txt', 'w') as f:
                f.write(debug_info['debuggerFullscreenUrl'])
        else:
            print("Failed to get debug URL", file=sys.stderr)
    else:
        print("Failed to create session", file=sys.stderr)

    print("Finished browserbase.py script", file=sys.stderr)

if __name__ == "__main__":
    main()
