povtoruvanje =int(input("Vnesi kolku pati da se povtoruva ciklusot: \n"))

for i in range(povtoruvanje):
    denari = int(input("Vnesi denari za konverzacija vo EUR: \n"))
    evra = denari * 61.5
    print("Evra: {}".format(evra))