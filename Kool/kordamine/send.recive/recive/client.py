import socket  # impordib mooduli socket

s = socket.socket()  # seab muutujale socketi classi
host = input(str("Please enter the host address of the sender:"))  # küsib hostinime
port = 8080  # seab pordi
s.connect((host, port))  # ühendab hostiga just sellel pordil
print("Connected ...")  # prindib rea
filename = input(str("Please enterafilename for the incoming file:"))  # küsib kasutaja käest faili nime
file = open(filename, 'wb')  # loob uue faili eelneva nimega
file_data = s.recv(1024)  # küsib hosti käest infot
file.write(file_data)  # kirjutab info uute faili
file.close()  # suleb saadetud faili
print("File has been received successfully.")  # prindib rea
