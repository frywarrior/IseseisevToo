import socket  # importib mooduli nimega socket

s = socket.socket()  # loob uue pistikupesa
host = socket.gethostname()  # leiab arvuti hostname
print("server will start on host:", host)  # prindib arvuti hostname
port = 8081  # seab ühenduse pordi
s.bind((host, port))  # ühendab pistikupesa sellele aadressile
print("")  # prindib tühja rea
print("Server done binding to host and port successfully")  # prindib teksti
print("")  # prindib tühja rea
print("Server is waiting for incoming connections")  # prindib teksti
print("")  # prindib tühja rea
s.listen(1)  # lubab serveril ühendusi apsekteerda
conn, addr = s.accept()  # seab need kaks muutujad ühenduse loomiseks
print(addr, "Has connected to the server and is now online ...")  # prindib teksti
print("")  # prindib tühja rea

while 1:  # kui on tõene
    message = input(str(">>"))  # võtab kasutaja poolt sisestatud sõnumi
    message = message.encode()  # kodeerib sõnumi
    conn.send(message)  # saadab ühendusele eelneva sõnumi
    print("message has been sent ...")  # prindib teksti
    print("")  # prindib tühja rea
    incoming_message = conn.recv(1024)  # võtab socketist infot
    incoming_message = incoming_message.decode()  # dekodeerib saadud sõnumi
    print("Client:", incoming_message)  # prindib sõnumi
    print("")  # prindib tühja rea
