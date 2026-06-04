@echo off
cd /d "%~dp0"
echo Installing dependencies...
pip install -r requirements.txt -q
echo.
echo Starting server at http://localhost:8080
echo Press Ctrl+C to stop.
echo.
start "" "http://localhost:8080"
python server.py
