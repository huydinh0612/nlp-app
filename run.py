
from src.api.api import app 

# import uvicorn 
# uvicorn.run(app, host="0.0.0.0", port=8000)

import threading
import uvicorn
import subprocess
import signal
import sys

# Define a function to handle graceful shutdown
def signal_handler(sig, frame):
    print('Shutting down...')
    sys.exit(0)

# Register the signal handler for SIGINT (Ctrl + C)
signal.signal(signal.SIGINT, signal_handler)


def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000)

def run_streamlit():
    subprocess.run(["streamlit", "run", "./src/gui/gui.py", "--server.port", "8080"])

if __name__ == "__main__":
    # Create threads for FastAPI and Streamlit
    fastapi_thread = threading.Thread(target=run_fastapi)
    streamlit_thread = threading.Thread(target=run_streamlit)

    # Start the threads
    fastapi_thread.start()
    streamlit_thread.start()

    # Wait for the threads to complete
    fastapi_thread.join()
    streamlit_thread.join()

    try:
        fastapi_thread.join()
        streamlit_thread.join()
    except KeyboardInterrupt:
        print('Shutting down...')
        sys.exit(0)