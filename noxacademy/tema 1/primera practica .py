from operator import xor


a=3
print(a+5)

####################################asignación#####################################

a,b=3,"hola" #asignación de dos variables a la vez
#a vale 3 y b hola, siempre en misma proporción
print(a)
a=a+1
print(a)
###valores a variables
i=42
f=3.1416
###en los numeros enteros no debemos describir el separador de miles
# separados por puntos y no por comas
s="Hola,mundo"
print(s)
b=False
print(b)
###numeros notacion cientifica
g=6.678E-11 ##
print(g)

##cadenas de texto
s1="hola, mundo"
print(s1)
s2="Hola, \"mundo\""
print(s2)
c2='Hola, \'mundo\''
print(c2)

###algunos datos pueden convertirse de un tipo a otro:
print(int(7.5)) #7
print(str(12.1)) #"12.1"
print(int(True)) #1
print(float(7.5)) #7.5

###para ver el tipo
print(type("7.5"))
print(type(False))

#operadores
#comparar valores, retorna valor booleano
print(a==8)
print(a>=9)
print(a!=7)

#netamente booleano
#and , or, not, xor (elevado a la algo)
print(a and i) #devuelve el primer valor falso
print(a or i) #devuelve el primer valor verdadero y omite el resto
##division entera o cociente(//)
print(50//6) #8
###calcular potencias
print(5**3) #5 a la 3

#operadores relacionales
print(-2<3.5)
print(4!=4)
print("a"<"b") #en general en informatica las letras minusculas son mayores
print(a==3)
print(a==4)
print(5==5) #comparar si el valor de la variable es igual a tal

#operadores booleanos
#siguiente doc