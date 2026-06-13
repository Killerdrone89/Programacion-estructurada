from paquete1 import modulos,modulo_paquete

modulos.BorrarPantalla()
modulos.funcion1()

nom="Daniel" 
ape="Carreon"

name,lastname=modulos.funcion4(nom,ape)
men=modulo_paquete.funcion4(nom,ape)

print(f"Nombre: {name}\nApellidos: {lastname}")
print(men)