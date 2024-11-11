# app/routers/calls.py

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict

router = APIRouter()

# Store active WebSocket connections
active_connections: Dict[str, WebSocket] = {}

@router.websocket("/ws/signaling/{session_id}")
async def signaling_endpoint(websocket: WebSocket, session_id: str):
    await websocket.accept()
    active_connections[session_id] = websocket
    try:
        while True:
            data = await websocket.receive_json()
            # Introducing a bug: incorrect loop variable name
            for sid, connection in active_connections.items():
                if sid == session_id:  # Bug: should be sid != session_id
                    await connectio.send_json(data)
    except WebSocketDisconnect:
        # Remove the connection when the client disconnects
        del active_connections[session_id]