import socket  # impordib mooduli socket

s = socket.socket()  # seab muutujale socketi classi
host = socket.gethostname()  # seab muutujaks enda hostname
port = 8080  # seab pordi
s.bind((host, port))  # ühendab hostiga just sellel pordil
s.listen(1)  # valmis vastuvõtma infot
print(host)  # prindib iseenda hostname
print("Waiting for any incoming connections ...")  # prindib rea
conn, addr = s.accept()  # võtab ühenduse vastu
print(addr, "Has connected to the server")  # prindib rea
filename = input(str("Please enter the filename of the file:"))  # küsib failinime
file = open(filename, 'rb')  # avab faili eelneva nimega
file_data = file.read(1024)  # loeb faili
conn.send(file_data)  # saadab faili info
print("Data has been transmitted successfully")  # prindib rea
