from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.binding import Binding
from textual.containers import Container


class EchoDesktopApp(App):
    """
    Simple Textual application for Echo Desktop.
    """

    TITLE = "Echo Desktop"
    SUB_TITLE = "Local device connectivity"

    BINDINGS = [
        # Binding("q", "quit", "Quit"),
        Binding("d", "toggle_dark", "Toggle dark mode"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets."""
        yield Header()

        with Container(id="main"):
            yield Static("Welcome to Echo Desktop!")
            yield Static("A terminal-based companion to the Echo mobile app.")
            yield Static("This is a simplified placeholder UI.")

        yield Footer()

    async def on_mount(self) -> None:
        """Handle app start-up."""
        # self.is_running = True

    def action_toggle_dark(self) -> None:
        """Toggle dark mode."""
        self.dark = not self.dark

    async def on_shutdown(self) -> None:
        """Handle application shutdown."""
        # self.is_running = False
