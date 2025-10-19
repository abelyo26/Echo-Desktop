#!/usr/bin/env python3
"""
Echo Desktop - Local bridge between your PC and mobile devices.
"""

import os
import sys
import asyncio
import logging
import argparse
import uvicorn
from fastapi import FastAPI, WebSocket

# Add the current directory to the path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.tui.app import EchoDesktopApp
from app.core.database import get_database

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("echo-desktop")

# Create FastAPI app
api = FastAPI(title="Echo Desktop API")

@api.get("/status")
async def status():
    """Simple status endpoint."""
    return {"status": "running", "version": "0.1.0"}

@api.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Simple WebSocket endpoint."""
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            await websocket.send_json({"received": data})
    except Exception as e:
        logger.error(f"WebSocket error: {e}")

class EchoDesktop:
    """Main application class for Echo Desktop."""
    
    def __init__(self, headless: bool = False):
        """
        Initialize the Echo Desktop application.
        
        Args:
            headless: Run in headless mode (API only, no TUI)
        """
        self.headless = headless
        
        # Initialize database
        self.db = get_database()
        
        # Initialize TUI if not in headless mode
        self.tui_app = None if headless else EchoDesktopApp()
    
    async def run(self):
        """Run the application."""
        if self.headless:
            # In headless mode, just run the API
            logger.info("Running in headless mode")
            config = uvicorn.Config(api, host="0.0.0.0", port=5678, log_level="info")
            server = uvicorn.Server(config)
            await server.serve()
        else:
            # In TUI mode, run the API in a separate task and then run the Textual app
            logger.info("Starting TUI mode")
            config = uvicorn.Config(api, host="0.0.0.0", port=5678, log_level="error")
            server = uvicorn.Server(config)
            api_task = asyncio.create_task(server.serve())
            await self.tui_app.run_async()

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Echo Desktop - Local bridge between your PC and mobile devices.")
    parser.add_argument("--headless", action="store_true", help="Run in headless mode (API only, no TUI)")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    
    return parser.parse_args()

def main():
    """Main entry point."""
    args = parse_args()
    
    # Set up logging level
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Create app instance
    app = EchoDesktop(headless=args.headless)
    
    # Run the app
    try:
        asyncio.run(app.run())
    except KeyboardInterrupt:
        logger.info("Application terminated by user")
    except Exception as e:
        logger.error(f"Application error: {e}", exc_info=True)

if __name__ == "__main__":
    main()