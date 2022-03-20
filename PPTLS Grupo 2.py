import random

## Declaramos funcion calculoPorcentaje y diccionario de analiticas fuera del While
# para que no se actualice a cada vuelta del bucle
def calculoPorcentaje(vic, total):
    porcentaje = (vic * 100) / total
    return porcentaje

## Diccionario donde se almacenan estadisticas
analiticas = {
        "partidas": 0,
        "victorias": 0,
        "derrotas": 0,
        "empates": 0,
        "porcentaje": calculoPorcentaje
    }

while True:

    ## Menu

    aleatorio = random.randrange(0, 5)
    elijePc = ""
    print("\n")
    print("0) Piedra")
    print("1) Papel")
    print("2 )Tijera")
    print("3) Lagarto")
    print("4) Spock")
    print("5) Ver estadisticas")
    print("6) Salir del Programa")
    try:
        opcion = int(input("Que eliges: "))
        print("\n#####################\n")
    except:
        print("\n#####################")
        print("\nValor invalido! Se debe ingresar un numero del 1 al 5")
        continue

    ## Creamos los elementos
    
    elementos = [{
        "nombre": "Piedra",
        "id": 0,
        "ganaContra": [2, 3],
        "pierdeContra": [1, 4],
    },
        {
            "nombre": "Papel",
            "id": 1,
            "ganaContra": [0, 4],
            "pierdeContra": [2, 3],
    },
        {
            "nombre": "Tijera",
            "id": 2,
            "ganaContra": [1, 3],
            "pierdeContra": [0, 4],
    },
        {
            "nombre": "Lagarto",
            "id": 3,
            "ganaContra": [1, 4],
            "pierdeContra": [0, 2],
    },
        {
            "nombre": "Spock",
            "id": 4,
            "ganaContra": [0, 2],
            "pierdeContra": [1, 3],
    }]

    ## Captamos datos del diccionario "analiticas"

    partidas = analiticas.get("partidas")
    victorias = analiticas.get("victorias")
    derrotas = analiticas.get("derrotas")
    empates = analiticas.get("empates")

    ## Eleccion del menu

    if opcion in range(0, 5):
        eligeUsuario = elementos[opcion]
    elif opcion == 5:
        print("Cantidad de partidas:", analiticas["partidas"])
        print("Cantidad de victorias:", analiticas["victorias"])
        print("Cantidad de derrotas:", analiticas["derrotas"])
        try:
            print("Winrate:", round(analiticas["porcentaje"](analiticas["victorias"], analiticas["partidas"])),"%")
        except:
            print("Winrate: 0%. Error en division por cero. Una sola partida te pido que ganes....")
        continue
    elif opcion == 6:
        print("nos vemos!")
        break
    else:
        print("Por favor, ingrese un valor valido")
        continue

    print("Tu eliges: ", eligeUsuario["nombre"])

    ## Definimos eleccion de la PC
    
    eligePc = elementos[aleatorio]

    print("PC eligio: ", eligePc["nombre"])
    print("\n..............\n")
 
    ## Comparaciones
    
    i = 0

    for num in eligeUsuario["ganaContra"]:

        if eligeUsuario["id"] != eligePc["id"]:
            if num == eligePc["id"]:
                print("Ganaste!!! ", eligeUsuario["nombre"], "le gana a", eligePc["nombre"], "\n")
                
                ## Actualizamos estadisticas de victoria
                partidas += 1
                analiticas["partidas"] = partidas
                victorias += 1
                analiticas["victorias"] = victorias
                break
            elif eligeUsuario["id"] == eligePc["ganaContra"][i]:
                print("Perdiste :/ ", eligeUsuario["nombre"], "pierde contra", eligePc["nombre"], "\n")
                
                ## Actualizamos estadisticas de derrota
                partidas += 1
                analiticas["partidas"] = partidas
                derrotas += 1
                analiticas["derrotas"] = derrotas
                break
            else:
                i += 1
        else:
            ## Actualizamos estadisticas de empate
            partidas += 1
            analiticas["partidas"] = partidas
            empates += 1
            analiticas["empates"] = empates
            print("Empate!\n")
            break

    # Opcion Reinicio
    again = input("Jugamos de nuevo? Si/No: ")
    if 'si' in again.lower():
        continue
    elif 'no' in again.lower():
        print("Nos vemos!")
        break
    else:
        print("Valor Invalido")