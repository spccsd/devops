import socket

MAX_BYTES = 65535

def client():
    server_ip = '3.108.235.109'  # Public IP of the AWS instance
    server_port = 3333
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = 'Request uptime'
    sock.sendto(message.encode(), (server_ip, server_port))

    server_data, _ = sock.recvfrom(MAX_BYTES)
    print(f"Latest uptime data: {server_data.decode()}")

if __name__ == '__main__':
    client()
