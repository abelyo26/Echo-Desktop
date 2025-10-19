from fastapi import APIRouter, HTTPException
from typing import Dict, Any

router = APIRouter(tags=["api"])

@router.get("/status")
async def get_status() -> Dict[str, Any]:
    """
    Return the current status of the Echo Desktop service.
    """
    return {
        "status": "running",
        "version": "0.1.0",
    }

@router.get("/devices")
async def get_connected_devices() -> Dict[str, Any]:
    """
    Return a list of connected devices (placeholder).
    """
    return {
        "devices": []
    }