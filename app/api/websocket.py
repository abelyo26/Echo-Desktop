from fastapi import WebSocket, WebSocketDisconnect
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)

# Store active connections
active_connections: List[WebSocket] = []

async def connect(websocket: WebSocket) -> None:
    """
    Handle new WebSocket connections.
    """
    await websocket.accept()
    active_connections.append(websocket)
    
    # Send initial connection success message
    await websocket.send_json({
        "type": "connection_established",
        "message": "Connected to Echo Desktop"
    })

async def disconnect(websocket: WebSocket) -> None:
    """
    Handle WebSocket disconnections.
    """
    if websocket in active_connections:
        active_connections.remove(websocket)

async def broadcast(message: Dict[str, Any]) -> None:
    """
    Broadcast a message to all connected clients.
    """
    for connection in active_connections:
        try:
            await connection.send_json(message)
        except WebSocketDisconnect:
            # Connection might have been closed
            await disconnect(connection)

async def handle_message(websocket: WebSocket, data: Dict[str, Any]) -> None:
    """
    Process incoming WebSocket messages (simple echo in this placeholder).
    """
    # Simply echo the message back
    await websocket.send_json({
        "type": "echo",
        "data": data
    })