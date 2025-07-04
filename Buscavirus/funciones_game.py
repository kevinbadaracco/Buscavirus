from random import randint
import pygame
from colores import *
from imagenes import *
from sonidos import *

#FUNCIONES LOGICAS

def generar_matriz(cantidad_de_filas:int, cantidad_de_columnas: int, valor_inicial: any) -> list:
    '''
    Documentacion:
    Funcion que retorna una matriz con filas, columnas, y el valor inicial de los elementos, dadas por parametros
    Parametro/s recibido/s:
    (cantidad_de_filas): dato de tipo int (cantidad de filas que tendra la matriz)
    (cantidad_de_columnas): dato de tipo int (cantidad de columnas que tendra la matriz)
    (valor_inicial): dato de tipo any (valor inicial de los elementos de la matriz)
    Retorno: list
    '''
    matriz_resultante = []

    for _ in range(cantidad_de_filas):
        filas_matriz_resultante = []
        for _ in range(cantidad_de_columnas):
            filas_matriz_resultante.append(valor_inicial)
        matriz_resultante.append(filas_matriz_resultante) 

    return matriz_resultante

def mostrar_matriz(matriz: list) -> None:
    '''
    Documentacion:
    Funcion que muestra por consola todos los elementos de una matriz dada por parametro
    Parametro/s recibido/s:
    (matriz): tipo de dato list (matriz de elementos con valores asignados)
    Retorno: None
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print("")
    print("")

def asignar_celdas_vacias_adyacentes(indice_fila: int, indice_columna: int, lista_de_indices_adyacentes: list, tablero_logico: list, tablero_logico_banderas: list, tablero_logico_celdas_despintadas: list, cantidad_de_clicks = 0) -> None:
    '''
    Documentacion:
    Funcion que se encarga de asignar una tuple o tuples a una lista, que representan las celdas vacias a despintar
    Parametro/s recibido/s:
    (indice_fila): Valor entero que representa el indice de fila de la matriz logica
    (indice_columna): Valor entero que representa el indice de columna de la matriz logica
    (lista_de_indices_adyacentes): Lista que almacena tuples, la cual tiene como valor el indice de fila y columna de una celda adyacente a despintar
    (tablero_logico): Matriz logica con valores numericos y "X"
    (tablero_logico_banderas): Matriz de valores booleanos utilizada para verificar en donde hay una bandera colocada, es decir, si es True, caso contrario, False 
    (tablero_logico_celdas_despintadas): Matriz de valores booleanos utlizada para verificar en donde ya hay una celda despintada, es decir, si es True, caso contario, False
    (cantidad_de_clicks): Parametro opcional, con valor entero 0
    Retorno: None
    '''
    indice_x_pre = 0
    indice_x_pos = 0
    indice_y_pos = 0
    indice_y_pre = 0

    if indice_fila == 0:
        indice_x_pre = 1
        indice_x_pos = 2
        indice_y_pos = 2
        if indice_columna == 0:
            indice_x_pre = 0
        elif indice_columna == len(tablero_logico[0]) - 1:
            indice_x_pos = 1
    elif indice_fila == len(tablero_logico) - 1:
        indice_x_pre = 1
        indice_x_pos = 2
        indice_y_pre = 1
        indice_y_pos = 1
        if indice_columna == 0:
            indice_x_pre = 0
        elif indice_columna == len(tablero_logico[0]) - 1:
            indice_x_pos = 1
    elif indice_columna == 0:
        indice_x_pos = 2
        indice_y_pre = 1
        indice_y_pos = 2
    elif indice_columna == len(tablero_logico[0]) - 1:
        indice_x_pre = 1
        indice_x_pos = 1
        indice_y_pre = 1
        indice_y_pos = 2
    else:
        indice_x_pre = 1
        indice_x_pos = 2
        indice_y_pre = 1
        indice_y_pos = 2

    if tablero_logico_celdas_despintadas[indice_fila][indice_columna] == False:    
        if tablero_logico[indice_fila][indice_columna] >= 1 and tablero_logico_banderas[indice_fila][indice_columna] == False:

            lista_de_indices_adyacentes.append((indice_fila, indice_columna))
            tablero_logico_celdas_despintadas[indice_fila][indice_columna] = True

        elif tablero_logico[indice_fila][indice_columna] == 0 and tablero_logico_banderas[indice_fila][indice_columna] == False:
            
            if cantidad_de_clicks == 1:
                for i in range(indice_fila - indice_y_pre, indice_fila + indice_y_pos):
                    for j in range(indice_columna - indice_x_pre, indice_columna + indice_x_pos):
                        if tablero_logico[i][j] != "X" and tablero_logico_banderas[i][j] == False:  
                            lista_de_indices_adyacentes.append((i, j))
            else:
                lista_de_indices_adyacentes.append((indice_fila, indice_columna))
                tablero_logico_celdas_despintadas[indice_fila][indice_columna] = True

                for i in range(indice_fila - indice_y_pre, indice_fila + indice_y_pos):
                    for j in range(indice_columna - indice_x_pre, indice_columna + indice_x_pos):
                        if (i, j) == (indice_fila, indice_columna):
                                continue
                        else:
                            if tablero_logico[i][j] != "X" and tablero_logico_banderas[i][j] == False:  
                                asignar_celdas_vacias_adyacentes(i, j, lista_de_indices_adyacentes, tablero_logico, tablero_logico_banderas, tablero_logico_celdas_despintadas)

def asignar_bombas_aleatorios_a_matriz(tablero_logico: list, lista_de_indices_en_primer_click: list, cant_minas: int) -> None:
    '''
    Documentacion:
    Funcion que asigna valores "X" de forma a una matriz logica dada por parametros, representando las bombas a colocar en las celdas del juego
    Parametro/s recibido/s:
    (tablero_logico): Matriz logica con valores numericos a la cual se le asignan valores "X" de forma aleatoria
    (lista_de_indices_en_primer_click): lista de tuples que contienen los indices en los cuales su valor no puede ser "X"
    (cant_minas): Valor entero que representa la cantidad de minas a asignar
    Retorno: None
    '''
    while cant_minas > 0:
        fila = randint(0, len(tablero_logico) - 1)
        columna = randint(0, len(tablero_logico[0]) - 1)
        
        bandera_indices_de_primer_click = False
        for i in range(len(lista_de_indices_en_primer_click)):
            if (fila, columna) == lista_de_indices_en_primer_click[i]:
                bandera_indices_de_primer_click = True
        
        if bandera_indices_de_primer_click == False:
            tablero_logico[fila][columna] = "X"
            cant_minas -= 1

def asignar_contador_de_bombas_adyacentes_en_celda(tablero_logico: list, indice_fila: int, indice_columna: int) -> None:
    '''
    Documentacion:
    Funcion que asigna un valor entero (entre 1 y 8) a un solo elemento de la matriz logica dada por parametros en base a la cantidad de "X" que se encuentran a su alrededor
    (tablero_logico): Matriz logica con valores numericos y "X"
    (indice_fila): Valor entero que representa el indice de fila de la matriz
    (indice_columna): Valor entero que representa el indice de columna de la matriz
    Retorno: None
    '''
    indice_x_pre = 0
    indice_x_pos = 0
    indice_y_pos = 0
    indice_y_pre = 0

    indice_x_pre = 0
    indice_x_pos = 0
    indice_y_pos = 0
    indice_y_pre = 0

    if indice_fila == 0:
        indice_x_pre = 1
        indice_x_pos = 2
        indice_y_pos = 2
        if indice_columna == 0:
            indice_x_pre = 0
        elif indice_columna == len(tablero_logico[0]) - 1:
            indice_x_pos = 1
    elif indice_fila == len(tablero_logico) - 1:
        indice_x_pre = 1
        indice_x_pos = 2
        indice_y_pre = 1
        indice_y_pos = 1
        if indice_columna == 0:
            indice_x_pre = 0
        elif indice_columna == len(tablero_logico[0]) - 1:
            indice_x_pos = 1
    elif indice_columna == 0:
        indice_x_pos = 2
        indice_y_pre = 1
        indice_y_pos = 2
    elif indice_columna == len(tablero_logico[0]) - 1:
        indice_x_pre = 1
        indice_x_pos = 1
        indice_y_pre = 1
        indice_y_pos = 2
    else:
        indice_x_pre = 1
        indice_x_pos = 2
        indice_y_pre = 1
        indice_y_pos = 2
    
    contador_bombas = 0
    for i in range(indice_fila - indice_y_pre, indice_fila + indice_y_pos):
        for j in range(indice_columna - indice_x_pre, indice_columna + indice_x_pos):
            if tablero_logico[i][j] == "X":
                contador_bombas += 1
    
    if tablero_logico[indice_fila][indice_columna] != "X" and contador_bombas > 0:
        tablero_logico[indice_fila][indice_columna] = contador_bombas

def asignar_cantidad_de_bombas_adyacentes_en_superficie_de_celdas(tablero_logico: list) -> None:
    '''
    Documentacion:
    Funcion que recorre y asigna a todos los elementos de una matriz la cantidad de "X" que se encuentran a su alrededor, representando la cantidad de minas que puede haber alrededor de una celda vacia
    Parametro/s recibido/s:
    (tablero_logico): Matriz logica con valores numericos y "X"
    Retorno: None
    '''
    for i in range(len(tablero_logico)):
        for j in range(len(tablero_logico[i])):
            asignar_contador_de_bombas_adyacentes_en_celda(tablero_logico, i, j)

#FUNCION PARA HOVER EN RECTANGULO

def cambiar_color_boton(bandera_hover: bool, pantalla: pygame.Surface, color_base: tuple, color_temporal: tuple, rectangulo: pygame.Rect) -> None:
        '''
        Documentacion:
        Funcion que se encarga de cambiar el color  de un rectangulo cuando nos posicionamos sobre el mismo, es decir, simular un cambio de estado de un boton
        Parametro/s recibido/s:
        (bandera_hover): Valor booleano que indica si el cursor del mouse se encuentra posicionado sobre un rectangulo especifico
        (pantalla): Superficie del juego pygame que establece en donde se va a dibujar el rectangulo
        (color_base): Tuple de enteros que representan el color RGB base que va a tener el rectangulo
        (color_temporal): Tuple de enteros que representan el color RGB temporal que va a tener el rectangulo
        (rectangulo): Rectangulo del juego pygame que representa el boton al cual le modificamos el color
        Retorno: None
        '''
        if bandera_hover == True:
            pygame.draw.rect(pantalla, color_temporal, rectangulo)
        else:
            pygame.draw.rect(pantalla, color_base, rectangulo)

#MOSTRAR IMAGEN DE SONIDO MUTEADO O NO

def mostrar_imagen_sonido(bandera_sonido: bool, ancho_boton: int, alto_boton: int, pantalla: pygame.Surface, rectangulo_sonido: pygame.Rect) -> None:
    '''
    Documentacion:
    Funcion que se encarga de alternar una imagen a otra, para simular el cambio de sonido
    Parametro/s recibido/s:
    (bandera_sonido): Valor booleano que indica que si es True entonces dibujamos la imagen que tiene sonido, en caso contrario, dibujamos la imagen sin sonido con sus respectivas medidas
    (ancho_boton): Valor entero que determina el ancho que va a tener un rectangulo especifico
    (alto_boton): Valor entero que determina el alto que va a tener un rectangulo especifico
    (pantalla): Superficie del juego pygame que establece en donde se va a dibujar el rectangulo
    (rectangulo_sonido): Rectangulo del juego pygame que representa el boton del sonido
    Retorno: None
    '''
    imagen_sonido = pygame.transform.scale(pygame.image.load(lista_imagenes["icono_sonido"]), (ancho_boton, alto_boton))
    imagen_sonido_muteado = pygame.transform.scale(pygame.image.load(lista_imagenes["icono_muteado"]), (ancho_boton, alto_boton))

    if bandera_sonido == True:
        pantalla.blit(imagen_sonido, ((rectangulo_sonido.centerx - (ancho_boton / 2)), (rectangulo_sonido.centery - (alto_boton / 2))))
    else:
        pantalla.blit(imagen_sonido_muteado, ((rectangulo_sonido.centerx - (ancho_boton / 2)), (rectangulo_sonido.centery - (alto_boton / 2))))

def configurar_volumen_sonido_de_fondo(bandera_sonido_fondo: bool, arranque: int) -> None:
    '''
    Documentacion:
    Funcion que se encarga de configurar el volumen de sonido de fondo, verificando que en caso de que no haya musica, iniciar el sonido de fondo, pero si ya hay, solamente bajarle el volumen
    Parametro/s recibido/s:
    (bandera_sonido_fondo): Valor booleano que indica si ya hay musica de fondo, si es False, iniciar el sonido de fondo, caso contrario, solamente bajarle el volumen
    (arranque): Valor entero que indica el arranque de la musica, si es 0 verifica si no hay musica en el juego, si es 1, inicia la musica
    Retorno: None
    '''
    if arranque == 0:
        if pygame.mixer.music.get_busy() == False:
            arranque = 1

    if arranque == 1:
            pygame.mixer.music.load(lista_sonidos["sonido_de_fondo"])
            pygame.mixer.music.set_volume(.1)
            pygame.mixer.music.play(-1)

        
    if bandera_sonido_fondo == True:
        pygame.mixer.music.set_volume(.1)
    else:
        pygame.mixer.music.set_volume(0)

def reproducir_sonido_derrota(bandera_sonido_fondo: bool, bandera_sonido_game_over: bool) -> None:
    '''
    Documentacion:
    Funcion que se encarga de reproducir un sonido de derrota
    Parametro/s recibido/s:
    (bandera_sonido_fondo): Valor booleano que indica si ya hay musica de fondo, si es True, cambiamos el volumen de sonido a 0
    (bandera_sonido_game_over): Valor booleano que verifica si debemos reproducir un sonido de derrota, en caso que sea True, reproducimos el mismo
    Retorno: None
    '''
    if bandera_sonido_fondo == True:
        configurar_volumen_sonido_de_fondo(False, 0)

    if bandera_sonido_game_over == True:
        pygame.mixer.music.load(lista_sonidos["sonido_de_derrota"])
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play(0)

def reproducir_sonido_victoria(bandera_sonido_fondo: bool, bandera_sonido_victoria: bool) -> None:
    '''
    Documentacion:
    Funcion que se encarga de reproducir un sonido de victoria, en caso de que ya haya un sonido de fondo, finalizarlo y ejecutar el sonido de victoria
    Parametro/s recibido/s:
    (bandera_sonido_fondo): Valor booleano que indica si ya hay musica de fondo, si es True, cambiamos el volumen de sonido a 0
    (bandera_sonido_victoria): Valor booleano que verifica si debemos reproducir un sonido de derrota, en caso que sea True, reproducimos el mismo
    Retorno: None
    '''
    if bandera_sonido_fondo == True:
        configurar_volumen_sonido_de_fondo(False, 0)

    if bandera_sonido_victoria == True:
        pygame.mixer.music.load(lista_sonidos["sonido_de_victoria"])
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play(0)

#FUNCIONES PARA LA CUADRICULA DE CELDAS, MINAS Y BANDERAS

def determinar_cant_filas_columns_minas_banderas(modo_dificultad: int) -> list:
    '''
    Documentacion:
    Funcion que se encarga de retornar un lista la cual almacena la cantidad de filas, columnas, minas y banderas que va a tener el juego segun la dificultad dada por parametros
    Parametro/s recibido/s:
    (modo_dificultad): Valor entero que representa la dificultad que tendra un juego especifico
    Retorno: list
    '''
    if modo_dificultad == 1:
            cantidad_filas_celdas = 8
            cantidad_columnas_celdas = 8
            cantidad_de_minas = 10
            cantidad_de_banderas = 10
    elif modo_dificultad == 2:
        cantidad_filas_celdas = 16
        cantidad_columnas_celdas = 16
        cantidad_de_minas = 50
        cantidad_de_banderas = 50
    elif modo_dificultad == 3:      
        cantidad_filas_celdas = 24
        cantidad_columnas_celdas = 24
        cantidad_de_minas = 120
        cantidad_de_banderas = 120

    return [cantidad_filas_celdas, cantidad_columnas_celdas, cantidad_de_minas, cantidad_de_banderas]

def generar_cuadricula_de_celdas_ocultas_en_superficie(cantidad_filas_celdas: int, cantidad_columnas_celdas: int, ancho_celda: int, alto_celda: int, superficie: pygame.Surface) -> list:
    '''
    Documentacion:
    Funcion que retorna una matriz donde todos sus elementos son pygame.Rect, los cuales poseen sus propiedades individuales para poder acceder a dichas en caso de ser necesario
    Parametro/s recibido/s:
    (cantidad_filas_celdas): Valor entero que representa la cantidad de filas que tendra una matriz
    (cantidad_columnas_celdas): Valor entero que representa la cantidad de columnas que tendra una matriz
    (ancho_celda): Valor entero que representa el ancho que tendra un rectangulo especifico
    (alto_celda): Valor entero que representa el alto que tendra un rectangulo especifico 
    (superficie): Superficie del juego pygame a la cual le dibujaremos los rectangulos especificos
    Retorno: list[pygame.Rect]
    '''
    #CREAMOS LA IMAGEN DE LA CELDA OCULTA Y LA ESCALAMOS
    imagen_celda_oculta = pygame.image.load(lista_imagenes["celda_oculta"])
    imagen_celda_oculta = pygame.transform.scale(imagen_celda_oculta, (ancho_celda, alto_celda))

    #POSICION INICIAL DE LOS RECTANGULOS DE MINAS
    posicion_x = 0
    posicion_y = 0

    #VAMOS A CREAR UNA MATRIZ DE CELDAS PARA REFERENCIARLOS INDIVUALMENTE A CADA UNO LUEGO DE QUE HAYAN SIDO DIBUJADOS
    matriz_de_celdas = []

    for _ in range(cantidad_filas_celdas):
        fila_de_celdas = []
        for _ in range(cantidad_columnas_celdas):
            celda_oculta = superficie.blit(imagen_celda_oculta, (posicion_x, posicion_y))
            posicion_x += ancho_celda
            fila_de_celdas += [celda_oculta]
        matriz_de_celdas += [fila_de_celdas]
        posicion_y += alto_celda
        posicion_x = 0

    return matriz_de_celdas

def buscar_minas_en_superficie_del_juego(matriz_logica: list) -> list:
    '''
    Documentacion:
    Funcion que retorna una lista de tuples, las tuples poseen un indice de fila y columna, en el cual el elemento de dicha tuple es una "X", representando una mina hallada en las celdas de juego
    Parametro/s recibido/s:
    (matriz_logica): Matriz logica con valores numericos y "X"
    Retorno: list[tuple]
    '''
    lista_indices_minas = []
    for i in range(len(matriz_logica)):
        for j in range(len(matriz_logica[i])):
            if matriz_logica[i][j] == "X":
                lista_indices_minas.append((i, j))
    
    return lista_indices_minas

def mostrar_minas_en_superficie(indice_fila: int, indice_columna: int, lista_de_indices_minas: list, matriz_de_celdas:list, ancho_celda: int, alto_celda: int, superficie_juego: pygame.Surface) -> None:
    '''
    Documentacion:
    Funcion que se encarga de dibujar pygame.images, las cuales son imagenes de minas encontradas en la superficie del juego
    Parametro/s recibido/s:
    (indice_fila): Valor entero que representa el indice de fila de la matriz logica
    (indice_columna): Valor entero que representa el indice de columna de la matriz logica 
    (lista_de_indices_minas): Lista de tuples, las cuales representan los indices en los que hay una "X" en la matriz logica
    (matriz_de_celdas): Matriz de elementos pygame.Rect, en los que vamos a dibujar una imagen obteniendo indice de fila y columna de la misma
    (ancho_celda): Valor entero que representa el ancho que tendra un rectangulo especifico
    (alto_celda): Valor entero que representa el alto que tendra un rectangulo especifico 
    (superficie): Superficie del juego pygame a la cual le dibujaremos los rectangulos especificos
    Retorno: None
    '''
    mina_revelada = pygame.transform.scale(pygame.image.load(lista_imagenes["celda_virus_descubierto"]), (ancho_celda, alto_celda))
    mina_clickeada = pygame.transform.scale(pygame.image.load(lista_imagenes["celda_virus_clickeado"]), (ancho_celda, alto_celda))


    for i in range(len(lista_de_indices_minas)):
        indice_i = lista_de_indices_minas[i][0]
        indice_j = lista_de_indices_minas[i][1]
        if (indice_fila, indice_columna) == (indice_i, indice_j):
            superficie_juego.blit(mina_clickeada, matriz_de_celdas[indice_i][indice_j].topleft)
        else:
            superficie_juego.blit(mina_revelada, matriz_de_celdas[indice_i][indice_j].topleft)

def mostrar_celdas_vacias_adyacentes(lista_de_indices_celdas: list, matriz_logica: list, matriz_de_celdas: list, ancho_celda: int, alto_celda: int, superficie_juego: pygame.Surface) -> None:
    '''
    Documentacion:
    Funcion que se encarga de dibujar pygame.images, las cuales son celdas vacias adyacentes en una superficie del juego, son identificadas a traves de una lista de indices dadas por parametros
    Parametro/s recibido/s:
    (lista_de_indices_celdas): Lista de tuples, las cuales representan los elementos con valores entre 0 y 8 de la matriz logica
    (matriz_logica): Matriz logica de valores numericos y "X"
    (matriz_de_celdas): Matriz de elementos pygame.Rect, en los que vamos a dibujar una imagen obteniendo indice de fila y columna de la misma
    (ancho_celda): Valor entero que representa el ancho que tendra un rectangulo especifico
    (alto_celda): Valor entero que representa el alto que tendra un rectangulo especifico 
    (superficie_juego): Superficie del juego pygame a la cual le dibujaremos los rectangulos especificos
    Retorno: None
    '''
    imagen_celda_vacia = pygame.transform.scale(pygame.image.load(lista_imagenes["celda_vacia"]), (ancho_celda, alto_celda))
    imagen_celda_1 = pygame.transform.scale(pygame.image.load(lista_imagenes["celda_1"]), (ancho_celda, alto_celda))
    imagen_celda_2 = pygame.transform.scale(pygame.image.load(lista_imagenes["celda_2"]), (ancho_celda, alto_celda))
    imagen_celda_3 = pygame.transform.scale(pygame.image.load(lista_imagenes["celda_3"]), (ancho_celda, alto_celda))
    imagen_celda_4 = pygame.transform.scale(pygame.image.load(lista_imagenes["celda_4"]), (ancho_celda, alto_celda))
    imagen_celda_5 = pygame.transform.scale(pygame.image.load(lista_imagenes["celda_5"]), (ancho_celda, alto_celda))            
    imagen_celda_6 = pygame.transform.scale(pygame.image.load(lista_imagenes["celda_6"]), (ancho_celda, alto_celda))
    imagen_celda_7 = pygame.transform.scale(pygame.image.load(lista_imagenes["celda_7"]), (ancho_celda, alto_celda))
    imagen_celda_8 = pygame.transform.scale(pygame.image.load(lista_imagenes["celda_8"]), (ancho_celda, alto_celda))

    for i in range(len(lista_de_indices_celdas)):
        indice_i = lista_de_indices_celdas[i][0]
        indice_j = lista_de_indices_celdas[i][1]

        match matriz_logica[indice_i][indice_j]:
            case 0:
                superficie_juego.blit(imagen_celda_vacia, matriz_de_celdas[indice_i][indice_j].topleft)
            case 1:
                superficie_juego.blit(imagen_celda_1, matriz_de_celdas[indice_i][indice_j].topleft)
            case 2:
                superficie_juego.blit(imagen_celda_2, matriz_de_celdas[indice_i][indice_j].topleft)
            case 3:
                superficie_juego.blit(imagen_celda_3, matriz_de_celdas[indice_i][indice_j].topleft)
            case 4:
                superficie_juego.blit(imagen_celda_4, matriz_de_celdas[indice_i][indice_j].topleft)
            case 5:
                superficie_juego.blit(imagen_celda_5, matriz_de_celdas[indice_i][indice_j].topleft)
            case 6:
                superficie_juego.blit(imagen_celda_6, matriz_de_celdas[indice_i][indice_j].topleft)
            case 7:
                superficie_juego.blit(imagen_celda_7, matriz_de_celdas[indice_i][indice_j].topleft)
            case 8:
                superficie_juego.blit(imagen_celda_8, matriz_de_celdas[indice_i][indice_j].topleft)

#DIBUJAR CONTADOR DE MINAS/BANDERAS

def verificar_cantidad_de_banderas_dibujadas_en_superficie(cantidad_de_banderas: int, matriz_logica_banderas: list) -> bool:
    '''
    Documentacion:
    Funcion que retorna un booleano, en caso de que las banderas dibujadas en pantalla sea igual a la cantidad de banderas que hay segun la dificultad, no permite mas que banderas sean dibujadas
    Parametro/s recibido/s:
    (cantidad_de_banderas): Valor entero que representa la cantidad de banderas que se pueden utilizar en el juego
    (matriz_logica_banderas): Matriz de valores booleanos utilizada para verificar en donde hay una bandera colocada, es decir, si es True, caso contrario, False
    Retorno: bool
    '''
    bandera_seguir_dibujando_banderas = True

    for i in range(len(matriz_logica_banderas)):
        for j in range(len(matriz_logica_banderas[i])):
            if matriz_logica_banderas[i][j] == True:
                cantidad_de_banderas -= 1
    
    if cantidad_de_banderas == 0:
        bandera_seguir_dibujando_banderas = False

    return bandera_seguir_dibujando_banderas

def asignar_o_quitar_celdas_con_bandera(indice_fila: int, indice_columna: int, tablero_logico_banderas: list, lista_de_indices_bandera: list, tablero_logico_celdas_despintadas: list, cantidad_de_banderas: int) -> None:
    '''
    Documentacion:
    Funcion que se encarga de asignar o quitar una tuple, la cual contiene el indice de fila y columna de una matriz a una lista
    Parametro/s recibido/s:
    (indice_fila): Valor entero que representa el indice de fila de una matriz especifica
    (indice_columna): Valor entero que representa el indice de columna de una matriz especifica
    (tablero_logico_banderas): Matriz de valores booleanos utilizada para verificar en donde hay una bandera colocada, es decir, si es True, caso contrario, False
    (lista_de_indices_bandera): Lista de tuples, que representan los indices en los cuales va a haber una bandera a dibujar
    (tablero_logico_celdas_despintadas): Matriz de valores booleanos utlizada para verificar en donde ya hay una celda despintada, es decir, si es True, caso contario, False
    (cantidad_de_banderas): Valor entero que representa la cantidad de banderas que se pueden utilizar en el juego
    Retorno: None
    '''
    if tablero_logico_celdas_despintadas[indice_fila][indice_columna] == False:

        if tablero_logico_banderas[indice_fila][indice_columna] == False:

            if verificar_cantidad_de_banderas_dibujadas_en_superficie(cantidad_de_banderas, tablero_logico_banderas) == True:

                tablero_logico_banderas[indice_fila][indice_columna] = True  
                lista_de_indices_bandera.append((indice_fila, indice_columna))

        elif tablero_logico_banderas[indice_fila][indice_columna] == True:
            tablero_logico_banderas[indice_fila][indice_columna] = False
            lista_de_indices_bandera.remove((indice_fila, indice_columna))

def mostrar_celdas_con_bandera(lista_de_indices_celdas_con_bandera: list, matriz_logica_banderas: list, matriz_de_celdas: list, ancho_celda: int, alto_celda: int, superficie_juego: pygame.Surface) -> None:
    '''
    Documentacion:
    Funcion que se encarga de dibujar pygame.images, las cuales son celdas con banderas, a una superficie del juego
    Parametro/s recibido/s:
    (lista_de_indices_celdas_con_bandera): Lista de tuples, que representan los indices en los cuales va a haber una bandera a dibujar
    (matriz_logica_banderas): Matriz de valores booleanos utilizada para verificar en donde hay una bandera colocada, es decir, si es True, caso contrario, False
    (matriz_de_celdas): Matriz de elementos pygame.Rect, en los que vamos a dibujar una imagen obteniendo indice de fila y columna de la misma
    (ancho_celda): Valor entero que representa el ancho que tendra un rectangulo especifico
    (alto_celda): Valor entero que representa el alto que tendra un rectangulo especifico 
    (superficie_juego): Superficie del juego pygame a la cual le dibujaremos los rectangulos especificos
    Retorno: None
    '''

    celda_bandera = pygame.transform.scale(pygame.image.load(lista_imagenes["celda_bandera"]), (ancho_celda, alto_celda))

    for i in range(len(lista_de_indices_celdas_con_bandera)):
        indice_i = lista_de_indices_celdas_con_bandera[i][0]
        indice_j = lista_de_indices_celdas_con_bandera[i][1]

        match matriz_logica_banderas[indice_i][indice_j]:
            case True:
                superficie_juego.blit(celda_bandera, matriz_de_celdas[indice_i][indice_j].topleft)

def dibujar_contador_de_banderas_en_pantalla(cantidad_de_banderas: int, lista_celdas_con_bandera: list, fuente: pygame.font.Font, pantalla: pygame.Surface, rectangulo_contador_banderas: pygame.Rect) -> None:
    '''
    Documentacion:
    Funcion que se encarga de dibujar un image.text, el cual es un contador de banderas colocadas en la superficie del juego dado por parametros
    Parametro/s recibido/s:
    (cantidad_de_banderas): Valor entero que representa la cantidad de banderas que se pueden utilizar en el juego
    (lista_celdas_con_bandera): Lista de tuples, que representan los indices en los cuales va a haber una bandera a dibujar
    (fuente): Fuente de de texto pygame a utilizar para dibujar el contador de banderas
    (pantalla):  Superficie del juego pygame a la cual le dibujaremos un rectangulo especifico
    (rectangulo_contador_banderas): Rectangulo de pygame sobre el cual dibujaremos un texto especifico
    Retorno: None
    '''
    contador_de_banderas_str = str(cantidad_de_banderas - len(lista_celdas_con_bandera))

    texto_contador_banderas = fuente.render(contador_de_banderas_str, True, colores["rojo"])

    posicion_x = rectangulo_contador_banderas.centerx - (texto_contador_banderas.get_width() / 2)
    posicion_y = rectangulo_contador_banderas.centery - (texto_contador_banderas.get_height() / 2)
    pantalla.blit(texto_contador_banderas, (posicion_x, posicion_y))

#FUNCIONES PARA PUNTAJES Y TIMER

def verificar_victoria(matriz_logica_celdas_despintadas: list, cantidad_total_celdas: int, cantidad_minas: int) -> bool:
    '''
    Documentacion:
    Funcion que retorna un bool, verifica si el jugador ha ganado contando las celdas realmente despintadas, si ha ganado retorna True, en caso contrario no retorna nada
    Parametro/s recibidos:
    (matriz_logica_celdas_despintadas): Matriz de valores booleanos utlizada para verificar en donde ya hay una celda despintada, es decir, si es True, caso contario, False
    (cantidad_total_celdas): Valor entero que representa la totalidad de celdas que va a tener el juego segun su dificultad
    (cantidad_minas): Valor entero que representa la cantidad de minas presentes en el juego segun su dificultad
    Retorno: bool
    '''
    contador_celdas_despintadas = 0
    bandera_victoria = False

    for i in range(len(matriz_logica_celdas_despintadas)):
        for j in range(len(matriz_logica_celdas_despintadas[i])):
            if matriz_logica_celdas_despintadas[i][j] == True:
                contador_celdas_despintadas += 1
    
    celdas_necesarias_para_ganar = cantidad_total_celdas - cantidad_minas
    
    if contador_celdas_despintadas >= celdas_necesarias_para_ganar:
        bandera_victoria = True
    
    return bandera_victoria

def obtener_tiempo_formateado(segundos_totales: int) -> str: 
    '''
    Documentacion:
    Funcion que retorna un str, el cual es un formato MM:SS, convertido por los segundos totales dados por parametros
    Parametro/s recibicido/s:
    (segundos_totales): valor entero que representa los segundos totales transcurridos en la partida 
    Retorno: str
    '''
    minutos = int(segundos_totales // 60)
    segundos = int(segundos_totales % 60)
    
    if minutos < 10:
        minutos_str = "0" + str(minutos)
    else:
        minutos_str = str(minutos)
    
    if segundos < 10:
        segundos_str = "0" + str(segundos)
    else:
        segundos_str = str(segundos)
    
    return minutos_str + ":" + segundos_str

def dibujar_timer_en_pantalla(tiempo_formateado: str, fuente: pygame.font.Font, pantalla: pygame.Surface, rectangulo_timer: pygame.Rect) -> None:
    '''
    Documentacion
    Funcion que se encarga de dibujar un pygame.text, el cual un timer del tiempo transcurrido de la partida dado por parametro, en la esquina superior derecha de la pantalla
    Parametro/s recibicido/s:
    (tiempo_formateado): valor string que repesenta el tiempo transcurrido en la partida
    (fuente): Fuente de de texto pygame a utilizar para dibujar el texto del timer
    (pantalla):  Superficie del juego pygame a la cual le dibujaremos un rectangulo especifico
    (rectangulo_timer): Rectangulo de pygame sobre el cual dibujaremos un texto especifico
    Retorno: None
    '''
    texto_timer = fuente.render(tiempo_formateado, True, colores["rojo"])
    posicion_x = rectangulo_timer.centerx - (texto_timer.get_width() / 2)
    posicion_y = rectangulo_timer.centery - (texto_timer.get_height() / 2)
    pantalla.blit(texto_timer, (posicion_x, posicion_y))

def determinar_cantidad_de_puntos_de_jugador(tiempo: int, dificultad: int) -> int:
    '''
    Documentacion:
    Funcion que retorna un int, el cual es la cantidad de puntos de un jugador en caso de ganar la partida, empieza con puntos base determinados segun la dificultad y son restados por el tiempo transcurrido de inicio de la partida dado por parametros
    Parametro/s recibicido/s:
    (tiempo): valor entero que representa los segundos totales transcurridos en la partida
    (dificultad): valor entero que representa la dificultad en la cual se produce el juego
    Retorno: int
    '''
    if dificultad == 1:
        puntos_base_dificultad = 400
    elif dificultad == 2:
        puntos_base_dificultad = 800
    elif dificultad == 3:
        puntos_base_dificultad == 1600

    puntos_jugador = (dificultad * puntos_base_dificultad) - tiempo

    return puntos_jugador

def guardar_puntaje_en_archivo(nombre: str, puntos_jugador: int, tiempo: int, dificultad: int) -> None:
    '''
    Documentacion:
    Funcion que se encarga de almacenar texto en un archivo .txt, el cual es el nombre, puntos, tiempo de partida y dificultad del jugador en caso de que haya ganado la partida
    Parametro/s recibicido/s:
    (nombre): valor string que representa el nomnbre de un jugador victorioso especifico 
    (puntos_jugador): valor entero que representa el puntaje obtenido por el jugador
    (tiempo): valor entero que representa los segundos totales transcurridos en la partida
    (dificultad): valor entero que representa la dificultad en la cual se produce el juego
    Retorno: None
    '''
    archivo = open("puntajes.txt", "a")
    archivo.write(nombre + "," + str(puntos_jugador) + "," + str(tiempo) + "," + str(dificultad) + "\n")
    archivo.close()

def leer_puntajes_desde_archivo(tipo_archivo: str) -> list:
    '''
    Documentacion:
    Funcion que retorna una lista de diccionarios, los cuales almacenanan la informacion del jugador victorioso en la partida, se encarga de leer texto de un archivo .txt, en caso de que dicho archivo no exista lo crea
    Parametro/s recibicido/s:
    (tipo_archivo): valor str que representa la URL de un archivo especifico
    Retorno: list[dict]
    '''
    lista_puntajes = []
    
    try:
        open(tipo_archivo, "r").close()
    except:
        open(tipo_archivo, "w").close()

    archivo = open(tipo_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    
    for linea in lineas:
        if linea.strip() != "":
            datos = linea.strip().split(",")
            puntaje = {
                "nombre": datos[0],
                "puntos": datos[1],
                "tiempo": float(datos[2]),
                "dificultad": int(datos[3])
            }
            lista_puntajes.append(puntaje)
    
    return lista_puntajes

def ordenar_puntajes(lista_puntajes: list) -> None:
    '''
    Documentacion:
    Funcion que se encarga de leer una lista de diccionarios y ordenarlos de mayor a menor segun los puntos obtenidos por cada jugador
    Parametro/s recibicido/s:
    (lista_puntajes): lista de diccionarios que almacena el nombre y el puntaje de los jugadores victoriosos
    Retorno: None
    '''

    for i in range(len(lista_puntajes) - 1):
        for j in range(i + 1, len(lista_puntajes)):
            if int(lista_puntajes[i]["puntos"]) < int(lista_puntajes[j]["puntos"]):
                auxiliar_puntajes = lista_puntajes[i]
                lista_puntajes[i] = lista_puntajes[j]
                lista_puntajes[j] = auxiliar_puntajes

def obtener_top_10_puntajes(puntajes_ordenados: list) -> list:
    '''
    Documentacion:
    Funcion que retorna una lista de 10 diccionarios unicamente, en caso de que haya menos retorna los que haya
    Parametro/s recibicido/s:
    (puntajes_ordenados): lista que almacena los nombres y puntajes de los jugadores victoriosos ya ordenada
    Retorno: list[dict]
    '''

    if len(puntajes_ordenados) >= 10:
        puntajes_ordenados = puntajes_ordenados[0:10]
    
    return puntajes_ordenados
    
def obtener_nombre_dificultad(numero_dificultad: int) -> str:
    '''
    Documentacion:
    Funcion que retorna un str, el cual es un texto obtenido segun la dificultad de la partida dada por parametros
    Parametro/s recibicido/s:
    numero_dificultad: valor entero que represnta la dificultad de la partida
    Retorno: str
    '''
    dificultad = ""

    if numero_dificultad == 1:
        dificultad = "FACIL"
    elif numero_dificultad == 2:
        dificultad = "NORMAL"
    elif numero_dificultad == 3:
        dificultad = "DIFICIL"
    else:
        dificultad = "FACIL"

    return dificultad

def dibujar_puntajes_en_pantalla(mejores_puntajes: list, fuente_texto: pygame.font.Font, pantalla: pygame.Surface) -> None:
    '''
    Documentacion:
    Funcion que se encarga de dibujar pygame.texts, los cuales son textos de los jugadores victorios en las partidas ordenados de mayor a menor segun su puntaje, en la pantalla dada por parametros
    Parametro/s recibicido/s:
    (mejores_puntajes): lista de 10 diccionarios que reprenstan los 10 mejores puntajes obtenidos en el juego 
    (fuente_texto): Fuente de de texto pygame a utilizar para dibujar los puntajes
    (pantalla): Superficie del juego pygame a la cual le dibujaremos un texto especifico
    Retorno: None
    '''
    posicion_y_inicial = 150

    if len(mejores_puntajes) == 0:
        texto_sin_puntajes = "NO HAY PUNTAJES ACTUALMENTE"
        linea_sin_puntaje = fuente_texto.render(texto_sin_puntajes, True, colores["blanco"])

        pantalla.blit(linea_sin_puntaje, ((pantalla.get_width() / 2) - (linea_sin_puntaje.get_width() / 2), ((pantalla.get_height() / 2) - (linea_sin_puntaje.get_height() / 2))))
    else:
        for i in range(len(mejores_puntajes)):
            numero_posicion = str(i + 1)
            nombre = mejores_puntajes[i]["nombre"]
            puntos = mejores_puntajes[i]["puntos"]
            tiempo = obtener_tiempo_formateado(mejores_puntajes[i]["tiempo"])
            dificultad = obtener_nombre_dificultad(mejores_puntajes[i]["dificultad"])
            
            texto_puntaje = numero_posicion + ". " + nombre + " - " + puntos + " Pts" + " - " + tiempo + " - " + dificultad

            if numero_posicion == "1":
                linea_puntaje = fuente_texto.render(texto_puntaje, True, colores["amarillo"])
            elif numero_posicion == "2":
                linea_puntaje = fuente_texto.render(texto_puntaje, True, colores["plateado"])
            elif numero_posicion == "3":
                linea_puntaje = fuente_texto.render(texto_puntaje, True, colores["marron"])
            else:
                linea_puntaje = fuente_texto.render(texto_puntaje, True, colores["blanco"])

            pantalla.blit(linea_puntaje, ((pantalla.get_width() / 2) - (linea_puntaje.get_width() / 2), posicion_y_inicial + (i * 50)))


    

