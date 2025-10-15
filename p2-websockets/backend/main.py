import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

# Create the FastAPI application
app = FastAPI()

# Define the sequence of statuses and their progress
STATUS_STAGES = [
    {"text": 'Uploading...', "progress": 25},
    {"text": 'Analyzing Audio & Video...', "progress": 50},
    {"text": 'Generating Highlight Clips...', "progress": 75},
    {"text": 'Complete!', "progress": 100},
]

# This is the WebSocket endpoint the frontend will connect to
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("Frontend connected.")
    await websocket.accept()
    try:
        # Loop through the statuses and send them to the frontend
        for stage in STATUS_STAGES:
            await websocket.send_json(stage) # Send the current stage as JSON
            await asyncio.sleep(2) # Wait for 2 seconds before sending the next one
        print("Finished sending statuses.")
    except Exception as e:
        print(f"Connection closed with error: {e}")
    finally:
        print("Frontend disconnected.")
