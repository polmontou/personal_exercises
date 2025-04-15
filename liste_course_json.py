from sys import exit
import os
import json 

chemin_liste = r"C:\Users\paulm\Desktop\CODE\EXO\liste.json"
choix_possible = ["1","2","3","4","5"]
liste_course = []

# test liste en mémoire + affichage
def test():
    if os.path.exists(chemin_liste):
        with open(chemin_liste,"r") as f:
            liste_stock = json.load(f)
        if liste_stock != []:
            print(f"Votre liste de course contient :")
            for i, element in enumerate(liste_stock):
                print(f"{i+1} - {element}")
                liste_course.append(element)
        else:
            print("Votre liste de course est actuellement vide.")

# message d'accueil
def accueil():
    print("Que voulez-vous faire ?")
    print(" 1 - Ajouter un nouvel élément à votre liste")
    print(" 2 - Retirer un élément de votre liste")
    print(" 3 - Afficher votre liste actuelle")
    print(" 4 - Vider votre liste")
    print(" 5 - Quitter le programme")
    numero_choix()

# ajout d'un élément à la liste
def ajout():
    nouvel_element = input("Que voulez-vous ajouter ? ")
    nouvel_element = nouvel_element.capitalize()
    if nouvel_element in liste_course:
        print(f"{nouvel_element} fait déjà partie de votre liste de course!")
    else:    
        liste_course.append(nouvel_element)
        print(f"{nouvel_element} a bien été ajouté à votre liste!")
    accueil()

# retrait élement de la liste
def retrait():
    element_a_enlever = input("Que voulez-vous enlever ? ")
    element_a_enlever = element_a_enlever.capitalize()
    if liste_course == []:
        print("Votre liste de course est vide.")
    elif not element_a_enlever in liste_course:
        print(f"{element_a_enlever} ne fait pas partie de votre liste de course!")
    else:
        liste_course.remove(element_a_enlever)
        print(f"{element_a_enlever} a bien été retiré de votre liste!")
    accueil()

# afficher la liste
def affichage():
    if liste_course == []:
        print("Votre liste de course est vide!")
    else:
        print("Votre liste contient :")
        for i, element in enumerate(liste_course) :
            print(f"  {i+1} - {element}")
    accueil()

# vider la liste
def vider():
    if liste_course == []:
        print('Votre liste de course est déjà vide!')
    else:
        liste_course.clear()
    accueil()

# quitter le programme + sauvegarde
def quitter():
    with open(chemin_liste, "w") as f:
        json.dump(liste_course, f, ensure_ascii=False)
    
    print("Merci et à bientôt :)")
    exit()

# choix
def numero_choix():
    choix = input("Entrez votre choix de 1 à 5 : ")
    while not choix in choix_possible:
        print("Choississez un chiffre compris entre 1 et 5")
        choix = input("Entrez votre choix de 1 à 5 : ")
    match choix :
        case "1":
            ajout()
        case "2":
            retrait()
        case "3":
            affichage()
        case "4":
            vider()
        case "5":
            quitter()




print("Bienvenue sur votre gestionnaire de liste de courses !")
test()
accueil()
