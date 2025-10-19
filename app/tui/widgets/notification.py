from textual.widgets import Static
from textual.containers import Container
from textual.reactive import reactive

class NotificationWidget(Static):
    """
    Simple widget for displaying a notification.
    """
    
    title = reactive("Notification")
    content = reactive("")
    app_name = reactive("Unknown")
    
    def __init__(
        self,
        title: str = "Notification",
        content: str = "",
        app_name: str = "Unknown",
        **kwargs
    ):
        """Initialize a notification widget."""
        super().__init__(**kwargs)
        self.title = title
        self.content = content
        self.app_name = app_name
    
    def compose(self):
        """Compose the notification widget."""
        with Container(classes="notification"):
            yield Static(f"[b]{self.title}[/b]")
            yield Static(self.content)
            yield Static(f"From: {self.app_name}", classes="app-name")