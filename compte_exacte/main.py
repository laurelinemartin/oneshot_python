from random import randint

while True:
    mini = int(input("Choisir la borne minimale : "))
    maxi = int(input("Choisir la borne maximale : "))
    print("")
    tour = 0
    alea = randint(mini, maxi)
    user = 0
    while user != alea:
        user = int(input("Entrer un nombre entre {0} et {1} : ".format(mini,maxi)))
        if user not in [_ for _ in range(mini, maxi+1)]:
            continue
        tour += 1
        if user < alea:
            print("C'est plus...")
        elif user > alea:
            print("C'est moins...")
    
    print("Yay ! En seulement {} tour(s).".format(tour))
    play = input("\nRejouer ? o / n : ").lower() == "o"
    if not play:
        break
    
print("A plus ! (ou moins) (:")
