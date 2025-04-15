from random import randint
import sys

hp_moi = 50
hp_ennemi = 50
stock_potion = 3
choix_possible = ["1","2"]
choix = ""
message = "Décider d'attaquer (1) ou prendre une potion (2) "

print("-----------------------------Bienvenue sur Text Fight-----------------------------")
print("Vous êtes face à l'incorruptible kikootroll du net, qui de vous deux l'emportera ?")
print("Pour ça, vous pouvez : ")

while hp_moi > 0 or hp_ennemi > 0:
    degats_moi = randint(5, 10)
    degats_ennemi = randint(5, 15)
    while not choix in choix_possible:
        choix = input(message)
    if choix == "2":
        if stock_potion != 0:
            soin_potion = randint(15, 50)
            stock_potion -= 1
            hp_moi += stock_potion
            hp_moi -= degats_ennemi
            print(f"Vous regagnez {soin_potion} points de vie.")
            for i in range (2):
                if i == 1:
                    print("Vous passez ce tour-ci.")
                print(f"Le kikoo vous fait {degats_ennemi} points de dégats")
                print("----")
                if hp_ennemi <= 0:
                    break
                if hp_moi <= 0 :
                    break
                print(f"Il vous reste {hp_moi} point{'s' if hp_moi>1 else ""} de vie.")
                print(f"Il reste {hp_ennemi} point{'s' if hp_ennemi>1 else ""} de vie au kikoo.")
            choix = ""
        else:
            print("Vous n'avez plus de potion!")
            choix = ""

    if choix == "1":
        hp_moi -= degats_ennemi
        hp_ennemi -= degats_moi
        print(f"Vous faites {degats_moi} points de dégats au kikoo!")
        print(f"Le kikoo vous {degats_ennemi} points de dégats.")
        print("----")
        if hp_ennemi <= 0:
            break
        if hp_moi <= 0 :
            break
        print(f"Il vous reste {hp_moi} point{'s' if hp_moi>1 else ""} de vie.")
        print(f"Il reste {hp_ennemi} point{'s' if hp_ennemi>1 else ""} de vie au kikoo.")
        choix = ""

if hp_ennemi <= 0:
    print("Félicitations! Vous avez renvoyé le kikootroll pleurer derrière son écran.")
    sys.exit()
else:
    print("Quoi?! Vous avez perdu ?! Je sens quelqueuh ch0seuh 2 biïzarr€...")
    print("Maàiiïs qqkk'essk'îil m'@@rRiiïveuùhhh???")
    sys.exit()
           