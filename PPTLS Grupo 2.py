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

## Bucle while True, para que al finalizar cada ronda, vuelva a ejecutarse de cero. Para finalizar programa o bucle, tenemos se usa 'break'
while True:

    ## Menu
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
        print("\n#####################") ## imprima una advertencia. 
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
    winrate = analiticas.get("porcentaje")

    ## Eleccion del menu

    if opcion in range(0, 5):
        eligeUsuario = elementos[opcion] # Relacion directa entre el indice del elemento en la lista (array) con valor ingresado en input
    elif opcion == 5:
        ## Menu analiticas
        print("Partidas totales:", analiticas["partidas"])
        print("Victorias:", analiticas["victorias"])
        print("Derrotas:", analiticas["derrotas"])
        print("Empates:", analiticas["empates"])
        try: ## Esto esta en caso de el programa no caiga si el usuario no tiene victorias, ya que intenta dividir por 0. 
            print("Winrate:", winrate ,"%")
        except:
            print("Winrate: 0%. Error en division por cero. Una sola te pido que ganes....")
        continue
    elif opcion == 6:
        print("nos vemos!")
        break ## Rompe el bucle While y finaliza el programa
    else:
        print("Por favor, ingrese un valor valido")
        continue

    print("Tu eliges: ", eligeUsuario["nombre"])

    ## Eleccion de la PC
    ## Computadora elige numero aleatorio desde el 0 hasta (sin incluir) el 5
    aleatorio = random.randrange(0, 5)
    eligePc = elementos[aleatorio]

    print("PC eligio: ", eligePc["nombre"])
    print("\n..............\n")
 
    ## Comparaciones
    
    i = 0 ## Variable para iterar sobre arrays a cada vuelta de bucle for

    ## Logica: 
    ## Cada elemento tiene un id y dos listas de id's de otros elementos; Una de elementos derrotables y otra de elementos que lo derrotan.
    for num in eligeUsuario["ganaContra"]: ## Iteramos sobre dicha lista de posibles elementos derrotables del elemento elegido por el usuario.

        if eligeUsuario["id"] != eligePc["id"]: ## Descarta de inmediato si hay situacion de empate o no
            if num == eligePc["id"]: ## Si el elemento que recorre en ese momento encuentra el id del elemento rival, se declara victoria para usuario.
                print("Ganaste!!! ", eligeUsuario["nombre"], "le gana a", eligePc["nombre"], "\n")
                ## Actualizamos estadisticas de victoria
                partidas += 1
                analiticas["partidas"] = partidas
                victorias += 1
                analiticas["victorias"] = victorias
                break
            elif eligeUsuario["id"] == eligePc["ganaContra"][i]: ## En caso de no encontrar victoria, checkea si el id de nuestro elemento se encuentra
                                                                 ## en la lista de id's derrotables por el elemento rival.    
                print("Perdiste :/ ", eligeUsuario["nombre"], "pierde contra", eligePc["nombre"], "\n") ## En dicho caso, derrota para usuario.
                
                ## Actualizamos estadisticas de derrota
                partidas += 1
                analiticas["partidas"] = partidas
                derrotas += 1
                analiticas["derrotas"] = derrotas
                break
            else: 
                i += 1 ## Si no encuentra nada, incrementa variable 'i', para que en siguiente vuelta de bucle, compare con el proximo id en lista de
                       ## elementos derrotables por el rival.
        else:
            ## Actualizamos estadisticas de empate
            partidas += 1
            analiticas["partidas"] = partidas
            empates += 1
            analiticas["empates"] = empates
            print("Empate!\n")
            break

    # Al finalizar el bucle, calculo el winrate y lo actualizo
    winrate = round(calculoPorcentaje(analiticas["victorias"], analiticas["partidas"]))
    analiticas["porcentaje"] = winrate

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