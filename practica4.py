lista=[]
pares=0
impares=0
for i in range (10):
    lista.append(float(input("Inserte un número: ")))
    if i%2==0:
        pares+=lista[i]
    else:
        impares+=lista[i]
print(f"{lista}\nLa media de los números en las posiciones pares es: {pares/5} y la media de las posiciones impares es: {impares/5}")