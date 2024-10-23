#!/bin/bash

# Wait for the URL file to be created
while [ ! -f /tmp/debugger_url.txt ]; do
    sleep 1
done

# Read the URL from the file
URL=$(cat /tmp/debugger_url.txt)

# Open the URL in Firefox
# DISPLAY=:1 firefox-esr "$URL"

# Open the URL using w3m in the background
# DISPLAY=:1 xterm -e "w3m '$URL'" &

# Open the URL using curl and display it in less
# DISPLAY=:1 xterm -e "curl -s '$URL' | less" &

# Print the URL to the console
echo "Debugger URL: $URL"

# Open Firefox in kiosk mode
DISPLAY=:1 firefox-esr --kiosk "$URL" &
# DISPLAY=:1 firefox-esr --fullscreen "$URL" &