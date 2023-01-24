import datetime
today = datetime.datetime.now()
godina = today.year
while True:
    ime = input("Vnesi Ime: ")
    prezime = input("Vnesi Prezime: ")
    godina_ragjanje = int(input("Vnesi godina na ragjanje: "))
    godini = godina - godina_ragjanje
    polnoleten = 0
    maloleten = 0
    if (godini >= 18):
        print("{} e polnoleten".format(ime))
        polnoleten += polnoleten
    else:
        print("{} e maloleten".format(ime))
        maloleten += maloleten
    da_ne = input("Dali sakate da prodolzite da/ne: ")
    if (da_ne == 'ne'):
        break

print("Ima vkupno {} maloletni, a {} polnoletni".format(maloleten,polnoleten))
