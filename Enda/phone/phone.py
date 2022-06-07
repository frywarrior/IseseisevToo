ui = str(input("Sisestage failinimi: "))
hind = float(input("Sisestage kõne minuti hind: "))
kokku, nr, ui = 0, 0, open(ui, encoding="Utf8")
for i in ui:
    i = int(i)
    if i > 600:
        i = hind * 10
    elif i < 60:
        i = hind * 1
    else:
        i = i * (hind/ 60)
    print(f"Kõne maksumus: {i}")
    kokku += i
    nr += 1
print(f"Kõnede arv: {nr} \nKogu arve: {round(kokku, 2)} EUR")
