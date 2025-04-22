lista = (1,6,7,8,3,5,7,10,45,67,32,48)
pares = []
impares = []
for num in lista:
    if num % 2 == 0:
        pares += [num]
    else:
        impares += [num]
print("Lista pares: ", pares)
print("Lista impares: ",impares)        
        