import socket
from app.server import start
from colorama import Fore
 
def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

print(Fore.GREEN + f"[INFO] Starting server on ip {get_local_ip()}")
try:
    start(get_local_ip())
except Exception as e:
    print(Fore.RED + f"[ERROR] {e}")