alumnos=[]
suma=bajos=altos=0
nalumnos=int(input("Introduzca el número de alumnos: "))
for i in range (nalumnos):
    alumnos.append(int(input("Altura en centímetros: ")))
    suma+=alumnos[i]
for i in range (len(alumnos)):
    if alumnos[i]<suma/len(alumnos):
        bajos+=1
    elif alumnos[i]>suma/len(alumnos):
        altos+=1
print(f"Las alturas de los alumnos son {alumnos} \nHay {altos} personas más altas que la media y {bajos} personas más bajas." )