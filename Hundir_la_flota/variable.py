from clases import*

tablero_1 = Tablero.crear_tablero((10,10),False)
tablero_2 = Tablero.crear_tablero((10,10), False)
tablero_usuario = Tablero.crear_tablero((10,10),True)
tablero_maquina = Tablero.crear_tablero((10,10),True)

lista_barcos = ['barco_4', 'barco_3_1', 'barco_3_2', 'barco_2_1', 'barco_2_2', 'barco_2_3', 'barco_1_1', 'barco_1_2', 'barco_1_3', 'barco_1_4']

usuario = Usuarios.crear_usuario('usuario')
maquina = Usuarios.crear_usuario('maquina')

flota_usuario = {}
flota_maquina = {}
