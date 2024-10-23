#!/bin/bash
set -e

./start_all.sh
./novnc_startup.sh

python http_server.py > /tmp/server_logs.txt 2>&1 &

# Run browserbase.py and redirect its output to both a file and stderr
python /home/computeruse/computer_use_demo/tools/browserbase.py 2>&1 | tee /tmp/browserbase_logs.txt >&2 &

# Run the new script to open the debugger URL
./open_debugger.sh &

STREAMLIT_SERVER_PORT=8501 python -m streamlit run computer_use_demo/streamlit.py > /tmp/streamlit_stdout.log &

echo "✨ Computer Use Demo is ready!"
echo "➡️  Open http://localhost:8080 in your browser to begin"

# Keep the container running
tail -f /dev/null