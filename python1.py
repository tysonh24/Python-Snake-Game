import http.server
import socketserver
import webbrowser
import os
from pathlib import Path
import time

def main():
    PORT = 8000
    current_dir = Path(__file__).parent.absolute()
    
    # Check if snake_game.html exists
    html_path = current_dir / 'snake_game.html'
    if not html_path.exists():
        print("Error: snake_game.html not found in the same directory as this script")
        return
    
    # Change to the directory containing the script
    os.chdir(current_dir)
    
    # Create and start the server
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)
    
    print(f"Starting server at http://localhost:{PORT}")
    
    # Start the server in a way that doesn't block
    import threading
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    # Give the server a moment to start
    time.sleep(1)
    
    # Open the web page using localhost instead of file:// protocol
    url = f'http://localhost:{PORT}/snake_game.html'
    print(f"Opening Snake game at: {url}")
    webbrowser.open_new(url)
    
    try:
        # Keep the main thread running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.shutdown()
        httpd.server_close()
        print("Server stopped.")

if __name__ == '__main__':
    main() 