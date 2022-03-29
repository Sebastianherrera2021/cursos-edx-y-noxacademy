"""El interés compuesto es aquel que se suma al 
capital inicial, por lo que va generando nuevos intereses."""
"""El capital final dependerá de tres valores:
C : El capital disponible inicialmente.
i : El tipo de interés compuesto.
n : El número de periodos (por ejemplo, años)."""
t=int(5) #años
i=float(0.015) #tasa
capital=int(3000) #antes era 10000
m=capital*(1+i)**t #nuevo capital
print(m)
print(f"El capital final es de {m:.2f} €") #dos decimales
#################################################################
##comisiones mantenimiento
f=5 #comisión mensual
G=f*12*t #meses
print(f"el gasto total en comisiones es de {G:.2f} $ ")
##################################################################
###ahorros al finalizar el periodo
s=m-G
print(f"El saldo en cuentra tras {t} años es de {s:.2f} $")
##################################################################

###ver si hemos ahorrado dinero
hay_ahorro=s>capital #devuelve valor booleano
print(f"¿hemos incrementado nuestro capital al finalizar el periodo? => {hay_ahorro}")


#### 2 EJERCICIO
"""En esta ocasión, vamos a ocupar el rol de un profesor 
que quiere llevar un buen control de las notas de sus estudiantes."""

LISTA=["Juan gonzales", "María moreno","Julia Sánchez", "pedro vidal"]
print(LISTA)

notas=[]
notas.append((7.5,6.2,8.1)) #append añade nuevos elementos al final de una lista
notas.append((9.3,7.4,7.7))
notas.append((5.6,4.1,4.4))
notas.append((3.8,4.1,6.4))
print(notas)

##todos los examenes valen 1/3 de la nota
"""guardar nota media en un diccionaria que tenga como clave
el nombre del estudainte "cadena texto" y valor numerico 
notas medias """

notas_medias = {}
notas_medias[LISTA[0]] = sum(notas[0])/len(notas[0])#tupla con tres notas
notas_medias[LISTA[1]] = sum(notas[1])/len(notas[1]) #tupla con tres notas
notas_medias[LISTA[2]] = sum(notas[2])/len(notas[2])
notas_medias[LISTA[3]] = sum(notas[3])/len(notas[3])
""""
for nombre, notas_medias in notas_medias.items():
    print(f"La nota media de {nombre} es un {notas_medias:.1f}.")
"""
"""
#ejercicio
l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
l = l2 + l1
print(l)
print(l[3:-3])

l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
l = l2 + l1
print(l)
l[2:6] = [0, 0]
print(l)

d = {'a': 8, 'b': 7, 'c': 9}
d['d'] = 5
print(d)
d[1] = 'e'
print(d)
print(5 in d)
"""

aprobadoss = {}
aprobadoss["Juan gonzales"] = notas_medias["Juan gonzales"] >= 5
aprobadoss[LISTA[1]]= notas_medias[LISTA[1]] >5
aprobadoss[LISTA[2]]= notas_medias[LISTA[2]] >5
aprobadoss[LISTA[3]]= notas_medias[LISTA[3]] >=5

print(f"en total han aprobado {sum(aprobadoss.values())} estudiantes.")

for nombre, notas_medias in notas_medias.items():
    print(f"La nota media de {nombre} es un {notas_medias:.1f}.")