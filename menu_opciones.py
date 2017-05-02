print("Bienvendo a ligth out, Elige entre una de estas funciones")
elegir = ("Iniciar jugada", "instrucciones", "Reanudar juego", "Salir")
print("1_" + elegir[0])
print("2_" + elegir[1])
print("3_" + elegir[2])
print("4_" + elegir[3])

def elegir():
    eleccion = input()
    print("Ingresa tu eleccion:", eleccion)  # Aca llamo a la funcion que iniciael juego")

    if (eleccion == "1"):
        print("Preciona cualquier tecla para comenzar el juego.")  # Aca llamo a la funcion que explica el juego.
    if(eleccion == "2"):
        print("Aca tendria que estar las instrucciones que todabia no hice.")
    if(eleccion == "3"):
        print("No tenes ningura jugada guardada.")# Aca llamo a la funcion que busca la ultima jugada
                        # del usuario.
    elif(eleccion == "4"):
        print("Regrece")
        print("Gracias por jugar")
    else:
        print("Tenes que elegir un numero del 1 al 4 segun lo que")
        print("quieras hacer.")
print(elegir())