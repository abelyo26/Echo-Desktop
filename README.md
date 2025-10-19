# Echo Desktop

A terminal-based (TUI) companion to the Echo mobile app. Acts as a local bridge between your PC and phone over Wi-Fi.

## Features

- File sharing
- Clipboard synchronization
- Notification mirroring

## Requirements

- Python 3.13 or later
- Wi-Fi network for device communication

## Running the App

```bash
# Run with TUI interface
python main.py

# Run in headless mode (API only)
python main.py --headless

# Enable debug logging
python main.py --debug
```

## Project Structure

This is a simplified file structure with minimal implementations.

```
/Echo-Desktop/
├── app/
│   ├── api/               # FastAPI endpoints
│   ├── core/              # Core functionality
│   │   └── database.py    # TinyDB implementation
│   ├── tui/               # Textual UI components
│   └── config/            # App settings
├── main.py                # Entry point
└── README.md              # This file
```
