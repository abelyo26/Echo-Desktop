import os
import json
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

# Default settings
DEFAULT_SETTINGS = {
    "app": {
        "name": "Echo Desktop",
        "version": "0.1.0",
    },
    "network": {
        "port": 5678,
        "auto_connect": True,
    },
    "files": {
        "download_directory": os.path.join(os.path.expanduser("~"), "Downloads", "Echo"),
    },
    "notifications": {
        "enabled": True,
        "max_history": 100,
    },
    "clipboard": {
        "enabled": True,
    },
}


class Settings:
    """Simple settings manager."""
    
    def __init__(self, config_file: str = None):
        """
        Initialize settings manager.
        
        Args:
            config_file: Path to config file, default is ~/.config/echo-desktop/config.json
        """
        self.config_file = config_file or os.path.join(
            os.path.expanduser("~"), 
            ".config", 
            "echo-desktop", 
            "config.json"
        )
        
        # Create config directory if it doesn't exist
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        
        # Load settings
        self.settings = self._load_settings()
    
    def _load_settings(self) -> Dict[str, Any]:
        """Load settings from file or create default."""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, "r") as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Error loading settings: {e}")
        
        return DEFAULT_SETTINGS.copy()
    
    def save(self) -> bool:
        """Save settings to file."""
        try:
            with open(self.config_file, "w") as f:
                json.dump(self.settings, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Error saving settings: {e}")
            return False
    
    def get(self, category: str, key: str, default: Any = None) -> Any:
        """Get a specific setting."""
        if category in self.settings and key in self.settings[category]:
            return self.settings[category][key]
        return default
    
    def set(self, category: str, key: str, value: Any) -> None:
        """Set a specific setting."""
        if category not in self.settings:
            self.settings[category] = {}
        
        self.settings[category][key] = value