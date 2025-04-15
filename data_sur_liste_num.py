listeNum = input("Entrez une liste de chiffres entiers séparés par des virgules sans espace :")
x = 0
posList = listeNum[x]
#permet de définir la longueur de la liste en comptant le rang 0 ex: "TOUTOU, le premier T est de rang 0 et le dernier U de rang 5"
longueurList = len(listeNum)-1

totalListe = 0
moyenneListe = 0
numSupMoy = 0
numPair = 0

#afficher liste : 
print(f"Votre liste est : {listeNum}")

#calcul total :
while x <= longueurList:
    posList = listeNum[x]
    totalListe += int(posList) 
    x += 2
     
print(f"Le total est de : {totalListe}")
x = 0

#moyenne (on prend la longueur de la liste + 1 car on a un chiffre + une virgule donc 2entrées = 1 chiffre, donc on rajoute +1 pour une entrée correspondant à la virgule que l'on a pas mise à la fin et on divise le tout par 2 :
moyenneListe = totalListe / ((len(listeNum)+1)/2)
print(f"La moyenne de cette liste : {moyenneListe}.")

#test pour savoir combien de nombres est >moyenne :
while x <= longueurList:
    posList = listeNum[x]
    if int(posList) > moyenneListe:
        numSupMoy += 1
    x += 2
print(f"Le nombre d'entrées supérieures à la moyenne est de : {numSupMoy}.")
x = 0

#test pour savoir combien de nombres de la liste sont pairs:
while x <= longueurList:
    posList = listeNum[x]
    if (int(posList) % 2)==0 :
        numPair +=1
    x += 2
print("Il y a", numPair, "nombres pairs dans ta liste.")