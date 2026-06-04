# Collatz Conjecture Visualizer

An interactive, cosmic-themed web dashboard and command-line engine built to calculate, map, and visualize the mathematical patterns of the Collatz Conjecture.

This setup supports computing arbitrary-precision starting values with native support for high-digit numbers, drawing dynamic SVG path curves, and offering an offline client-side computation fallback architecture.

## Local Demo

The local interface runs entirely on your machine. Once launched, you can access the interface at:
[http://localhost:8080](https://www.google.com/search?q=http://localhost:8080)

## Project Layout

```text
collatz.html          Web interface workspace, SVG path rendering, and starfield canvas logic
server.py             Flask microservice hosting the static files and exposing the compute API
collatz_core.py       Shared core mathematical execution framework used by both Web and CLI
weird_algorithm.py    Pure command-line tool interface implementation for terminal operations
run.bat               Windows automation script to handle installation and execution setup
requirements.txt      Python package dependency definition list

```

## Features

* **Ultra-Large Number Support:** Computes starting values up to 10,000 digits long (meaning the largest supported value is $10^{10^{4}} - 1$) without thread locks, browser crashes, or execution lag.
* **Dynamic Charting:** Generates real-time vector mathematical peak charts utilizing structural bézier path smoothing.
* **Hybrid Execution Fallback:** Features built-in resilience. If the local Flask service is stopped or unreachable, the browser automatically switches to an internal JavaScript BigInt processing routine.
* **Dual-Mode Control:** Use either the browser-based web dashboard interface or run automated sets directly using a fast, native terminal application.

## Requirements

* Python 3.10 or higher.
* Flask library framework (handled automatically or via manual package manager setup).
* A modern web browser with BigInt and HTML5 Canvas capabilities.

## Quick Start

### Windows execution

Double-click `run.bat`. This automatically handles missing packages via pip, launches the local web server host, and automatically initializes the entry point directly inside your default browser shell.

### macOS and Linux execution

Install the required microservice packages and execute the server file inside your terminal window environment:

```bash
pip install -r requirements.txt
python server.py

```

To run the text-only terminal core application instead of the web engine framework, use:

```bash
python weird_algorithm.py

```

## Technical Architecture

### Downsampling Large Data Streams

To protect user interfaces from performance decay during extreme sequence sizes, the visualization script processes raw data payloads before building the DOM graphic structure.

```text
[Raw Sequence Array] ---> Max 2,000 Data Point Downsampler ---> Smooth Bezier SVG Path

```

When an input generates massive step counts, the application scales down the array using a calculated structural index step stride. This preserves the visual trajectory curve across the screen layout while keeping rendering performance entirely optimal.

### Fail-safe Communication Setup

The application prioritizes uptime by defaulting to a micro-Flask endpoint. When an evaluation starts, a network payload request passes to `/compute`. If a connection drop occurs, a local Javascript implementation overrides the interface state, maintaining functionality even if the Python process terminates.

## Credits

* Fonts: Google Fonts (Space Mono and Rajdhani typography profiles).
* Backend Library: Flask open-source microframework architecture project.

