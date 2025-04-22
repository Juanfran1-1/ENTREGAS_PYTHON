lista= []
cantidad= int(input("Ingrese cantidad de numeros en la lista: "))
for num in range(cantidad):
    ingresado=int(input("Ingrese numero: "))
    lista += [ingresado]
concatenado= ""
for num in lista:
    if num % 3 != 0:
        concatenado += str(num) + "-"                    
print(concatenado)
