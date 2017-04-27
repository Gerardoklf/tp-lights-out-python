print("Bienvendo a ligth out, Elige entre una de estas funciones")
elegir = ("Iniciar jugada", "instrucciones", "Reanudar juego", "Salir")
print("1_" + elegir[0])
print("2_" + elegir[1])
print("3_" + elegir[2])
print("4_" + elegir[3])

def elegir():
    eleccion = input()
    print("Ingresa tu eleccion:", eleccion)  # Aca llamo a la funcion que iniciael juego")
    print("Seleccion: ")
    if (eleccion == "1"):
        print("Preciona cualquier tecla para comenzar el juego.")  # Aca llamo a la funcion que explica el juego.
    elif(eleccion == "2"):
        print("Aca tendria que estar las instrucciones que todabia no hice.")
        (eleccion == "3")
        print("No tenes ningura jugada guardada.")# Aca llamo a la funcion que busca la ultima jugada
                        # del usuario.
        (eleccion == 4)       # Salgo del juego.
        print("Regrece")
    else:
        print("Tenes que elegir un numero del u al 4 segun lo que")
        print("quieras hacer.")
print(elegir())