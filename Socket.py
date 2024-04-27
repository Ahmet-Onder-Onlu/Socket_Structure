# An example script to connect to Google using socket 
# programming in Python 
import socket # for socket 
import sys 

def send_request(host, port, message):
    try:
        # Soket oluştur
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")

        # Sunucuya bağlan
        s.connect((host, port))
        print(f"Socket connected to {host} on port {port}")

        # İstek gönder
        s.sendall(message.encode())

        # Veri al
        data = s.recv(1024)
        print("Received", repr(data.decode()))

    except socket.error as err:
        print("Socket creation or connection failed with error:", err)
    finally:
        # Soketi kapat
        s.close()

try: 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	print ("Socket successfully created")
except socket.error as err: 
	print ("socket creation failed with error %s" %(err))

# default port for socket 
port = 80

try: 
	host_ip = socket.gethostbyname('www.google.com') 
except socket.gaierror: 

	# this means could not resolve the host 
	print ("there was an error resolving the host")
	sys.exit() 

# connecting to the server 
s.connect((host_ip, port)) 

print ("the socket has successfully connected to google") 

message = "GET /search?q=What+is+the+socket HTTP/1.1\r\nHost: www.google.com\r\n\r\n"

host = 'www.google.com'

send_request(host, port, message)
