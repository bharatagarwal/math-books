# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Serve the reader. Run: uv run reader/serve.py"""
import http.server, os, webbrowser
from pathlib import Path

os.chdir(Path(__file__).parent.parent)
print("\n  http://localhost:8765/reader/\n")
webbrowser.open("http://localhost:8765/reader/")

with http.server.HTTPServer(("", 8765), http.server.SimpleHTTPRequestHandler) as s:
    try: s.serve_forever()
    except KeyboardInterrupt: print("\nStopped")
