# impordib moodulid
from tkinter import *
import linecache


# teeb kasutaja registreerimise funktsiooni
def register_user():
    # võtab teisest funktsioonist kasutaja nime ja parooli
    username_info = username.get()
    password_info = password.get()

    # loob uue faili kasutaja nime ja parooliga
    file = open(username_info + ".txt", "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    # kustutab inputi lahtrid
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    # Prindib registreerimise tulemuse
    Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()


def register():
    # seab muutuja screen 1 globaalseks
    global screen1

    # loob screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    # seab muutujad globaalseks
    global username
    global password
    global username_entry
    global password_entry

    # defineerib nime ja parooli
    username = StringVar()
    password = StringVar()

    # loob nupud ja tksti ekraanil
    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username*").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password*").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login_user():
    # võtab teisest funktsioonist kasutaja nime ja parooli
    username_info = username.get()
    password_info = f"{password.get()}"

    # avab kasutaja info faili ja prindib tulemuse
    line = linecache.getline(fr"{username_info}.txt", 2)
    line = f"{line[:-1]}"
    if line == password_info:
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Label(screen1, text="Login Sucess", fg="green", font=("calibri", 11)).pack()


def login():
    # seab muutuja screen 1 globaalseks
    global screen1

    # loob screen1
    screen1 = Toplevel(screen)
    screen1.title("Login")
    screen1.geometry("300x250")

    # seab muutujad globaalseks
    global username
    global password
    global username_entry
    global password_entry

    # defineerib nime ja parooli
    username = StringVar()
    password = StringVar()

    # loob nupud ja tksti ekraanil
    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username*").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password*").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Login", width=10, height=1, command=login_user).pack()


def main_screen():
    # seab muutuja screen globaalseks
    global screen

    # loob screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")

    # loob nupud ja tksti ekraanil
    Label(text="Program", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    # uuendab screeni
    screen.mainloop()


# alustab main loopi
main_screen()
