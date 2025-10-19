from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer
from textual.containers import Container

class SettingsScreen(Screen):
    """
    Simple settings screen placeholder.
    """
    
    def compose(self) -> ComposeResult:
        """Create child widgets."""
        yield Header()
        
        with Container(id="content"):
            yield Static("Settings Screen", id="title")
            yield Static("This is a placeholder for the settings screen.")
        
        yield Footer()