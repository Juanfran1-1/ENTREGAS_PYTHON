import random
import sys

# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]


#SELECCIONA TRES PREGUNTAS ALEATORIAS SIN REPETICIONES (INCISO C)
preguntas= random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

#INICIA EL PUNTAJE EN 0
score = 0


# El usuario deberá contestar 3 preguntas (INCISO D)
for pregunta, opciones, correcta in preguntas:
    
# Se muestra la pregunta y las respuestas posibles
    print(pregunta)
    for i, answer in enumerate(opciones):
        print(f"{i + 1}. {answer}")
        
# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        
        #se pide la respuesta del usuario y se guarda en user_answer
        user_answer = input("Respuesta: ") 
        
        # (INCISO A) Se verifica que la respuesta sea un número entero si no lo es se termina el juego
        if not user_answer.isdigit():
            print("RESPUESTA INVALIDA. FIN DEL JUEGO")
            sys.exit(1)
        else:
            #se resta 1 a la respuesta del usuario para que coincida con el indice de la respuesta correcta
            user_answer = int(user_answer) - 1
            #se verifica que la respuesta sea un numero valido si no se termina el juego
            if user_answer < 0 or user_answer >= len(opciones):
                print("RESPUESTA INVALIDA. FIN DEL JUEGO")
                sys.exit(1)
            
        # Se verifica si la respuesta es correcta, si lo es suma 1 al score, si no lo es resta 0.5 al score
        if user_answer == correcta:
            print("¡Correcto!\nGANASTE 1 PUNTO.") 
            score += 1
            break
        else:
            print("Incorrecto.\nPERDISTE 0.5 PUNTOS.")
            score -= 0.5
            
            #verifica si se llego al ultimo intento para mostrar la respuesta correcta si no muestra un mensaje para volver a intentar
            if intento == 1:
                print(f"La respuesta correcta es: {opciones[correcta]}\n")
            else: 
                print("Intenta de nuevo.\n")
                
# si no se llego a la ultima pregunta se imprime SIGUIENTE PREGUNTA
    if len(preguntas) != 3:
        print("°SIGUIENTE PREGUNTA:")
        
#MUESTRA EL PUNTAJE FINAL  (INCISO B)      
print(f"Tu puntaje final es: {score}")

