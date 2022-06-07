import socket  # importib mooduli nimega socket

s = socket.socket()  # loob uue pistikupesa# loob uue pistikupesa
host = input(str("Please enter the hostname of the server:"))
port = 8081  # seab ühenduse pordi
s.connect((host, port))  # ühendab pistikupesa sellele aadressile
print("Connected to chat server")
while 1:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server:", incoming_message)
    print("")
    message = input(str(">>"))
    message = message.encode()
    s.send(message)
    print("message has been sent ...")
    print("")
