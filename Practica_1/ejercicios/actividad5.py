cant= int(input("Ingrese cantidad de numeros de la lista: "))

lista = [int(input(f"Ingrese numero {i+1}: "))for i in range(cant)]
for num in lista:
    if num < 0:
        print("NUMERO NEGATIVO")
        break
    print(num)