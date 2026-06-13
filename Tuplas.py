'''
   LAS TUPLAS SE UTILIZAN PARA ALMACENAR VARIOS ELEMENTOS EN UNA SOLA VARIABLE.
   una sola tupla es una coleccion ordenada e inmutable.
   las tuplas se escriben entre parentesis
'''  
print("\033c")

paises1 =("Mexico", "Canada", "EUA")
varios =("hola", 1, 2.5, True)



print (paises1)
print (varios)

for i in paises1:
    print(i)

for i in varios:
    print(i)

print (f"El pais que inaugura la copa del mundo es: {paises1[0]}")


paises1 = ("Mexico", "Canada", "EUA")
paises3 = ("Mexico", "Canada", "EUA")

print (paises1)
print (paises3)

for i in paises1:
    print(i)

for i in range (0,len(paises1)):
    print (paises1[i])

print (f"El pais que inaugura la copa del mundo es: {paises1[0]}")


'''_____________________________Con while_________________________________'''

paises1 = ("Mexico", "Canada", "EUA")
paises3 = ("Mexico", "Canada", "EUA")

i=0
while i<3:
    print (paises1[i])
    i += 1
    print (f"El pais que inaugura la copa del mundo es: {paises1[0]}")
  
edades= (18, 20, 22, 24, 26)
print (edades)
cuantos= edades.count(22)
print(f"La edad 22 aparece {cuantos} veces en la tupla.")

numeros = int (input("Ingrese el numero a buscar : ")).strip()
posiciones= edades.index(numeros)
print(f"El numero {numeros} se encuentra en la posicion {posiciones}. ")

'''_________________________________________________________________________'''

edades= (18, 20, 22, 24, 26)
print (edades)

numeros = int (input("Ingrese el numero a buscar : ").strip())
posiciones =[]
for i in range (0, len(edades)):
    posiciones.append(posiciones)

for i in range (0, len(posiciones)):
    print (f"El numero {numeros} se encuentra en la posicion {posiciones[i]}. ")