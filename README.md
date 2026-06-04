# Collatz Conjecture

Interactive 3x+1 / Collatz visualizer with a Python backend for large numbers.

## Quick start (Windows)

Double-click **`run.bat`** — installs Flask, starts the server, and opens http://localhost:8080

Or manually:

```bash
pip install -r requirements.txt
python server.py
```

Then open **http://localhost:8080** in your browser.

## Files

| File | Purpose |
|---|---|
| `collatz.html` | Web UI |
| `server.py` | Flask backend — serves the page and `/compute` API |
| `collatz_core.py` | Shared algorithm logic |
| `weird_algorithm.py` | Command-line version |

## CLI

```bash
python weird_algorithm.py
```
