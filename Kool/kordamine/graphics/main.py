from tkinter import *


def save_info():
    firstname_info = firstname.get()  # võtab info kastidest
    lastname_info = lastname.get()  # võtab info kastidest
    age_info = age.get()  # võtab info kastidest
    age_info = str(age_info)  # vanus on int
    print(firstname_info, lastname_info, age_info)  # prindib nime, perekonnanime ja vanuse
    file = open("user.txt", "w")  # avab faili kirutamise moodis
    file.write(firstname_info)  # kirjutab faili info
    file.write(lastname_info)  # kirjutab faili info
    file.write(age_info)  # kirjutab faili info
    file.close()  # suleb faili
    print("User", firstname_info, "has been registered successfully")  # prindib nime ja et see on registreeritud

    firstname_entry.delete(0, END)  # kustutab teksti kastis
    lastname_entry.delete(0, END)  # kustutab teksti kastis
    age_entry.delete(0, END)  # kustutab teksti kastis


screen = Tk()  # loob ekraani
screen.geometry("500x500")  # ekraani suurused 500 x 500
screen.title("Python Form")  # programmi pealis
heading = Label(text="Python Form", bg="grey", fg="black", width="500", height="3")  # programmi pealis
heading.pack()  # programmi pealis

firstname_text = Label(text="Firstname * ", )  # loob eesnime teksti
lastname_text = Label(text="Lastname * ", )  # loob perekonnanime teksti
age_text = Label(text="Age * ", )  # loob vanuse teksti

firstname_text.place(x=15, y=70)  # asetab ees nime teksti oma asukohta
lastname_text.place(x=15, y=140)  # asetab perekonna nime teksti oma asukohta
age_text.place(x=15, y=210)  # asetab vanuse teksti oma asukohta

firstname = StringVar()  # eesnimi on sõne
lastname = StringVar()  # perekonnanimi on sõne
age = IntVar()  # vanus on täisnumbriline muutuja

firstname_entry = Entry(textvariable=firstname, width=30)  # loob ees nime kasti oma asukohta
lastname_entry = Entry(textvariable=lastname, width=30)  # loob perekonna nime kasti oma asukohta
age_entry = Entry(textvariable=age, width=30)  # loob vanuse kasti oma asukohta

firstname_entry.place(x=15, y=100)  # asetab ees nime kasti oma asukohta
lastname_entry.place(x=15, y=180)  # asetab perekonna nime kasti oma asukohta
age_entry.place(x=15, y=240)  # asetab vanuse kasti oma asukohta

register = Button(screen, text="Register", width="30", height="2", command=save_info,
                  bg="grey")  # loob registreerimise nuppu
register.place(x=15, y=290)  # asetab nupu oma asukohta

screen.mainloop()  # alustab main loopi
