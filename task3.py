povtoruvanje = int(input("Kolku pati da se povtoruva ciklusot? :\n"))

for i in range(povtoruvanje):
    if (i == 0):
        continue
    if (i % 2 == 0):
        print("Brojot {} e paren".format(i))
