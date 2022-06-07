import socket  # importib mooduli nimega socket

s = socket.socket()  # loob uue pistikupesa# loob uue pistikupesa
host = input(str("Please enter the hostname of the server:"))  # prindib teksti
port = 8081  # seab ühenduse pordi
s.connect((host, port))  # ühendab pistikupesa sellele aadressile
print("Connected to chat server")  # prindib teksti
while 1:  # kui on tõene
    incoming_message = s.recv(1024) # võtab socketist infot
    incoming_message = incoming_message.decode() # dekodeerib saadud sõnumi
    print("Server:", incoming_message) # prindib sõnumi
    print("") # prindib tühja rea
    message = input(str(">>"))  # võtab kasutaja poolt sisestatud sõnumi
    message = message.encode() # kodeerib sõnumi
    s.send(message) # saadab ühendusele eelneva sõnumi
    print("message has been sent ...")  # prindib teksti
    print("")   # prindib tühja rea
