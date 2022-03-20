# Importamos el random para que la eleccion de la computadora sea aleatoria
import random
# Importamos la biblioteca de JSON para trabajar con un archivo .json y tener persistencia
# de datos.
import json

## Declaramos funcion calculoPorcentaje y diccionario de analiticas fuera del While
# para que no se actualice a cada vuelta del bucle

def calculoPorcentaje(vic, total):
    porcentaje = (vic * 100) / total
    analiticas["porcentaje"] = porcentaje
    return porcentaje

## Diccionario donde se almacenan estadisticas
# analiticas = {
#         "partidas": 0,
#         "victorias": 0,
#         "derrotas": 0,
#         "empates": 0,
#         "porcentaje": 0
#     }
## Lo dejo comentado porque no necesito declararlo, ya que lo extraigo
## directamente del archivo json


## open() trae el archivo analiticas en modo lectura.
data = open('analiticas.json', 'r')

## Los diccionarios de python son un objeto para JSON, por lo que con data.read() leemos el archivo
## y esa informacion, dentro del json.loads() la deserializamos a formato diccionario.
analiticas = json.loads(data.read())

while True:

    ## Menu

    ## Computadora elige numero aleatorio desde el 0 hasta (sin incluir) el 5
    aleatorio = random.randrange(0, 5)

    print("\n")
    print("0) Piedra")
    print("1) Papel")
    print("2 )Tijera")
    print("3) Lagarto")
    print("4) Spock")
    print("5) Ver estadisticas")
    print("6) Salir del Programa")
    
    
    
    try:
        opcion = int(input("Que eliges: ")) ## Aclaramos que el input debe ser de tipo int.
        print("\n#####################\n")
    except: ##Si el user ingresa una letra o signo, el try/except hace que no rompa el codigo, y en su lugar
        print("\n#####################") ## imprima que el valor es invalido. 
        print("\nValor invalido! Se debe ingresar un numero del 1 al 5")
        continue ## Con el continue reiniciamos el ciclo While.

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
            print("Winrate:", round(calculoPorcentaje(analiticas["victorias"], analiticas["partidas"])),"%")
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
    
    ## Abrimos el archivo 'analiticas.json' en formato de escritura ('w'), bajo la variable json_file. Luego, con json.dump(analiticas, json_file) 
    ## insertamos el diccionario analiticas en el archivo que se almacena como referencia en la variable json_file. De esta forma, cada vez que 
    ## finalicemos una ronda, antes de volver a jugar nos aseguramos de reescribir los datos en el json
    with open('analiticas.json', 'w') as json_file:
        json.dump(analiticas, json_file)

    # Opcion Reinicio
    again = input("Jugamos de nuevo? Si/No: ")
    if 'si' in again.lower():
        continue
    elif 'no' in again.lower():
        print("Nos vemos!")
        break
    else:
        print("Valor Invalido")