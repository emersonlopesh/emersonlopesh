# Importamos la librería random para elegir una opción aleatoria
import random

# Definimos las opciones disponibles
opciones = ["piedra", "papel", "tijeras"]

# Pedimos al usuario que ingrese su nombre
jugador1 = input("Jugador 1, ¿cuál es tu nombre? ")
jugador2 = input("Jugador 2, ¿cuál es tu nombre? ")

# Creamos una función que compare las opciones y determine quién ganó
def comparar(opcion1, opcion2):
    if opcion1 == opcion2:
        return "Empate"
    elif opcion1 == "piedra":
        if opcion2 == "tijeras":
            return jugador1 + " gana"
        else:
            return jugador2 + " gana"
    elif opcion1 == "papel":
        if opcion2 == "piedra":
            return jugador1 + " gana"
        else:
            return jugador2 + " gana"
    elif opcion1 == "tijeras":
        if opcion2 == "papel":
            return jugador1 + " gana"
        else:
            return jugador2 + " gana"

# Comenzamos el juego
while True:
    # Pedimos al jugador 1 que elija una opción
    jugador1_opcion = input(jugador1 + ", ¿piedra, papel o tijeras? ").lower()
    while jugador1_opcion not in opciones:
        jugador1_opcion = input("Opción no válida. Elige piedra, papel o tijeras. ").lower()

    # Pedimos al jugador 2 que elija una opción
    jugador2_opcion = input(jugador2 + ", ¿piedra, papel o tijeras? ").lower()
    while jugador2_opcion not in opciones:
        jugador2_opcion = input("Opción no válida. Elige piedra, papel o tijeras. ").lower()

    # Mostramos quién ganó
    print(comparar(jugador1_opcion, jugador2_opcion))

    # Preguntamos si quieren seguir jugando
    jugar_de_nuevo = input("¿Quieren jugar de nuevo? (s/n) ").lower()
    if jugar_de_nuevo != "s":
        break

print("¡Gracias por jugar!")
