import socket
import sys
import time

host = socket.gethostname()
print(f"server will start on host . {host}")
port = 8080