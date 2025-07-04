import pygame 
from colores import *
from funciones_game import *
from imagenes import *
from sonidos import *        

pygame.init()

#CREACION DE PANTALLA
ancho_pantalla = 720
alto_pantalla = 720
centro_pantalla_x = ancho_pantalla / 2
centro_pantalla_y = alto_pantalla / 2

pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Buscavirus")

#IMAGEN DE FONDO
imagen_fondo_juego = pygame.image.load(lista_imagenes["fondo_pantalla"])
imagen_fondo_juego = pygame.transform.scale(imagen_fondo_juego, (ancho_pantalla, alto_pantalla))

#FUENTES DE TEXTO
fuente_titulo_logo = pygame.font.Font("fonts/Press_Start_2P/PressStart2P-Regular.ttf", 32)
fuente_texto = pygame.font.Font("fonts/Press_Start_2P/PressStart2P-Regular.ttf", 12)

#ICONO DE FONDO
ancho_imagen_logo = int(ancho_pantalla * 0.25)
alto_imagen_logo = int(alto_pantalla * 0.15)
imagen_logo = pygame.image.load(lista_imagenes["icono_pantalla"])
imagen_logo = pygame.transform.scale(imagen_logo, (ancho_imagen_logo, alto_imagen_logo))
texto_imagen_logo = fuente_titulo_logo.render("BUSCAVIRUS", True, colores["blanco"])

#CREACION DE RECTANGULOS Y FUENTES PARA BOTONES DEL MENU
ancho_boton = 220
alto_boton = 50

ancho_boton_reiniciar_y_sonido = 40
alto_boton_reiniciar_y_sonido = 40

ancho_imagen_sonido = 30
alto_imagen_sonido = 30

ancho_boton_timer_y_bandera = 80
alto_boton_timer_y_bandera = 50


rectangulo_boton_jugar = pygame.Rect(int((ancho_pantalla / 2) - (ancho_boton / 2)), int(alto_pantalla * 0.32), ancho_boton, alto_boton)
texto_boton_jugar = fuente_texto.render("JUGAR", True, colores["negro"])

rectangulo_boton_dificultad = pygame.Rect(int((ancho_pantalla / 2) - (ancho_boton / 2)), int(alto_pantalla * 0.44), ancho_boton, alto_boton)
texto_boton_dificultad = fuente_texto.render("DIFICULTAD:FACIL", True, colores["negro"])

rectangulo_boton_puntajes = pygame.Rect(int((ancho_pantalla / 2) - (ancho_boton / 2)), int(alto_pantalla * 0.56), ancho_boton, alto_boton)
texto_boton_puntajes = fuente_texto.render("PUNTAJES", True, colores["negro"])

rectangulo_boton_salir = pygame.Rect(int((ancho_pantalla / 2) - (ancho_boton / 2)), int(alto_pantalla * 0.68), ancho_boton, alto_boton)
texto_boton_salir = fuente_texto.render("SALIR", True, colores["negro"])

# BOTONES PARA PANTALLA DEL JUEGO Y PUNTAJES
rectangulo_boton_volver = pygame.Rect(int((ancho_pantalla / 2) - (ancho_boton / 2)), int(alto_pantalla * 0.90), ancho_boton, alto_boton)
texto_boton_volver = fuente_texto.render("VOLVER AL MENU", True, colores["negro"])

rectangulo_boton_reiniciar = pygame.Rect(int((ancho_pantalla / 2) - (ancho_boton_reiniciar_y_sonido / 2)), int(alto_pantalla * 0.05), ancho_boton_reiniciar_y_sonido, alto_boton_reiniciar_y_sonido)
texto_boton_reiniciar = fuente_texto.render("R", True, colores["negro"])

rectangulo_boton_timer = pygame.Rect(int(ancho_pantalla * 0.875) - ancho_boton_timer_y_bandera, int(alto_pantalla * 0.05), ancho_boton_timer_y_bandera, alto_boton_timer_y_bandera)

rectangulo_boton_contador_banderas = pygame.Rect(int(ancho_pantalla * 0.125), int(alto_pantalla * 0.05), ancho_boton_timer_y_bandera, alto_boton_timer_y_bandera)

rectangulo_boton_sonido = pygame.Rect(int((ancho_pantalla * 0.0625) - (ancho_boton_reiniciar_y_sonido / 2)), int(rectangulo_boton_volver.centery - (alto_boton_reiniciar_y_sonido / 2)), ancho_boton_reiniciar_y_sonido, alto_boton_reiniciar_y_sonido)

# BOTONES PARA PANTALLA DE INGRESO DE NOMBRE
rectangulo_boton_guardar = pygame.Rect(int((ancho_pantalla / 2) - (ancho_boton / 2)), int(alto_pantalla * 0.65), ancho_boton, alto_boton)
boton_guardar = fuente_texto.render("GUARDAR", True, colores["negro"])

# INPUT DE NOMBRE
rectangulo_input_nombre = pygame.Rect(int((ancho_pantalla / 2) - (ancho_boton / 2)), int(alto_pantalla * 0.45), ancho_boton, alto_boton)

#CREACION DE BANDERA DE PANTALLAS
pantalla_menu = True
pantalla_juego = False
pantalla_puntajes = False
pantalla_victoria = False
                               
#CREACION DE HOVER COLOR
bandera_hover_jugar = False
bandera_hover_dificultad = False
bandera_hover_puntajes = False
bandera_hover_salir = False
bandera_hover_reiniciar = False
bandera_hover_volver = False
bandera_hover_sonido = False

#BANDERA IMAGEN SONIDO
bandera_sonido_fondo = True
bandera_sonido_game_over = False
bandera_sonido_victoria = False

#CREACION DEL MODO DE DIFICULTAD
modo_dificultad = 1  # 1 es facil, 2 es facil, 3 es dificil

#DECLARAMOS UNA VARIABLE QUE CUENTE LA CANTIDAD DE CLICKS QUE HICIMOS EN ALGUNO DE LAS CELDAS
contador_de_clicks_en_celdas = 0

#LISTAS QUE ACUMULAN TODAS LAS CELDAS A DESPINTAR Y CON BANDERA
lista_celdas_a_despintar = []
lista_celdas_con_bandera = []

#DECLARO UNA VARIABLE QUE FINALICE EL JUEGO EN CASO DE QUE HAYA UNA BOMBA
bandera_game_over = False

#GENERAMOS UNA VARIABLE BANDERA QUE EN CASO DE CLICKEAR EN UNA BOMBA NO SE PUEDA DESPINTAR MAS
bandera_seguir_pintando = True

#VARIABLES Y EVENTOS PARA TIMER Y PUNTAJES
evento_segundo = pygame.USEREVENT + 1
pygame.time.set_timer(evento_segundo, 1000)
tiempo_actual_juego = 0
bandera_timer_iniciado = False

#VARIABLES PARA PANTALLA DE VICTORIA Y INGRESO DE NOMBRE
nombre_jugador_temporal = ""

# BUCLE PRINCIPAL DEL JUEGO                 
while True: 
    
    #IMAGEN PARA TODAS LAS PANTALLAS
    pantalla.blit(imagen_fondo_juego, (0, 0))

    cambiar_color_boton(bandera_hover_sonido, pantalla, colores["blanco"], colores["gris_oscuro"], rectangulo_boton_sonido)

    mostrar_imagen_sonido(bandera_sonido_fondo, ancho_imagen_sonido, alto_imagen_sonido, pantalla, rectangulo_boton_sonido)

    #TODOS LOS EVENTOS DEL JUEGO
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        elif evento.type == pygame.MOUSEBUTTONUP:
            if rectangulo_boton_sonido.collidepoint(evento.pos):
                if bandera_sonido_fondo == True:
                    bandera_sonido_fondo = False
                    configurar_volumen_sonido_de_fondo(bandera_sonido_fondo, 0)
                else:
                    bandera_sonido_fondo = True
                    configurar_volumen_sonido_de_fondo(bandera_sonido_fondo, 0)
                    
        elif evento.type == pygame.MOUSEMOTION:
            if rectangulo_boton_sonido.collidepoint(evento.pos):
                bandera_hover_sonido = True
            else:
                bandera_hover_sonido = False
        
        if pantalla_menu == True:
            if evento.type == pygame.MOUSEBUTTONUP:
                    if evento.button == 1:
                        if rectangulo_boton_jugar.collidepoint(evento.pos) == True:
                            pantalla_juego = True
                            pantalla_menu = False
                            bandera_creacion_matriz = True
                        elif rectangulo_boton_dificultad.collidepoint(evento.pos) == True:
                            modo_dificultad += 1
                        elif rectangulo_boton_puntajes.collidepoint(evento.pos) == True:
                            pantalla_puntajes = True
                            pantalla_menu = False
                        elif rectangulo_boton_salir.collidepoint(evento.pos) == True:
                            pygame.quit()
                            quit()

            elif evento.type == pygame.MOUSEMOTION:
                if rectangulo_boton_jugar.collidepoint(evento.pos) == True:
                    bandera_hover_jugar = True
                else:   
                    bandera_hover_jugar = False
                if rectangulo_boton_dificultad.collidepoint(evento.pos) == True:
                    bandera_hover_dificultad = True
                else:   
                    bandera_hover_dificultad = False
                if rectangulo_boton_puntajes.collidepoint(evento.pos) == True:
                    bandera_hover_puntajes = True
                else:   
                    bandera_hover_puntajes = False
                if rectangulo_boton_salir.collidepoint(evento.pos) == True:
                    bandera_hover_salir = True
                else:   
                    bandera_hover_salir = False
        
        elif pantalla_juego == True:
            if evento.type == pygame.MOUSEBUTTONUP:
                click_x_global, click_y_global = evento.pos

                # convertimos la posicion global del clic a una posicion relativa de la superficie del juego
                click_x_relativo_a_superficie = click_x_global - ubicacion_superficie_x_en_pantalla
                click_y_relativo_a_superficie = click_y_global - ubicacion_superficie_y_en_pantalla

                click_pos_relativa = (click_x_relativo_a_superficie, click_y_relativo_a_superficie)
                
                for i in range(len(matriz_de_celdas)):
                    for j in range(len(matriz_de_celdas[i])):
                        if matriz_de_celdas[i][j].collidepoint(click_pos_relativa):
                            contador_de_clicks_en_celdas += 1
                            if bandera_seguir_pintando == True:
                                if contador_de_clicks_en_celdas == 1:
                                    if evento.button == 1:
                                        asignar_celdas_vacias_adyacentes(i, j, lista_celdas_a_despintar, matriz_logica_juego, matriz_logica_banderas, matriz_logica_celdas_despintadas, contador_de_clicks_en_celdas)
                                
                                        asignar_bombas_aleatorios_a_matriz(matriz_logica_juego, lista_celdas_a_despintar, cantidad_de_minas)

                                    elif evento.button == 3:
                                        asignar_o_quitar_celdas_con_bandera(i, j, matriz_logica_banderas, lista_celdas_con_bandera, matriz_logica_celdas_despintadas, cantidad_de_banderas)

                                        asignar_bombas_aleatorios_a_matriz(matriz_logica_juego, lista_celdas_con_bandera, cantidad_de_minas)

                                    asignar_cantidad_de_bombas_adyacentes_en_superficie_de_celdas(matriz_logica_juego)

                                    asignar_celdas_vacias_adyacentes(i, j, lista_celdas_a_despintar, matriz_logica_juego, matriz_logica_banderas, matriz_logica_celdas_despintadas)

                                    bandera_timer_iniciado = True
                                else:
                                    if evento.button == 1:
                                        if matriz_logica_juego[i][j] == "X" and matriz_logica_banderas[i][j] == False:
                                            bandera_game_over = True
                                            bandera_sonido_game_over = True
                                            bandera_seguir_pintando = False
                                            lista_indices_minas = buscar_minas_en_superficie_del_juego(matriz_logica_juego)
                                            indice_i_mina = i
                                            indice_j_mina = j
                                        elif matriz_logica_juego[i][j] != "X" or matriz_logica_banderas[i][j] == False :
                                            asignar_celdas_vacias_adyacentes(i, j, lista_celdas_a_despintar, matriz_logica_juego, matriz_logica_banderas, matriz_logica_celdas_despintadas)
                                    elif evento.button == 3:
                                            asignar_o_quitar_celdas_con_bandera(i, j, matriz_logica_banderas, lista_celdas_con_bandera, matriz_logica_celdas_despintadas, cantidad_de_banderas)

                if evento.button == 1:
                    if rectangulo_boton_volver.collidepoint(evento.pos) or rectangulo_boton_reiniciar.collidepoint(evento.pos):
                        contador_de_clicks_en_celdas = 0
                        lista_celdas_a_despintar.clear()
                        lista_celdas_con_bandera.clear()
                        bandera_seguir_pintando = True
                        bandera_timer_iniciado = False
                        tiempo_actual_juego = 0
                        if rectangulo_boton_volver.collidepoint(evento.pos):
                            bandera_game_over = False
                            pantalla_juego = False
                            pantalla_menu = True
                            configurar_volumen_sonido_de_fondo(bandera_sonido_fondo, 0)
                        if rectangulo_boton_reiniciar.collidepoint(evento.pos):
                            if bandera_game_over == True:
                                configurar_volumen_sonido_de_fondo(bandera_sonido_fondo, 1)
                                bandera_game_over = False

            elif evento.type == pygame.MOUSEMOTION:
                if rectangulo_boton_volver.collidepoint(evento.pos):
                    bandera_hover_volver = True
                else:
                    bandera_hover_volver = False
                if rectangulo_boton_reiniciar.collidepoint(evento.pos):
                    bandera_hover_reiniciar = True
                else:
                    bandera_hover_reiniciar = False

            if bandera_timer_iniciado == True:
                if evento.type == evento_segundo:
                    tiempo_actual_juego += 1

        elif pantalla_puntajes == True:
            if evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:
                    if rectangulo_boton_volver.collidepoint(evento.pos) == True:
                        pantalla_puntajes = False
                        pantalla_menu = True
            elif evento.type == pygame.MOUSEMOTION:
                if rectangulo_boton_volver.collidepoint(evento.pos):
                    bandera_hover_volver = True
                else:
                    bandera_hover_volver = False
        
        elif pantalla_victoria == True:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if len(nombre_jugador_temporal) > 0:
                        puntos_jugador = determinar_cantidad_de_puntos_de_jugador(tiempo_actual_juego, modo_dificultad)
                        guardar_puntaje_en_archivo(nombre_jugador_temporal, puntos_jugador, tiempo_actual_juego, modo_dificultad)
                        pantalla_victoria = False
                        pantalla_menu = True
                        contador_de_clicks_en_celdas = 0
                        lista_celdas_a_despintar.clear()
                        lista_celdas_con_bandera.clear()
                        bandera_game_over = False
                        bandera_seguir_pintando = True
                        bandera_timer_iniciado = False
                        nombre_jugador_temporal = ""
                        tiempo_actual_juego = 0
                elif evento.key == pygame.K_BACKSPACE: # Tecla Borrar
                        nombre_jugador_temporal = nombre_jugador_temporal[0:-1]
                else:
                    letra = evento.unicode
                    if letra.isalpha() and len(nombre_jugador_temporal) < 10:
                        nombre_jugador_temporal += letra.upper()

    #PANTALLA DEL MENU
    if pantalla_menu == True:

        #CONFIGURAMOS LA MUSICA PARA SE EJECUTE UNA VEZ ESTEMOS DENTRO DEL MENU
        configurar_volumen_sonido_de_fondo(bandera_sonido_fondo, 0)

        #LOGO DEL JUEGO EN EL MENU PRINCIPAL
        logo = pantalla.blit(imagen_logo, ((centro_pantalla_x - (imagen_logo.get_width()) / 2), 60))
        pantalla.blit(texto_imagen_logo, (logo.centerx - (texto_imagen_logo.get_width() / 2), logo.bottom - texto_imagen_logo.get_height()))
        
        #DIBUJAMOS LOS RECTANGULOS CON SUS RESPECTIVOS HOVER
        cambiar_color_boton(bandera_hover_jugar, pantalla, colores["blanco"], colores["gris_oscuro"], rectangulo_boton_jugar)

        cambiar_color_boton(bandera_hover_dificultad, pantalla, colores["blanco"], colores["gris_oscuro"], rectangulo_boton_dificultad)

        cambiar_color_boton(bandera_hover_puntajes, pantalla, colores["blanco"], colores["gris_oscuro"], rectangulo_boton_puntajes)

        cambiar_color_boton(bandera_hover_salir, pantalla, colores["blanco"], colores["gris_oscuro"], rectangulo_boton_salir)
        

        #APLICAMOS LOGICA DEL BOTON DIFICULTAD CON SU TEXTO
        if modo_dificultad == 1:
            texto_boton_dificultad = fuente_texto.render("DIFICULTAD:FACIL", True, colores["negro"])
        elif modo_dificultad == 2:
            texto_boton_dificultad = fuente_texto.render("DIFICULTAD:NORMAL", True, colores["negro"])
        elif modo_dificultad == 3:      
            texto_boton_dificultad = fuente_texto.render("DIFICULTAD:DIFICIL", True, colores["negro"])
        else:
            modo_dificultad = 1

        #INSERTAMOS LOS TEXTOS EN LOS BOTONES DEL MENU 
        pantalla.blit(texto_boton_jugar, (rectangulo_boton_jugar.centerx - (texto_boton_jugar.get_width() / 2), (rectangulo_boton_jugar.centery - (texto_boton_jugar.get_height() / 2))))

        pantalla.blit(texto_boton_dificultad, (rectangulo_boton_dificultad.centerx - (texto_boton_dificultad.get_width() / 2), (rectangulo_boton_dificultad.centery - (texto_boton_dificultad.get_height() / 2))))
        
        pantalla.blit(texto_boton_puntajes, (rectangulo_boton_puntajes.centerx - (texto_boton_puntajes.get_width() / 2), (rectangulo_boton_puntajes.centery - (texto_boton_puntajes.get_height() / 2))))

        pantalla.blit(texto_boton_salir, (rectangulo_boton_salir.centerx - (texto_boton_salir.get_width() / 2), (rectangulo_boton_salir.centery - (texto_boton_salir.get_height() / 2))))
    
    #PANTALLA DEL JUEGO
    if pantalla_juego == True:

        #CONFIGURAMOS LA MUSICA PARA SE EJECUTE UNA VEZ ESTEMOS DENTRO DEL JUEGO
        configurar_volumen_sonido_de_fondo(bandera_sonido_fondo, 0)
        
        # DECLARAMOS LAS VARIABLES DE LA CANTIDAD DE CELDAS EN FILAS Y COLUMNAS Y LAS MINAS
        cantidad_filas_celdas, cantidad_columnas_celdas, cantidad_de_minas, cantidad_de_banderas = determinar_cant_filas_columns_minas_banderas(modo_dificultad)

        
        #CREACION DE SUPERFICIE JUEGO
        #para que la superificie sea justa, nos vamos a basar en en el acho y alto de las celdas
        #CREAMOS LA CELDA CON SU RESPECTIVO TAMAÑO SEGUN LA DIFICULTAD DEL JUEGO
        
        ancho_celda = (ancho_pantalla * 0.75) // cantidad_columnas_celdas
        alto_celda = (alto_pantalla * 0.75) // cantidad_filas_celdas

        #ahora si generamos el alto y ancho de la superficie
        ancho_superficie = ancho_celda * cantidad_columnas_celdas
        alto_superficie = alto_celda * cantidad_filas_celdas
        centro_superficie_x = ancho_superficie / 2
        centro_superficie_y = alto_superficie / 2

        superficie_juego = pygame.Surface((ancho_superficie, alto_superficie))

        #generamos la ubicacion de donde va a estar la superficie en la pantalla
        ubicacion_superficie_x_en_pantalla = centro_pantalla_x - centro_superficie_x
        ubicacion_superficie_y_en_pantalla = centro_pantalla_y - centro_superficie_y

        #el color de la superficie se tiene que ejecutar antes de mostrarla en pantalla
        superficie_juego.fill(colores["negro"])

        #GENERAMOS TODAS LAS CELDAS OCULTAS DEL JUEGO y la dibujamos en la superficie
        matriz_de_celdas = generar_cuadricula_de_celdas_ocultas_en_superficie(cantidad_filas_celdas, cantidad_columnas_celdas, ancho_celda, alto_celda, superficie_juego)

        #GENERAMOS UNA MATRIZ LOGICA DE LOS VALORES Y DE BANDERAS PARA IR CONTROLANDO LA PARTIDA (SOLAMENTE SE TIENE QUE CREAR UNA VEZ POR PARTIDA)
        if contador_de_clicks_en_celdas == 0:
            matriz_logica_juego = generar_matriz(cantidad_filas_celdas, cantidad_columnas_celdas, 0)
            matriz_logica_banderas = generar_matriz(cantidad_filas_celdas, cantidad_columnas_celdas, False)
            matriz_logica_celdas_despintadas = generar_matriz(cantidad_filas_celdas, cantidad_columnas_celdas, False)
        

        # DIBUJAR BOTONES CON SUS RESPECTIVOS HOVER
        cambiar_color_boton(bandera_hover_volver, pantalla, colores["blanco"], colores["gris_oscuro"], rectangulo_boton_volver)

        cambiar_color_boton(bandera_hover_reiniciar, pantalla, colores["blanco"], colores["gris_oscuro"], rectangulo_boton_reiniciar)
        
        pygame.draw.rect(pantalla, colores["negro"], rectangulo_boton_timer)

        pygame.draw.rect(pantalla, colores["negro"], rectangulo_boton_contador_banderas)
        

        mostrar_celdas_con_bandera(lista_celdas_con_bandera, matriz_logica_banderas, matriz_de_celdas, ancho_celda, alto_celda, superficie_juego)

        mostrar_celdas_vacias_adyacentes(lista_celdas_a_despintar, matriz_logica_juego, matriz_de_celdas, ancho_celda, alto_celda, superficie_juego)

        #ACTUALIZAR Y MOSTRAR TIMER
        
        if bandera_timer_iniciado == False:
            dibujar_timer_en_pantalla("00:00", fuente_texto, pantalla, rectangulo_boton_timer)
        
        if bandera_timer_iniciado == True and bandera_game_over == False and pantalla_victoria == False:
            tiempo_formateado = obtener_tiempo_formateado(tiempo_actual_juego)
        
            dibujar_timer_en_pantalla(tiempo_formateado, fuente_texto, pantalla, rectangulo_boton_timer)
        
        
        #VERIFICAR VICTORIA
        if bandera_game_over == False and pantalla_victoria == False:
            cantidad_total_celdas = cantidad_filas_celdas * cantidad_columnas_celdas
            if verificar_victoria(matriz_logica_celdas_despintadas, cantidad_total_celdas, cantidad_de_minas) == True:
                bandera_sonido_victoria = True
                pantalla_victoria = True
                pantalla_juego = False
        
        #VERIFICAMOS DERROTA Y MOSTRAMOS CUANTO TIEMPO FUE QUE HIZO
        if bandera_game_over == True:        
            mostrar_minas_en_superficie(indice_i_mina, indice_j_mina, lista_indices_minas, matriz_de_celdas, ancho_celda, alto_celda, superficie_juego)

            dibujar_timer_en_pantalla(tiempo_formateado, fuente_texto, pantalla, rectangulo_boton_timer)

            if bandera_sonido_game_over == True:
                reproducir_sonido_derrota(bandera_sonido_fondo, bandera_sonido_game_over)
                bandera_sonido_game_over = False


            
        #POR ULTIMO, DIBUJAMOS LA SUPERFICIE DE LA MATRIZ EN PANTALLA PARA QUE YA SE DIBUJE CON LOS RECTANGULOS DE LAS MINAS Y LOS BOTONES PARA REINICIAR Y VOLVER AL MENU
        pantalla.blit(superficie_juego, (ubicacion_superficie_x_en_pantalla, ubicacion_superficie_y_en_pantalla))
        
        pantalla.blit(texto_boton_volver, (rectangulo_boton_volver.centerx - (texto_boton_volver.get_width() / 2), rectangulo_boton_volver.centery - (texto_boton_volver.get_height() / 2)))

        pantalla.blit(texto_boton_reiniciar, (rectangulo_boton_reiniciar.centerx - (texto_boton_reiniciar.get_width() / 2), rectangulo_boton_reiniciar.centery - (texto_boton_reiniciar.get_height() / 2)))

        dibujar_contador_de_banderas_en_pantalla(cantidad_de_banderas, lista_celdas_con_bandera, fuente_texto, pantalla, rectangulo_boton_contador_banderas)
   
    #PANTALLA DE LOS PUNTAJES
    if pantalla_puntajes == True:

        #CONFIGURAMOS LA MUSICA PARA SE EJECUTE UNA VEZ ESTEMOS DENTRO DE LOS PUNTAJES 
        configurar_volumen_sonido_de_fondo(bandera_sonido_fondo, 0)
        
        #TÍTULO DE PUNTAJES
        titulo_puntajes = fuente_texto.render("TOP 10 PUNTAJES", True, colores["blanco"])
        pantalla.blit(titulo_puntajes, (centro_pantalla_x - (titulo_puntajes.get_width() / 2), 50))
        
        #OBTENER LOS MEJORES PUNTAJES

        puntajes = leer_puntajes_desde_archivo("puntajes.txt")

        ordenar_puntajes(puntajes)

        mejores_puntajes = obtener_top_10_puntajes(puntajes)
        
        #MOSTRAR CADA PUNTAJE
        dibujar_puntajes_en_pantalla(mejores_puntajes, fuente_texto, pantalla)
        

        #BOTON VOLVER
        cambiar_color_boton(bandera_hover_volver, pantalla, colores["blanco"], colores["gris_oscuro"], rectangulo_boton_volver)

        pantalla.blit(texto_boton_volver, (rectangulo_boton_volver.centerx - (texto_boton_volver.get_width() / 2), (rectangulo_boton_volver.centery - (texto_boton_volver.get_height() / 2))))

    #PANTALLA DE INGRESO DE NOMBRE 
    if pantalla_victoria == True:
        
        #REPRODUCIR SONIDO DE VICTORIA
        if bandera_sonido_victoria == True:
            reproducir_sonido_victoria(bandera_sonido_fondo, bandera_sonido_victoria)
            bandera_sonido_victoria = False

        #TEXTO DE VICTORIA
        texto_victoria = fuente_texto.render("¡GANASTE!", True, colores["amarillo"])
        pantalla.blit(texto_victoria, (centro_pantalla_x - (texto_victoria.get_width() / 2), centro_pantalla_y - 100))

        texto_instruccion = fuente_texto.render("ESCRIBE TU NOMBRE:", True, colores["blanco"])
        pantalla.blit(texto_instruccion, (centro_pantalla_x - (texto_instruccion.get_width() / 2), centro_pantalla_y - 50))
        
        texto_instruccion2 = fuente_texto.render("(SOLO LETRAS)", True, colores["blanco"])
        pantalla.blit(texto_instruccion2, (centro_pantalla_x - (texto_instruccion2.get_width() / 2), centro_pantalla_y - 20))
        

        if nombre_jugador_temporal == "":
            texto_mostrar = "_"
        else:
            texto_mostrar = nombre_jugador_temporal
        
        texto_nombre = fuente_texto.render(texto_mostrar, True, colores["amarillo"])
        pantalla.blit(texto_nombre, (centro_pantalla_x - (texto_nombre.get_width() / 2), centro_pantalla_y + 20))
        
        texto_enter = fuente_texto.render("PRESIONA ENTER PARA GUARDAR", True, colores["blanco"])

        pantalla.blit(texto_enter, (centro_pantalla_x - (texto_enter.get_width() / 2), centro_pantalla_y + 60))
    
    pygame.display.flip()