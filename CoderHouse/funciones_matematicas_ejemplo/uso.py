from funciones_matematicas import sumar, restar
from estadistica import combinar
from collections import namedtuple, Counter
from math import sqrt, ceil, floor, acos, acosh,tan,tanh
import random
from datetime import datetime


resultado_suma = sumar(20, 30)
print(resultado_suma)

resultado_resta = restar(100, 50)
print(resultado_resta)

Fish = namedtuple('Fish', ['name', 'species', 'tank'])
# Esto crea una clase Fish con lo atributos publicos nombre, especie y tanque
pez_1 = Fish('Sammy', 'Tiburon', 'Tanque grande')

lista = [1,2,3,1,2,2,1,1,3,4,2,1]
Counter(lista)

# Random
lista_1 = [1,2,'coder',-1,'nico',3]
print(random.choice(lista_1))

string = "Esta es una cadena"
print(random.choice(string))

num = random.randit(0,50)
print(num)

dt = datetime.now()
print(dt, dt.year, dt.month, dt.minute, dt.second)
