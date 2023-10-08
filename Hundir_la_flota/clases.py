import numpy as np


class Tablero:

    """
    La clase tablero tiene fijo:
    -Todos estarán compuestos por una matriz en forma de cuadrado o rectangulo
    -Están compuestos por agua alas que cada casilla donde haya agua se repesentará con un ' '
    """

    forma = 'cuadrado o rectangulos'
    composicion = 'agua'


    def __init__(self, tamaño, operativo):

        """
        Los atributos varibles de la clase tablero son:
        -Tamaño. Donde definiremos el numero de casillas que tendrá de alto y de ancho
        -Operativo. 
            *Llamaremos tablero operativo (True), al tablero vacío y con las filas y columnas enumeradas con el que elijiremos las casillas
            *Llamaremos tablero no operativo (False). al tablero con los barcos representados y con el que se comparará cada disparo
        """


        self.tamaño = tamaño
        self.operativo = operativo


    def crear_tablero(tamaño, operativo):
        tablero = np.full(tamaño, " ")
        if operativo == True:
            a = np.arange(10).reshape(1,10)
            b = np.arange(11).reshape(11,1)
            tablero = np.append(tablero, a, axis = 0)
            tablero = np.append(tablero, b, axis = 1)
            

        return tablero
    
class Usuarios:

    """
    La clase denominada Usuarios, tendrá 2 atributos fijos
    -Tipo de usuario, el cual será humano y meterá las coordenadas a mano
    -Tipo de oponente, que será la comutadora y coordenadas se meterán automáticamente
    """

    tipo_usuario = 'Humano'
    tipo_oponente = "Computadora"


    def __init__(self, usuario):

        """
        la función usuario determinará el nombre del usuario 
        y te permitirá asignarle un nombre a tu oponente aunque seaa una computadora."""

        self.usuario = usuario


    def crear_usuario(usuario):

        if usuario == 'usuario':
            print('Bienvenido a Hundir la Flota')
            usuario = input('Introduzque su nombre, por favor:')
        elif usuario == 'maquina':
            print('Creo que llamarle máquina a tu oponente va a ser un poco frío')
            usuario = input('Por favor, introduzca un nombre para tu oponente:')
        else:
            print('De momento este juego esta pensado solo para los jugadores usuario y máquina. Quizas para el próximo proyecto ;) !!')

        return usuario
        