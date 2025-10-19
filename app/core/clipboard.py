import pyperclip
import logging

logger = logging.getLogger(__name__)

class ClipboardManager:
    """
    Simple clipboard manager.
    """
    
    def __init__(self):
        """Initialize clipboard manager."""
        self._last_content = ""
    
    def get_content(self) -> str:
        """Get current clipboard content."""
        try:
            return pyperclip.paste()
        except Exception as e:
            logger.error(f"Error reading clipboard: {e}")
            return ""
    
    def set_content(self, content: str) -> bool:
        """Set clipboard content."""
        try:
            pyperclip.copy(content)
            self._last_content = content
            return True
        except Exception as e:
            logger.error(f"Error setting clipboard: {e}")
            return False