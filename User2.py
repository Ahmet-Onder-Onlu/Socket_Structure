import socket

def send_message(message, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())

def receive_message(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            print('Received', repr(data.decode()))

if __name__ == "__main__":
    # User2, User1'e mesaj gönderir
    message = "Merhaba, User1!"
    user1_host = '127.0.0.1'
    user1_port = 65431
    send_message(message, user1_host, user1_port)

    # User2, User1'den gelen mesaji alir
    user2_port = 65432
    receive_message(user2_port)