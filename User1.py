import socket

# This is func which contain sender's infos
def send_message(message, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())

# This is func which contain receive's infos
def receive_message(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            print('Received', repr(data.decode()))

if __name__ == "__main__":
    
    # User1, User2'den gelen mesajı alır
    user1_port = 65431
    receive_message(user1_port)
    
    # User1, User2'ye mesaj gönderir
    message = "Merhaba, User2!"
    user2_host = '127.0.0.1'
    user2_port = 65432
    send_message(message, user2_host, user2_port)