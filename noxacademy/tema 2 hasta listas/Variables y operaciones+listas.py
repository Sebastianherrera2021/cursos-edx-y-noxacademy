# Operadores booleanos
#and, or, not and xor
from operator import xor
from re import L
from tkinter import TRUE


print(True and True) #devuelve true si ambos valores son True
False or False #Devuelve true si al menos uno de los valores es true
not True

###operadores con cadena de text
a="Hola "
b="mundo"
print(a+b)

##contar
print(len("hola mundo"))
gh="hola mundo"
print(gh.upper()) ##mayuscula
hg="hola MUndo"
print(hg.lower())  ##minuscula


## Estructuras de datos
##permite almacenar varios valores del mismo o diferente tipo
# listas o diccionarios
#listas: almacenan valores uno tras otro
# diccionarios: almacenan valores asociados a una clave
#lista [] primer elemento indexado con el valor cero
#diccionario {} el indice no tiene porque ser numerico sino cualquier valor "clave"
#lista: colección de elementos ordenada

l=[] #lista vacía 
opo=[1.54, "hola","mundo",3]
################################## borrar por posicion#############################################
del opo[0] #borra el elemento cero
print(opo)
opo=[154, "hola","mundo",3]
print(opo) 
########################para borrar un elemento de una lista#######################################
sec=[18,59,5]
sec.remove(18) ## borrar
print(sec)


#########################################para añadir elementos a la lista###########################
lol=[1.54,"hola","mundo",3]
lol.append("adios") ##lo agrega al final
print(lol)
lol.insert(2,"que tal") #en una posicion 
print(lol)

############################## acceso a elementos mediante un indice###################################
pai=[5.2, "kk",598]
pai[0]
pai[2]
print(pai[-1]) #ultimo elemento de la lista y no el -0
pai[-2] #penultimo

################################## otra forma "rangos"#################################################
print(pai[:2]) #de 0 a 2, dos numeros
print(pai[1:]) # de 1 hasta el final
print(pai[:]) #todos los elementos

##tambien se puede con cadenas de texto
print("hola mundo"[1:-2]) #recorro la lista desde el 1 y termino en el -2

## len para conocer la longitud de una lista
andreiña=[4,8,4,8,4,5,6] 
print(len(andreiña))
ff=[5,"ñ"]
print(andreiña+ff) #las concatena o une

##operador in "relacional"
print(3 in ff)
print(5 in ff)
## suma
ter=[1,11,2]
print(sum(ter))
################################## invertir orden de los elementos######################
print(reversed(ter))
## sorted - reordenar
print(sorted(ter)) #de menor a mayor

##actualización de elementos "por asignación"
gar=["hola",1,45,5]
gar2=gar[2]="que tal" #reemplazar valores de la lista
print(gar)

## actualizacion de una sublista 
gar[1:3]=["que tal",2] ##reemplaza valores 2 y 3 de los 4
print(gar)


