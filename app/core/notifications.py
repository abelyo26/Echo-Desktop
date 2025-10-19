import logging
from typing import Dict, List, Any
import time

logger = logging.getLogger(__name__)

class NotificationManager:
    """
    Simple notification manager.
    """
    
    def __init__(self, max_notifications: int = 100):
        """
        Initialize notification manager.
        
        Args:
            max_notifications: Maximum number of notifications to store
        """
        self.notifications = {}
        self.max_notifications = max_notifications
    
    def add_notification(self, title: str, content: str, app_name: str = "Unknown"):
        """
        Add a new notification.
        
        Args:
            title: Notification title
            content: Notification content
            app_name: Source application name
        """
        notification_id = str(int(time.time() * 1000))
        notification = {
            "id": notification_id,
            "title": title,
            "content": content,
            "app_name": app_name,
            "timestamp": time.time(),
            "dismissed": False
        }
        
        self.notifications[notification_id] = notification
        logger.info(f"New notification: {title}")
        
        # Trim if needed
        if len(self.notifications) > self.max_notifications:
            oldest_id = min(self.notifications.keys(), 
                           key=lambda k: self.notifications[k]["timestamp"])
            del self.notifications[oldest_id]
        
        return notification_id
    
    def get_notifications(self, limit: int = None) -> List[Dict[str, Any]]:
        """
        Get recent notifications.
        
        Args:
            limit: Maximum number to return
            
        Returns:
            List of notifications
        """
        notifications = list(self.notifications.values())
        notifications.sort(key=lambda n: n["timestamp"], reverse=True)
        
        if limit:
            notifications = notifications[:limit]
            
        return notifications
