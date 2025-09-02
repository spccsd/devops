import socket

MAX_BYTES = 65535

def client():
    server_ip = '3.108.235.109'  # Public IP of the AWS instance
    server_port = 3333
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))
    print(f"Connected to {server_ip}:{server_port}")

    message = 'Request uptime'
    sock.sendall(message.encode())
    server_data = sock.recv(MAX_BYTES)
    print(f"Latest uptime data: {server_data.decode()}")
    sock.close()

if __name__ == '__main__':
    client()
