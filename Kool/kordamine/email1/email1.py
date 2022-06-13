import smtplib # impordib smtplib

sender_email = "vikk.opilane@outlook.com" # kes saadab meili
rec_email = "rovan.kutt@vikk.ee" # kellele saadab meili
password = input(str("Please enter your password: ")) # küsib meili parooli

SUBJECT = "Hello!" # Seab teema
TEXT = "This message was sent with Python's smtplib." # Seab teksti sisu
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT) # Koostab meili

server = smtplib.SMTP('smtp-mail.outlook.com', 587) # sisestab emaili
server.starttls() # alustab starttlsi
server.login(sender_email, password) # logib sisse emaili
print("Login success") # prindib et logisid sisse
server.sendmail(sender_email, rec_email, message) # saadab meili
print("Email has been sent to ", rec_email) # prindib et meil on saadetud
