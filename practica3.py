import random as r
lista=[]
for i in range (10):
    lista.append(r.randint(0,100))
print(lista)
for i in range(len(lista)):
    if lista[i]%2==0:
        print(f"El número {lista[i]} es par y se encuentra en la posición {i}")
