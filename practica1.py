lista=[]
maxi=float(input("Introduzca un número: "))
lista.append(maxi)
nmax=0
for i in range (9):
    lista.append(float(input("Introduzca un número: ")))
for i in range (len(lista)):
    if  lista[i]> maxi:
        nmax=1
        maxi=lista[i]
    elif lista[i]==maxi:
        nmax+=1
print(f"El máximo es {maxi} y sale {nmax} veces")