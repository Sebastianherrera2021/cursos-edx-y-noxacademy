#condicionales y gestion de errores
##if<condicion>:
#ejemplo:
from cmath import exp
from logging import exception


a=15
if a<15:
    a=a+1 #incrementa el valor
    print("hola")
print("Adios")


#if True: siempre se cumple
#if False: nunca se cumple
#if a>b: si el valor de a es menor que el de b
#if a==1 and b<c: si se cumplen ambas condiciones simultaneamente
#if a<=b or b<=c: si se cumple una de las dos condiciones

lag=["hola", "adios"]
if "hola" in lag:
    print("ss")
print("adios")


#if-else
if a<15:
    print("caso 1") #se imprime si a<15
else:
    print("caso 2") #se imprime en otro caso, es decir, si a>=15
print("Adios") #se imprime siempre (está fuera del bloque)

####
# if solo se ejecura si se cumple la condición 1
#elif solo se ejecuta si se cumple la condicion 2 y no se cumple la condicion 1
#elif  solo se ejecuta si se cumple la condicion n y no se cumple ninguna de las anteriores
#else solo se ejecuta si no se cumple ninguna condicion anterior  

nota=7
if nota<5:
    print("suspenso")
elif nota <7:
    print("aprobado")
elif nota<9:
    print("notable")
elif nota<10:
    print("sobresaliente")
else:
    print("matricula honor")

a=5
b=3
if a<3: 
    print("caso 1")
else:
    if b<5:
        print("caso 2")
    else: 
        print("caso 3")

a=6
a = 3
if a<3:
    print("caso 1")
elif b<5:
    print("el caso 2")
else: 
    print("caso 3")

### tipos de errores
#value error= error de valor no puedo convertir una cadena de texto a valor
#zerodivisionerror= no se puede dividir entre 0
# nameError: name "a" is not defined: variable no definida

#para capturar errrores
#usar try-except
#try:
    #codigo que se intenta ejecutar pero pueden ocurrir errores
#except: 
    #codigo que se ejecuta si ocurre un error en el codigo anterior 

a,b=7,0
try:
    c=a/b #se produce un error
    print(c) #no se ejecuta
except:
    print("error!") #esta si se ejecuta

s=7.5
#s="hola"
#s=0
try:
    b=float(s)
    c=a/b
    print(c)
except ValueError:
    print("s no es un numero")
except ZeroDivisionError:
    print("s vale 0, no se puede dividir")
except:
    print("ha ocurrido un error desconocido")

## EXPRESIÓN PASS -NO EJECUTA NADA

#try:
    #codigo 
#except:
#    pass
#el codigo sigue funcionando

#try-except-else
#try:
#except:
#else:
#ejecutar un codigo en caso de que no se haya producido ningun error
print("hola")
a=68
b=1
try:
    c=a/b
    print(c)
except:
    print("ha ocurrido un error")
else:
    print("todo marcha bien")
#se ejecuta el try con el else

################# try-except- finally####
try:
    c=a/b
    print(c)
except:
    print("ha ocurrido un error")
finally:
    print("adios") ##siempre se ejecuta sin importar si hay o no error

########################## EXCEPCIONES #########################
a=2
try:
    c=a/b
    print(c)
except exception as e:
    print(e)
### la excepcion la estoy guardando en una variable y luego puedo hacer cosas con e


######################## BLOQUES DE CODIGOOOOOOOOOOOOOOO """"""""""""""""""""""""
print("hola")
a=2
if a<5:
    a=a+1
    print("que tal")
print("adios")
