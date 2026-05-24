#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
    nombre=input("Nombre: ").upper().strip()
    apellidos=input("Apellidos: ").upper().strip()
    print(f"El nombre del alumno es: {nombre} {apellidos}")

#3.- Funcion que recibe parametros y no regresa valor
def funcion3(nom,ape):
    nombre=nom
    apellidos=ape
    print(f"El nombre del alumno es: {nombre} {apellidos}")

#2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    nombre=input("Nombre: ").upper().strip()
    apellidos=input("Apellidos: ").upper().strip()
    return(nombre,apellidos)

#4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
    nombre=nom
    apellidos=ape
    return(nombre,apellidos)

#Invocar las funciones

#Funcion 1
funcion1 ()

#Funcion 3
nombre= input("Nombre: ").upper().strip()
apellidos= input("Apellidos: ").upper().strip()
funcion3 (nombre,apellidos)

#Funcion 2
funcion2 ()
nombre,apellidos=funcion2()
print(f"El nombre del alumno es: {nombre} {apellidos}")

#Funcion 4
nom= input("Nombre: ").upper().strip()
ape= input("Apellidos: ").upper().strip()
nombre,apellidos=funcion4(nombre, apellidos)
print(f"El nombre del alumno es: {nombre} {apellidos}")