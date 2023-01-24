vkupna_cena = 0
while True:
    produkt = input("Vnesi go produktot: ")
    cena = int(input("Vnesi ja cenata: "))
    vkupna_cena += cena
    da_ne = input("Dali sakate da prodolzite (da/ne): ")
    if (da_ne == 'ne'):
        break

print("Imate vkupno {} ".format(vkupna_cena))
plakanje = int(input("Vnesete ja uplatata: "))
while True:
    if (plakanje < vkupna_cena):
        plakanje = int(input("Ve molime uplatete poveke od {} ".format(vkupna_cena)))
    else:
        break
kusur = plakanje - vkupna_cena
print("Uplateni se {} den, vkupnata cena e {}, kusurot e {}".format(plakanje, vkupna_cena, kusur))
