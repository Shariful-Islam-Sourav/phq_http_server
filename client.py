"""
Course: Computer Networks
Project: HTTP Client
Team: PHQ

Implemented by: Ahammed Tanim
Role: Client UI & Command Line Interface
"""

import socket
import sys

HOST = '127.0.0.1'
PORT = 8080

def get_page(filename):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))

        # Standard HTTP GET Request
        request = (
            f"GET /{filename} HTTP/1.1\r\n"
            f"Host: {HOST}\r\n"
            f"Connection: close\r\n"
            f"\r\n"
        )

        client.sendall(request.encode('utf-8'))

        response = b""
        while True:
            chunk = client.recv(4096)
            if not chunk:
                break
            response += chunk

        print(f"--- Team PHQ Client: Requesting /{filename} ---")
        print(response.decode('utf-8', errors='replace'))
        print("\n-------------------------------------------")

    except ConnectionRefusedError:
        print("Error: Could not connect. Make sure server.py is running.")
    finally:
        client.close()

if __name__ == "__main__":
    file_to_get = "index.html"
    if len(sys.argv) > 1:
        file_to_get = sys.argv[1]
    
    get_page(file_to_get)