
def elegir():

    print("Bienvendo a ligth out, Elige entre una de estas funciones")
    opciones = ("Iniciar jugada", "instrucciones", "Reanudar juego", "Salir")
    print("1_" + opciones[0])
    print("2_" + opciones[1])
    print("3_" + opciones[2])
    print("4_" + opciones[3])

    print("");

    eleccion = input("Ingresa tu eleccion:")

    if (eleccion == "1"):
        print("Preciona cualquier tecla para comenzar el juego.")  # Aca llamo a la funcion que explica el juego.
    elif(eleccion == "2"):
        print("Aca tendria que estar las instrucciones que todabia no hice.")
    elif(eleccion == "3"):
        print("No tenes ningura jugada guardada.")# Aca llamo a la funcion que busca la ultima jugada
    elif(eleccion == "4"):
        print("Regrece")
        print("Gracias por jugar")
        exit()
    else:
        print("[OPCION INCORRECTA] Tenes que elegir un numero del 1 al 4 segun lo que quieras hacer.")
        print("")
        elegir()