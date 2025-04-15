import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

temp_absolu = []
temp_base = []
temp_mini = 0
index = []
resultat = 0
x = 0


n = int(input())  # the number of temperatures to analyse
for temp in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(temp)
    x += 1
    temp_base.append(t)
    if t < 0 :
        temp_absolu.append(t * (-1))
        t_absolu = t * (-1)
    else : 
        temp_absolu.append(t)
        t_absolu = t

if x > 0 :
    x = 0
    temp_mini = temp_absolu[0]
#recherche de la valeur absolue la + petite    
for i, temp in enumerate(temp_absolu):
    if temp < temp_mini:
        temp_mini = temp_absolu[i]
#recherche du nombre d'itération de cette valeur et de l'index de chaque itération
for i, temp in enumerate(temp_absolu):
    if temp == temp_mini:
        index.append(i)

# gestion de 1 résultat en valeur absolue
if len(index) == 1:
    if temp_absolu[index[0]] != temp_base[index[0]] :
        resultat = temp_mini * (-1)
    elif temp_absolu[index[0]] == temp_base[index[0]]:
        resultat = temp_mini
# gestion de plus de 1 résultat en valeur absolue
elif len(index) > 1 :
    for i in index :
        if temp_absolu[i] == temp_base[i]:
            resultat = temp_mini
            break
        else :
            resultat = temp_mini * (-1)

print(resultat)




# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)