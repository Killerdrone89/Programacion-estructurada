print ("\033c")
'''Ejercicio 1: Crea una lista de numeros e imprime el contenido.'''
numeros = [23,33,45,8,24,0,100]
print (numeros)

#Con for
listas=""
for i in numeros:
    listas += str(i) + " "
print ("[" + listas + "]")



#Con in range
for i in range (0,len(numeros)):
    listas+= f"{numeros[i]}, "
    print (numeros[i])
print ("[" + listas + "]")

#Con while
i = 0
while i < len(numeros):
     listas+= f"{numeros[i]}, "
     i += 1
print ("[" + listas + "]")


#Crear una lista de palabras 
palabras = ["UTD", "TERCER", "CUATRIMESTRE", "TI"]
palabra= input ("Dame la palabra a buscar: ")
encontro = palabra in palabras

if encontro== True:
    print (f"Encontre la palabra {palabra} en la lista")
else:
    print (f"No se encontro la palabra {palabra} en la lista")


encontro = False
for i in palabras:
    if i == palabra:
        encontro = True
if encontro== True:
    print (f"Encontre la palabra {palabra} en la lista")
else:
    print (f"No se encontro la palabra {palabra} en la lista")

encontro = False
indice = 0
while indice < len(palabras):
    if palabras[indice] == palabra:
         encontro = True
    
    indice += 1
if encontro== True:
    print (f"Encontre la palabra {palabra} en la lista")
else:
    print (f"No se encontro la palabra {palabra} en la lista")

encontro = False
for i in range(len(palabras)):
    if palabras[i] == palabra:
         encontro = True
       
if encontro== True:
    print (f"Encontre la palabra {palabra} en la lista")
else:
    print (f"No se encontro la palabra {palabra} en la lista")

'''Practica 2'''


#Opcion 1 con una variable logica
listas = []

true= True
while true:
    valor= input ("Dame un valor:").strip()
    listas.append(valor)
    true= input ("Ingrese True/False para continuar: ").strip()
    if true == "False":
        true = False   

print (listas)

# #Opcion 2 con un variable string 

listas=[]
true = "True"  

while true == "True":
    valor = input("Dame un valor: ").strip()
    listas.append(valor)
    true = input("Ingrese True/False para continuar: ").strip()

print(listas)

'''Ejemplo 3: Crear una lista multidimensional que permitaz almacenar el nombre y telefono de la agenda'''  

#Primer ejercicio usando range 
agenda = [
    ["David", "1234567890"],
    ["Maria", "0987654321"],
    ["Juan", "5555555555"]
]
print(agenda)

for i in agenda:
    print (i)


for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

#Codigo de manera continua 
agenda = [
    ["David", "1234567890"],
    ["Maria", "0987654321"],
    ["Juan", "5555555555"]
]
listas= ""
for r in range(0,3):
    for c in range(0,2):
        listas += f"{agenda[r][c]}, "
    listas += "\n"
print (listas)
 