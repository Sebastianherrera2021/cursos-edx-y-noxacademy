

# Capital inicial (en €)
C = 5000

# Tipo de interés (en %, sobre 1)
i = 0.015

# Periodo (en años)
n = 5

# Cálculo del capital final (en €)
M = C * (1 + i) ** n

# Comisiones mensuales (en €)
f = 5

# Gastos totales atribuibles a comisiones durante todo el periodo (en €)
G = f * 12 * n

# Saldo final de la cuenta (en €)
S = M - G

####### ESCRIBE EL CÓDIGO AQUÍ (4 líneas aprox.)
if C<S:
  print("tiene beneficios")
elif C==S:
  print("no se tienen beneficios ni perdidas")
else:
  print("no se obtuvieron beneficios")
"""
####### 2 EJE!pip install geocoder --quiet
!pip install timezonefinder[numba] --quiet
from datetime import datetime
import geocoder
import json
import pytz
import requests
from timezonefinder import TimezoneFinderRCICIOOOOO ################

####### ESCRIBE EL CÓDIGO AQUÍ (1 línea)
location="madrid,españa"
#######

# Obtiene las coordenadas de la ubicación indicada.
latlng = geocoder.arcgis(location).latlng
if latlng is None:
  raise Exception("La ubicación indicada no se ha encontrado.")

# Obtiene la zona horaria de la ubicación indicada.
tz = TimezoneFinder().timezone_at(lng=latlng[1], lat=latlng[0])

# Obtiene la hora actual en la ubicación indicada (ajustando la zona horaria).
time = datetime.now(pytz.timezone(tz))
hour = time.hour

# Obtiene y extrae la información meteorológica.
sites = requests.get(f"https://www.metaweather.com/api/location/search/?lattlong={latlng[0]},{latlng[1]}").json()
if not sites:
  raise Exception("No se encuentra información meteorológica para a ubicación indicada.")
meteo = requests.get(f"https://www.metaweather.com/api/location/{sites[0]['woeid']}/{time.year}/{time.month}/{time.day}/").json()[0]
status = meteo['weather_state_name'].lower()
min_temp = meteo['min_temp']
max_temp = meteo['max_temp']
"""
##CODIGO CON LA VARIABLE HOUR
hour=6
if hour>=5 and hour<12:
  print("buenos dias")
elif hour>=12 and hour<19:
  print("buenas tardes")
elif hour>=19 and hour<5:
  print("buenas noches")

### estado metereologico
status="snow"
if status=="snow":
  print("el cielo esta nevado")
elif status=="sleet":
  print("el cielo está aguanieve")
else:
  print("lloviznas")

#temperaturas minimas y maximas
min_temp=-5
max_temp=19
if min_temp<0:
  print("va a hacer frio")
if max_temp>35:
  print("va a hacer calor")


##otro ejercicio
from datetime import date, timedelta
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", 
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

####### MODIFICA LOS VALORES A TU ANTOJO
dia = 35
mes = "abril"
#######
"""
today = date.today()
birthday = date(today.year, meses.index(mes) + 1, dia)
if birthday < today:
  birthday = birthday.replace(year = birthday.year + 1)
dias = (birthday - today).days
"""
####### ESCRIBE EL CÓDIGO AQUÍ (10 líneas, incluyendo las anteriores)
try:
  today = date.today()
  birthday = date(today.year, meses.index(mes) + 1, dia)
  if birthday < today:
    birthday = birthday.replace(year = birthday.year + 1)
  dias = (birthday - today).days
  print(f"Quedan {dias} días para tu cumpleaños. ¡Ve preparando la fiesta!")
except:
  print("Error con la fecha, revisala")
#######

#parcial
print("8")
a = 10
if a > 2:
    print("caso 1")
elif a > 5:
    print("caso 2")
else:
    print("caso 3")
print("7")
l = [1, 2, 3]
if len(l*2) > 5:
    print("caso 1")
else:
    print("caso 2")

print("6")
l = list(range(5, 0, -1))
if l[1] / l[-1] > 0:
    print("caso 1")
else:
    print("caso 2")

print("5")
l1 = [1, 3, 4, 5]
l2 = [2, 1, 3, 3]
if l1 < l2:
    print("caso 1")
elif l2 < l1:
    print("caso 2")
else:
    print("fin")
print("4")
l = [1, 2, 3]
if len(l*2) > 5:
    print("caso 1")
else:
    print("caso 2")


"""
a, b = b, a
if a >= b and b >= a:
    print("hola")
"""
print("3.5")
l = [1, 3, 5, 7, 11]
print(3 in l[2:-1])
print("2")
l1 = [1, 3, 4, 5]
l2 = [2, 1, 3, 3]
if l1 < l2:
    print("caso 1")
elif l2 < l1:
    print("caso 2")
else:
    print("fin")
print("1")
l = [1, 2, 3]
if len(l*2) > 5:
    print("caso 1")
else:
    print("caso 2")

a, b = b, a
if a >= b and b >= a:
    print("hola")