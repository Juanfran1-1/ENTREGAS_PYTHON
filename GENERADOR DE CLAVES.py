import random 
import string

#caracteres_contraseña = ["a" , "b" , "c" , "-" , "1" , "2" , "3"]
caracteres_contraseña = string.ascii_letters + string.digits + string.punctuation
contraseña=""
cantidad= int(input("INGRESE CANTIDAD DE CARACTERES PARA CONTRASEÑA: "))
print("\n creando contraseña..." )
for caracter in range(cantidad):
    contraseña += random.choice(caracteres_contraseña)
print("contraseña generada: ",contraseña)    
