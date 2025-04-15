import random

num_a_deviner = str(random.randint(0,100))
reponse = ""

print("J'ai choisi mon nombre, à ton tour de le trouver!")
reponse = input("Choisis un nombre entre 1 et 100 : ")
for i in range(6):
    if not reponse.isdigit():
        print("C'est un chiffre qu'il faut donner!")
        reponse = input("Choisis un nombre entre 1 et 100 : ")
    elif reponse == num_a_deviner:
        print(f"Félicitations, tu as trouvé en {i+1} essai{'s'if (i+1)>1 else ''}!!")
        break
    elif reponse > num_a_deviner:
        print("Un petit peu trop haut! Le chiffre que j'ai choisi est plus petit")
        reponse = input("Choisis un nombre entre 1 et 100 : ")
    elif reponse < num_a_deviner:
        print("Trop petit, j'ai choisi un nombre plus grand")
        reponse = input("Choisis un nombre entre 1 et 100 : ")
print("Dommage c'est raté!!")