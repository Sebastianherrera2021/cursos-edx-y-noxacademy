### diccionarios
#tiene claves que son unicas y no estan repetidas

d= {} #diccionario vacío 
d = {"c1":1, 3: "gola","b2":True,"a_":1.4}
#no estan ordenados, no existe un primer lugar
print(d)

##########################inserción de elementos#####################################
de={"c1":1,3:"hola","b2":True,"a_":1.4}
de["d7"]="mundo" #d7=nombre, agrega esa nueva mediante asignación
print(de)


##para borrar elementos
del de["c1"] ## se coloca la clave
print(de)

###################################### obtener un elemento de una lista:#####################
de["a_"]
print(de[3]) #no es por posición sino el nombre de la clave
print(len(de))
print("b2" in de)
print(de.keys()) ### me da el nombre de de las llaves
print(de.values()) ### los valores de las llaves

################################################# TUPLAS #####################################
#ES UNA COLECCIÓN SIMILAR A UNA LISTA CON ALGUNAS DIFERENCIAS
t=(1,2,3)
### son inmutables, no se puede añadir, borrar, ni modificar
#t[1]=0 #error
#del t[2] #error
#t.append(4) #error

a,b,c=t #asignar a esa tupla varias variables
print(t) #a=1, b=3, c=2


##########################CONJUNTOS, no pueden haber valores repetidos, y no tienen orden ##################
#tienen ventaja de rendimiento
s={1,2,3}
s.add(4)
print(s)
s.add(1) #no pueden haber repetidos
print(s)

## COMENTARIOS
a=a+1 #incrementa la variable a en una unidad
"""
ESTO ES UN COMENTARIO
"""
