print("Controles de comando")
print("A. Mover a la derecha")
print("B. Mover a la izquierda")
print("C. Mover hacia el frente")
print("D. Mover hacia atrás")
print("E. Apagar")

while True:
    comando = input("Ingrese un comando: ")

    match comando:
        case "A" | "a":
            print("El robot se desplazó a la derecha")
        case "B" | "b":
            print("El robot se desplazó a la izquierda")
        case "C" | "c":
            print("El robot se  desplazó hacia adelante")
        case "D" | "d":
            print("El robot se desplazó hacia atrás")
        case "E" | "e":
            print("El robot se ha apagado")
            break
        case _:
            print("Comando no reconocido. Intente de nuevo.")