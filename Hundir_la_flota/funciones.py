import numpy as np
import random
import os
import time
from PIL import Image


from variable import*

import os
from PIL import Image
import time

import os
from PIL import Image
import time

def abrir_imagen():
    """
    Esta función permite abrir una imagen en una ventana emergente
    con la cual presentamos el juego
    """
    
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    ruta_img = os.path.join(directorio_actual, "img", "hlf.jpg")

    im = Image.open(ruta_img)
    im.show()
    time.sleep(3)


            
def crear_flota(barco,tablero,coordenadas):
    """
    Esta función consisite en crear una flota de barcos para cada jugador, 
    la cual, se irá reducuiendo a medida que se vayan hundiendo los barcos
    """
    
    if tablero is tablero_2:
        
        flota_usuario[barco]= (coordenadas)
        
    else:
        flota_maquina[barco]= (coordenadas)

def colocar_barco(barco,eslora, tablero):

    """
    esta función coloca los barcos según las coordenadas adqueridas en la función, crear barco
    además, para tener mas claridad a la hora de representar a los barcos
    según la eslora de cada barco, este será representadocon el numero de eslora tantas veces com sea su tamaño
    """
    
    if eslora == 1:
        for casilla in barco:
            tablero[casilla] = 1
    elif eslora == 2:
        for casilla in barco:
            tablero[casilla] = 2
    elif eslora == 3:
        for casilla in barco:
            tablero[casilla] = 3
    elif eslora == 4:
        for casilla in barco:
            tablero[casilla] = 4
    
    
    return tablero


def crear_barco_aleatorio(lista_barcos, tablero):

    """
    Esta función de pende de 2 argumentos:
    -lista_barcos
    -tablero, que habrá 2 y en los cuales representará los barcos

    Esta función permite crear el barco según la orientación aleatoria, dada a continuación.
    La eslora la determinará según el nombre del barco, el cual, es nombrado a su vez, según la eslora.
    -1º, mediante un bucle for, recorremos los nombres de barcos de una lista para ir creandolos.
    -2º, mediante un bucle while que depende de la eslora del barco, buscamos aleatoriamente la posicion inicial, la cual, 
        si ya existe algo en esa casilla, volvera ejecutar el bucle hasta que lo consiga.
    -3º, mediante otro bucle while que tambien depende de la eslora y ademas, de una condición llamada romer.
        En este bucle, incrementamos el barco dependiendo de la orientación. 
        Si eso no fuera posible debido a que se salga del tablero o se encuentre otro barco, romper pasará a True.
        Tras romper el bucle, vuleve al primer bucle while y comenzará a buscar una nueva casilla de inicio.
    -4º, cuando cree cada barco, llamamos a la función colocar barco para que cuando se cree el proximo, reconozca esas casillas como ocupadas.
     """

    for barco in lista_barcos:
        eslora = int(barco[6])
        romper = False
        barco_aleatorio = []
        orientacion_aleatorio = random.choice(["N","S","E","O"])
    
        while len(barco_aleatorio) < eslora:
            romper = False
            barco_aleatorio = []
            fila_aleatorio = random.randint(0,9)
            columna_aleatorio = random.randint(0,9)
            fila_mutable = fila_aleatorio
            columna_mutable = columna_aleatorio
            
            if tablero[fila_aleatorio, columna_aleatorio] == " ":
                barco_aleatorio.append((fila_mutable, columna_mutable))                                    

            while len(barco_aleatorio) < eslora and romper == False:
                
                if orientacion_aleatorio == "O":                                                          
                    columna_mutable = columna_mutable - 1                                                  
                    if columna_mutable >= 0 and tablero[fila_mutable, columna_mutable] == " ":             
                        barco_aleatorio.append((fila_mutable, columna_mutable))
                    else:
                        romper = True
                
                elif orientacion_aleatorio == "E":
                    columna_mutable = columna_mutable + 1
                    if columna_mutable <= 9 and tablero[fila_mutable, columna_mutable] == " ":
                        barco_aleatorio.append((fila_mutable, columna_mutable))
                    else:
                        romper = True
                    
                elif orientacion_aleatorio == "N":
                    fila_mutable = fila_mutable - 1
                    if fila_mutable >= 0 and tablero[fila_mutable, columna_mutable] == " ":
                        barco_aleatorio.append((fila_mutable, columna_mutable))
                    else:
                        romper = True
                                
                elif orientacion_aleatorio == "S":
                    fila_mutable = fila_mutable + 1
                    if fila_mutable <= 9 and tablero[fila_mutable, columna_mutable] == " ":
                        barco_aleatorio.append((fila_mutable, columna_mutable))
                    else:
                        romper = True  

        colocar_barco(barco_aleatorio,eslora,tablero)
        crear_flota(barco,tablero,barco_aleatorio)

    return tablero

def comprobar_disparo(disparo, turno):
    """
    En esta función, lo que hacemos es mediante un bucle for, 
    recorremos cada flota creada y a su vez, las posiciones de cada barco.
    A medida que se acierta un disparo, se elimina esa posicion de la lista del barco.
    Cuando la lista del barco, se queda sin posiciones, imprimimos tocado y hundido.
    """

    estado = ""
    if turno == 'Usuario':
        for clave,valor in flota_maquina.items():
            for i, coordenada in  enumerate(valor):
                if coordenada == disparo:
                    flota_maquina[clave] = list(flota_maquina[clave])
                    flota_maquina[clave].pop(i)
                    flota_maquina[clave] = tuple(flota_maquina[clave])
                    if len(flota_maquina[clave]) == 0:
                        estado = (f"Tocado y hundido!!\n Enorabuena!! Has hundido el {clave}")
                    else:
                        estado = "Tocado"
    else:
        for clave,valor in flota_usuario.items():
            for i, coordenada in  enumerate(valor):
                if coordenada == disparo:
                    flota_usuario[clave] = list(flota_usuario[clave])
                    flota_usuario[clave].pop(i)
                    flota_usuario[clave] = tuple(flota_usuario[clave])
                    if len(flota_usuario[clave]) == 0:
                        estado = (f"Tocado y hundido!!\n Vaya!! Han hundido tu {clave}")
                    else:
                        estado = "Tocado"


    return estado       



def disparar():
    
    """
    En esta función he querido implementar, pese al lo que decía el enunciado, una elección aleatoria del turno.
    Para la demo, reduciremos a 4 al número de vidas pero por defecto serán 20.
    El bucle while se ejecutará hasta que uno de los 2 se quede sin vidas.
    En el turno del jugador 2 opciones:
    - Meter un input incorrecto. El cual te avisará y volveras a intentarlo
    - Meter input correcto:
        - La casilla esta en blanco. AGUA
        - En la casilla hay "-" o "X", se habrá repetido casilla y volverá a tirar.
        - Else: En la casilla habra un numero. TOCADO
    En el truno de la máquina, es igual pero lógicamente, no puede meter un imput incorrecto.
    Por ultimo, mediante una condición según las vidas de la máquina, seleccionará el ganador.
    Utilizamos el os.system('cls') para borrar los tableros que vamos generando.
    """
    print("Prepárate que esto comienza.\n Este es tu tablero")
    print(tablero_2)
    time.sleep(5)
    turno = random.choice(["Usuario","Máquina"])
    vidas_usuario = 20
    vidas_maquina = 20
    while vidas_usuario > 0 and vidas_maquina > 0:

        os.system('cls')

        if turno == 'Usuario':
            print(f"Es tu turno {usuario}")
            print(tablero_usuario)
            casilla = []
            lista_input = ['0','1','2','3','4','5','6','7','8','9']
            fila = input(f"{usuario} Introduzca numero de fila del 0 al 9:>")
            columna = input(f"{usuario} Introduzca numero de columna del 0 al 9:>")
            if fila in lista_input and columna in lista_input:
                casilla.append(int(fila))
                casilla.append(int(columna))
                casilla = tuple(casilla)
                if tablero_1[casilla] == " ":
                    print("Agua")
                    time.sleep(2)
                    tablero_1[casilla] = "-"
                    tablero_usuario[casilla] = "-"
                    turno = 'Máquina'
                    
                elif tablero_1[casilla] == '-' or tablero_1[casilla] == 'X':
                    turno == 'Usuario' 
                    print(f'{usuario} has repetido casilla, volverás a tirar')
                    time.sleep(2)

                else:
                    vidas_maquina = vidas_maquina - 1
                    print(comprobar_disparo(casilla,turno))
                    print(f"Genial {usuario}!! A la flota de {maquina} le quedan {vidas_maquina} aciertos para que la derrotes ")
                    time.sleep(4)
                    tablero_1[casilla] = "X"
                    tablero_usuario[casilla] = "X"
                    turno = 'Usuario'



            else:
                print(f'{usuario}, ya sabes que ese input no es correcto. Anda vuelve a introducirlo y que no se vuelva a repetir.')
                time.sleep(3.5)
                turno = 'Usuario'
            
                
                

        elif turno == 'Máquina':
            print(f"Es el turno de {maquina}")
            print(tablero_maquina)
            time.sleep(3)
            casilla = []
            fila_aleatorio = random.randint(0,9)
            columna_aleatorio = random.randint(0,9)
            casilla.append(fila_aleatorio)
            casilla.append(columna_aleatorio)
            casilla = tuple(casilla)

            if tablero_2[casilla] == " ":
                print("Agua")
                time.sleep(1.5)
                tablero_2[casilla] = "-"
                tablero_maquina[casilla] = "-"
                turno = 'Usuario'
                
            elif tablero_2[casilla] == "-" or tablero_2[casilla] == 'X':
                turno == 'Máquina' 
                print(f'{maquina} ha repetido casilla. Es lo que tiene los disparos aleatorios, que a veces se repiten')
                print(f"Volverá a tirar {maquina}")
                time.sleep(2.5)
                    

            else:
                vidas_usuario = vidas_usuario - 1
                print(comprobar_disparo(casilla,turno))
                print(f"Vaya! {maquina} te ha vuelto a tocar, cuidado que con {vidas_usuario} aciertos de {maquina} mas, habras sido derrotado ")
                time.sleep(4)
                tablero_2[casilla] = "X"
                tablero_maquina[casilla] = "X" 
                turno = 'Máquina'       

    os.system('cls')
    if vidas_maquina == 0:
        resultado = print(f"Has ganado {usuario} \n", tablero_1)
    
    else:
        resultado = print(f"Ha ganado {maquina}. Otra vez será \n", tablero_2)

    return resultado 

