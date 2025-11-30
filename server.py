"""
Course: Computer Networks
Project: Simple HTTP Web Server
Date: November 2025

Team: PHQ
Members & Roles:
1. Sourav Md Shariful Islam (ID: [Student ID]) - Networking Logic
2. Tamim Md (ID: [Student ID]) - Request Routing & File Handling
3. Ahammed Tanim (ID: [Student ID]) - Client Implementation
4. Fahad Md Mainuddin (ID: [Student ID]) - Testing & Documentation

Description:
This program implements a multi-threaded HTTP/1.1 server.
It serves files strictly from the 'public' directory.
"""

import socket
import threading
import os

# Server Configuration
HOST = '127.0.0.1'
PORT = 8080
PUBLIC_DIR = 'public'  # Files are served from this folder

def get_content_type(filename):
    """
    Determines MIME type based on file extension.
    Implemented by: Tamim Md
    """
    if filename.endswith('.html'):
        return 'text/html'
    elif filename.endswith('.txt'):
        return 'text/plain'
    elif filename.endswith('.jpg') or filename.endswith('.jpeg'):
        return 'image/jpeg'
    return 'application/octet-stream'

def handle_client(client_socket):
    """
    Handles a single client connection.
    Logic by: Tamim Md (Routing) & Sourav Md Shariful Islam (Socket)
    """
    try:
        request = client_socket.recv(1024).decode('utf-8')
        if not request:
            return

        # Parse HTTP Request Line
        lines = request.split('\r\n')
        request_line = lines[0]
        try:
            method, path, protocol = request_line.split()
        except ValueError:
            return

        print(f"[REQUEST] {method} {path}")

        # Default to index.html if root is requested
        if path == '/':
            path = '/index.html'
        
        # Security: Remove leading slash to join correctly with PUBLIC_DIR
        safe_path = path.lstrip('/')
        file_path = os.path.join(PUBLIC_DIR, safe_path)

        # Checking if file exists inside the public folder
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
            
            content_type = get_content_type(file_path)
            content_length = len(content)

            # HTTP/1.1 200 OK Response
            response_header = (
                f"HTTP/1.1 200 OK\r\n"
                f"Content-Type: {content_type}\r\n"
                f"Content-Length: {content_length}\r\n"
                f"Connection: close\r\n"
                f"\r\n"
            )
            client_socket.sendall(response_header.encode('utf-8') + content)
        else:
            # HTTP/1.1 404 Not Found Response
            error_msg = "<h1>404 Not Found</h1><p>File not found in public folder.</p>"
            response_header = (
                "HTTP/1.1 404 Not Found\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(error_msg)}\r\n"
                "Connection: close\r\n"
                "\r\n"
            )
            client_socket.sendall(response_header.encode('utf-8') + error_msg.encode('utf-8'))

    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        client_socket.close()

def start_server():
    """
    Main server loop.
    Implemented by: Sourav Md Shariful Islam
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((HOST, PORT))
    except OSError:
        print(f"Error: Port {PORT} is busy. Try changing PORT in server.py")
        return

    server.listen(5)
    print(f"[*] Team PHQ Server running on http://{HOST}:{PORT}")
    print(f"[*] Serving files from ./{PUBLIC_DIR}/")

    while True:
        client_sock, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_sock,))
        client_handler.start()

if __name__ == "__main__":
    # Checking public dir exists
    if not os.path.exists(PUBLIC_DIR):
        print(f"Warning: '{PUBLIC_DIR}' folder missing. Creating it...")
        os.makedirs(PUBLIC_DIR)
    start_server()