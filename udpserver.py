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
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((server_ip, server_port))
    print(f"Listening for UDP datagrams at {server_ip}:{server_port}...")

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        print(f"Received request from {address}")
        latest_uptime = read_latest_uptime()
        sock.sendto(latest_uptime.encode(), address)

if __name__ == '__main__':
    server()