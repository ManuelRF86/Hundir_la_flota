![Descripción de la imagen](Hundir_la_flota/img/hundir-la-flota-juego-de-mesa.jpg)


# Hundir la Flota

Este proyecto consiste en la implementación del juego clásico Hundir la Flota en Python. La versión desarrollada incluye algunas particularidades para simplificar el desarrollo y ofrece la posibilidad de jugar contra la máquina.

## Funcionamiento del juego

- **Jugadores:** El juego involucra a dos jugadores: el usuario y la máquina.
- **Tablero:** Se utiliza un tablero de 10x10 para posicionar los barcos.
- **Colocación de barcos:** Se colocan barcos de diferentes longitudes de manera aleatoria en el tablero. Los barcos incluidos son: 4 barcos de 1 posición, 3 barcos de 2 posiciones, 2 barcos de 3 posiciones y 1 barco de 4 posiciones.
- **Objetivo:** Cada jugador intenta hundir los barcos del oponente disparando a coordenadas del tablero hasta que uno de los jugadores se queda sin barcos.
- **Turnos:** El juego funciona por turnos, comenzando por el jugador humano.
- **Disparos:** En cada turno, el jugador dispara a una coordenada del tablero del oponente. Si acierta, vuelve a disparar. En caso contrario, le toca al oponente.
- **Turnos de la máquina:** La máquina dispara aleatoriamente en los turnos en los que le toca. Si acierta, vuelve a disparar.
- **Fin del juego:** El juego termina cuando todos los barcos de un jugador han sido hundidos.

## Desarrollo del juego

El desarrollo del juego se divide en los siguientes elementos:

1. **Variables:** Se definen constantes en un archivo `variables.py` para las dimensiones del tablero y las características de los barcos.
2. **Clase Tablero:** Se implementa una clase `Tablero` en un archivo `clases.py` que gestiona la colocación de los barcos, los disparos y el estado del juego.
3. **Programa Principal:** El programa principal se encuentra en `main.py` y contiene el bucle principal del juego, donde se solicitan las coordenadas al usuario y se realizan los disparos.
4. **Funciones Auxiliares:** Las funciones auxiliares se encuentran en un archivo `funciones.py` y se utilizan para diversas tareas durante la ejecución del juego.

## Funcionalidades adicionales

Además de cumplir con los requisitos del enunciado, se han implementado las siguientes funcionalidades adicionales:

- **Numeración de casillas:** Se ha añadido la numeración de las casillas para facilitar la identificación de las coordenadas.
- **Indicación de barcos hundidos:** Cuando un barco es hundido, se marca como tocado y hundido en el tablero.

## Ejecución del juego

Para ejecutar el juego, simplemente se debe correr el archivo `main.py`. Se proporcionarán instrucciones durante la ejecución para guiar al jugador a través del juego.
