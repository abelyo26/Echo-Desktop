import os
import logging
from typing import Dict, List, Any, Optional
from tinydb import TinyDB, Query

logger = logging.getLogger(__name__)

class DatabaseManager:
    """
    Simple database manager for Echo Desktop using TinyDB.
    """
    
    def __init__(self, db_path: str = None):
        """
        Initialize database manager.
        
        Args:
            db_path: Path to database file, defaults to ~/.local/share/echo-desktop/db.json
        """
        if db_path is None:
            data_dir = os.path.join(os.path.expanduser("~"), ".local", "share", "echo-desktop")
            os.makedirs(data_dir, exist_ok=True)
            db_path = os.path.join(data_dir, "db.json")
        
        self.db_path = db_path
        self.db = TinyDB(db_path)
        
        # Create standard tables
        self.devices = self.db.table("devices")
        self.notifications = self.db.table("notifications")
        self.files = self.db.table("files")
        
        logger.info(f"Database initialized at {db_path}")
    
    def close(self):
        """Close database connection."""
        self.db.close()
    
    def get_table(self, table_name: str):
        """Get a table by name, creating it if it doesn't exist."""
        return self.db.table(table_name)
    
    # Example of a simple storage method
    def store(self, table_name: str, data: Dict[str, Any]):
        """Store data in a specified table."""
        table = self.get_table(table_name)
        return table.insert(data)
    
    # Example of a simple query method
    def find(self, table_name: str, query_func):
        """Find data in a specified table."""
        table = self.get_table(table_name)
        return table.search(query_func)

# Global database instance
_db_instance: Optional[DatabaseManager] = None

def get_database() -> DatabaseManager:
    """Get or create the global database instance."""
    global _db_instance
    if _db_instance is None:
        _db_instance = DatabaseManager()
    return _db_instance