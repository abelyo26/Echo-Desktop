import os
import logging
from pathlib import Path
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class FileManager:
    """
    Simple file manager for handling basic file operations.
    """
    
    def __init__(self, base_directory: str = None):
        """
        Initialize file manager.
        
        Args:
            base_directory: Base directory for file operations, defaults to user home directory
        """
        self.base_directory = base_directory or str(Path.home())
    
    def list_directory(self, directory: str = "") -> List[Dict[str, Any]]:
        """
        List files and directories in the specified directory.
        
        Args:
            directory: Directory to list, relative to base_directory
            
        Returns:
            List of file/directory information
        """
        target_dir = os.path.join(self.base_directory, directory)
        
        try:
            entries = []
            for entry in os.scandir(target_dir):
                entry_info = {
                    "name": entry.name,
                    "path": os.path.relpath(entry.path, self.base_directory),
                    "is_dir": entry.is_dir(),
                    "size": entry.stat().st_size if not entry.is_dir() else 0,
                    "modified": entry.stat().st_mtime
                }
                entries.append(entry_info)
            return entries
        except Exception as e:
            logger.error(f"Error listing directory {target_dir}: {e}")
            return []