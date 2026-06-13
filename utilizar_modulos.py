# 1er utilizar los modulos 
import modulos

modulos.BorrarPantalla()
modulos.funcion1()

nom="Daniel" 
ape="Carreon"

name,lastname=modulos.funcion4(nom,ape)
print(f"Nombre: {name}\n Apellidos: {lastname}")

#2da formar de utilizar modulos

#from modulos import BorrarPantalla,funcion1,funcion4
from modulos import *

BorrarPantalla()
funcion1()

nom="Daniel" 
ape="Carreon"

name,lastname=funcion4(nom,ape)
print(f"Nombre: {name}\n Apellidos: {lastname}")