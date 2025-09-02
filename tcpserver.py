import socket

MAX_BYTES = 65535

def read_latest_uptime():
    try:
        with open("uptime_data.tsv", "r") as file:
            #lines = file.readlines()
            return file.read().strip() if file else "No uptime data available."
    except FileNotFoundError:
        return "uptime_data.tsv not found."

def server():
    server_ip = '0.0.0.0'
    server_port = 3333
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((server_ip, server_port))
    sock.listen(1)

    print(f"Listening for TCP connections at {server_ip}:{server_port}...")

    while True:
        conn, address = sock.accept()
        print(f"Connection established with {address}")
        _ = conn.recv(MAX_BYTES)  # Dummy receive
        latest_uptime = read_latest_uptime()
        conn.sendall(latest_uptime.encode())
        conn.close()

if __name__ == '__main__':
    server()