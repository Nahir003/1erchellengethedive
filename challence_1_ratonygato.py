import random

FILAS = 9
COLUMNAS = 12
MOVIMIENTOS_TODOS = [
    (-1, 0),  # arriba
    (1, 0),   # abajo
    (0, -1),  # izquierda
    (0, 1),   # derecha
    (-1, 1),  # arriba-derecha
    (1, 1),   # abajo-derecha
    (1, -1),  # abajo-izquierda
    (-1, -1)  # arriba-izquierda
]


def crear_tablero():
    """Crea una matriz (lista de listas), que será el tablero."""
    tablero = []
    for i in range(FILAS):
        fila = []
        for j in range(COLUMNAS):
            fila.append(".")
        tablero.append(fila)
    return tablero

def imprimir_tablero(tablero):
    """Imprime el tablero con íconos y bordes"""
    print("╔" + "══" * COLUMNAS + "╗")
    for fila in tablero:
        fila_dibujo = ""
        for celda in fila:
            if celda == ".":
                fila_dibujo += "⬜"
            elif celda == "R":                          
                fila_dibujo += "🐭"
            elif celda == "G":
                fila_dibujo += "🐱"
            elif celda == "X":
                fila_dibujo += "💥"
            elif celda == "█":
                fila_dibujo += "🧱"
        print("║" + fila_dibujo + "║")
    print("╚" + "══" * COLUMNAS + "╝")
    print()

    
def colocar_elemento(tablero, fila, columna, simbolo):
    """Coloca un símbolo en una posición válida del tablero."""
    if 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
        tablero[fila][columna] = simbolo

def limpiar_tablero(tablero):
    """Se usa para borrar los movimientos anteriores en cada turno"""  
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if tablero[i][j] not in ["█"]:
                tablero[i][j] = "."

def agregar_obstaculos(tablero, pos_raton, pos_gato, cantidad=16):
    """Agrega obstáculos en posiciones del tablero"""
    paredes_colocadas = 0
    intentos = 0
    max_intentos = 100

    while paredes_colocadas < cantidad and intentos < max_intentos:
        intentos += 1
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        posicion = (fila, columna)

        # Verificaciones:
        # verifica no poner una pared en la posicion del gato y/o del raton, si encuentra no pone
        if posicion in [pos_raton, pos_gato]:
            continue
        # verifica no poner una pared en la posicion de otra pared, si encuentra no pone
        if tablero[fila][columna] == "█":
            continue
        # No poner muy pegado a otras paredes:
        adyacentes = [(-1,0), (1,0), (0,-1), (0,1)]
        cerca = False
        for direccion_fila, direccion_columna in adyacentes:
            nueva_fila, nueva_columna = fila + direccion_fila, columna + direccion_columna
            #validador de que no salgas fuera del tablero ni pise una pared
            if 0 <= nueva_fila < FILAS and 0 <= nueva_columna < COLUMNAS:
                if tablero[nueva_fila][nueva_columna] == "█":
                    cerca = True
                    break
        if cerca:
            continue
        # Colocar la pared
        tablero[fila][columna] = "█"
        paredes_colocadas += 1

def validar_teclas(tecla):
    """Asegura que el jugador solo pueda usar teclas válidas (W/A/S/D/Q/E/Z/C)."""
    while tecla not in ["w", "a", "s", "d","q","e","z","c"]:
        print("Recuerda debes de ingresar las teclas para mover:\n"
                           "[W] arriba, [S] abajo, [A] izquierda, [D] derecha\n"
                           "[Q] arriba-izquierda, [E] arriba-derecha\n"
                           "[Z] abajo-izquierda, [C] abajo-derecha\n no otra!!")
        tecla = input("Ingrese la tecla nuevamente:")
    return tecla

def mover_con_tecla(posicion):
    """Mueve al objeto según la tecla que el jugador ingresa"""
    fila, columna = posicion
    movimientos = {
        'w': (-1, 0),
        's': (1, 0),
        'a': (0, -1),
        'd': (0, 1),
        'q': (-1, -1),
        'e': (-1, 1),
        'z': (1, -1),
        'c': (1, 1)
    }
    while True:
        tecla = validar_teclas(input("Movimiento del gato → Usá las teclas:\n"
                           "[W] arriba, [S] abajo, [A] izquierda, [D] derecha\n"
                           "[Q] arriba-izquierda, [E] arriba-derecha\n"
                           "[Z] abajo-izquierda, [C] abajo-derecha\n"
                           "Ingresá tu movimiento: ").lower())        
        if tecla in movimientos:
            direccion_fila, direccion_columna = movimientos[tecla]
            nueva_fila = fila + direccion_fila
            nueva_columna = columna + direccion_columna
            #validador de que no salgas fuera del tablero ni pise una pared
            if 0 <= nueva_fila < FILAS and 0 <= nueva_columna < COLUMNAS:
                if tablero[nueva_fila][nueva_columna] != "█":
                    return nueva_fila, nueva_columna
                else:
                    print("¡No puedes atravesar una pared!")
            else:
                print("¡Ese movimiento te saca del tablero!")


def validar_siono(texto):
    """Asegura que el jugador solo pueda usar las palabras "si" o "no"."""
    while texto!="si" and texto!="no":
        print("Recuerda debes de ingresar las palabras si o no, no otras!!")
        texto = input("Ingrese nuevamente:")
    return texto

def mover(posicion_actual, desplazamiento_fila, desplazamiento_columna):
    """Dado un punto (fila, columna) y un movimiento (dx, dy), devuelve la nueva posición.
    Ejemplo: Si estás en (3, 4) y el movimiento es (1, -1), terminás en (4, 3).."""
    return (posicion_actual[0] + desplazamiento_fila, posicion_actual[1] + desplazamiento_columna)

#Representa el número mínimo de movimientos necesarios en un tablero si se puede mover en todas las direcciones (incluyendo diagonales), como lo hace el rey en ajedrez
def distancia_Chebyshev(pos1, pos2):
    """Devuelve la distancia Chebyshev entre dos posiciones en una grilla."""
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))

def mejor_movimiento_raton(pos_raton, pos_gato):
    """Elige el movimiento más seguro para el ratón: el que maximiza su distancia mínima frente al gato."""
    fila_raton, columna_raton = pos_raton
    movimientos_posibles = MOVIMIENTOS_TODOS
    mejor_posicion = pos_raton
    
    #La mejor distancia posible que puede tener, asumiendo que el gato hace lo peor que me puede hacer.
    mejor_distancia_entre_peores_casos= float('-inf') #Es menos infinito pq se usa cuando querés buscar el máximo.Es el punto de partida más bajo posible, para que cualquier número real lo mejore."
    
    #recorre todas las direcciones posibles en las que el raton se puede mover
    for desplazamiento_fila, desplazamiento_columna in movimientos_posibles:
        # Calcula a que casilla llegaria el raton si se mueve en una direccion. 
        nueva_fila = fila_raton + desplazamiento_fila
        nueva_columna = columna_raton + desplazamiento_columna
        nueva_posicion_raton = (nueva_fila, nueva_columna)

        #validador de que la nueva posicion no salga fuera del tablero ni pise una pared
        if 0 <= nueva_fila < FILAS and 0 <= nueva_columna < COLUMNAS:
            if tablero[nueva_fila][nueva_columna] == "█":
                continue

            peor_distancia_posible = float('inf')#Es  infinito pq se usa cuando querés buscar el mínimo. Es el punto de partida más alto posible, para que cualquier número real lo supere hacia abajo."
            
            #recorre todas las direcciones posibles en las que el gato podria moverse desde su posición actual.
            for desplazamiento_gato_fila, desplazamiento_gato_col in movimientos_posibles:
                #calcula la nueva fila y columna a donde el gato llegaria si se moviera en esa dirección.
                nueva_fila_gato = posicion_gato[0] + desplazamiento_gato_fila
                nueva_columna_gato = posicion_gato[1] + desplazamiento_gato_col
                nueva_posicion_gato = (nueva_fila_gato, nueva_columna_gato)
                
                # se valida el movimiento del gato porque estamos en un nuevo contexto.
                # Aunque ya se valido al raton, ahora simula los posibles movimientos del gato,
                # asi que tambien se asegura que este dentro del tablero y no sean paredes.
                if 0 <= nueva_fila_gato < FILAS and 0 <= nueva_columna_gato < COLUMNAS:
                    if tablero[nueva_fila_gato][nueva_columna_gato] == "█":
                        continue

                    distancia_actual = distancia_Chebyshev(nueva_posicion_raton, nueva_posicion_gato)
                    #Se busca el peor escenario
                    if distancia_actual < peor_distancia_posible:
                        peor_distancia_posible = distancia_actual
                        
            # Si este movimiento del ratón tiene el mejor resultado en su peor escenario,
            # lo guardamos como la mejor opción hasta ahora.
            if peor_distancia_posible > mejor_distancia_entre_peores_casos:
                mejor_distancia_entre_peores_casos = peor_distancia_posible
                mejor_posicion = nueva_posicion_raton

    return mejor_posicion

def mejor_movimiento_gato(pos_gato, pos_raton):
    """Elige el movimiento que más limita las escapatorias del ratón."""
    fila_gato, columna_gato = pos_gato
    movimientos_posibles = MOVIMIENTOS_TODOS
    mejor_posicion = pos_gato
    
    #La menor distancia que el gato permitiria al raton, incluso si el raton escapa de la mejor forma posible
    menor_escape_posible_del_raton= float('inf')
    #recorre todas las direcciones posibles en las que el gato se puede mover
    for desplazamiento_gato_fila, desplazamiento_gato_col in movimientos_posibles:
        # Calcula a que casilla llegaria el gato si se mueve en una direccion.
        nueva_fila_gato = fila_gato + desplazamiento_gato_fila
        nueva_columna_gato = columna_gato + desplazamiento_gato_col
        nueva_posicion_gato = (nueva_fila_gato, nueva_columna_gato)
        #validador de que la nueva posicion no salga fuera del tablero ni pise una pared
        if 0 <= nueva_fila_gato < FILAS and 0 <= nueva_columna_gato < COLUMNAS:
            if tablero[nueva_fila_gato][nueva_columna_gato] == "█":
                continue

            mejor_escape_raton = float('inf')
            
            #recorre todas las direcciones posibles en las que el raton podria moverse desde su posición actual.
            for desplazamiento_raton_fila, desplazamiento_raton_col in movimientos_posibles:
                #calcula la nueva fila y columna a donde el raton llegaria si se moviera en esa dirección.
                nueva_fila_raton = posicion_raton[0] + desplazamiento_raton_fila
                nueva_columna_raton = posicion_raton[1] + desplazamiento_raton_col
                nueva_posicion_raton = (nueva_fila_raton, nueva_columna_raton)
                
                # se valida el movimiento del raton porque estamos en un nuevo contexto.
                # Aunque ya se valido al gato, ahora simula los posibles movimientos del raton,
                # asi que tambien se asegura que este dentro del tablero y no sean paredes.
                if 0 <= nueva_fila_raton < FILAS and 0 <= nueva_columna_raton < COLUMNAS:
                    if tablero[nueva_fila_raton][nueva_columna_raton] == "█":
                        continue

                    distancia_actual = distancia_Chebyshev(nueva_posicion_gato, nueva_posicion_raton)
                    
                    # Guardamos la menor distancia que el raton podria alcanzar si se escapa tras nuestro movimiento.
                    # El gato quiere minimizar ese mejor escape posible del raton.
                    if distancia_actual < mejor_escape_raton:
                        mejor_escape_raton = distancia_actual
            
            #decide cual es el mejor movimiento para el gato, basandose en cuanto puede limitar el escape del raton.                 
            if mejor_escape_raton == menor_escape_posible_del_raton:
                # Si este movimiento bloquea al ratón igual que el mejor hasta ahora, lo elegimos al azar en un 50%.
                if random.random() < 0.5:
                    mejor_posicion = nueva_posicion_gato
            # Si bloquea aún más, lo elegimos como el nuevo mejor movimiento del gato.
            elif mejor_escape_raton < menor_escape_posible_del_raton:
                menor_escape_posible_del_raton = mejor_escape_raton
                mejor_posicion = nueva_posicion_gato

    return mejor_posicion


def evaluar_estado(pos_raton, pos_gato):
    """ Asigna un puntaje al estado del juego. Cuanto más lejos está el ratón del gato, mejor para el ratón. Pero si hay repeticiones (movimientos ya hechos), penaliza."""
    estado = (pos_raton, pos_gato)
    repeticiones = historial_valores.get(estado, 0) #Si el estado ya existe como clave en el diccionario te devuelve su valor. Si el estado aún no existe devuelve 0.
    #Si el ratón fue atrapado el puntaje es -1000 (muy malo).
    if pos_raton == pos_gato:
        return -1000
    #Aca lo que pasa es que se calcula la distancia si no hay penalizacion te devuelve el valor de la distancia y si hay penalizacion te devuelve
    #un menor valor a la distancia ya que se le resta el valor de la penalizacion y el raton ve como que el gato esta mas cerca de el y le fuerza a moverse
    else:
        distancia = distancia_Chebyshev(pos_raton, pos_gato)
        penalizacion = repeticiones ** 2 * 10  
        recompensa_escape = distancia ** 2    # representa lo lejos que está el ratón del gato  
        return recompensa_escape - penalizacion

def es_pos_valida(pos):
    """Verifica si una posición está dentro del tablero y no es una pared."""
    fila, col = pos
    return (0 <= fila < FILAS and 0 <= col < COLUMNAS and tablero[fila][col] != "█")

def minimax(pos_raton, pos_gato, profundidad, turno_del_raton):
    """Busca la mejor jugada simulando los próximos movimientos, alternando entre ratón y gato."""
    #Si se llega al limite de profundidad o si el raton fue atrapado, entonces dejamos de explorar y simplemente evaluamos el estado actual del tablero.
    if profundidad == 0 or pos_raton == pos_gato:
        return evaluar_estado(pos_raton, pos_gato), None

    movimientos_posibles = MOVIMIENTOS_TODOS
    mejores_jugadas = []
    
    # Inicializamos el mejor valor como -inf si es el turno del raton (quiere maximizar),
    # o +inf si es el turno del gato (quiere minimizar).
    mejor_valor = float('-inf') if turno_del_raton else float('inf')

    # Simulamos todos los movimientos posibles del jugador actual (raton o gato).
    # Si el movimiento lleva a una posición inválida o con pared, se ignora.
    for fila, columna in movimientos_posibles:
        nueva_posicion = mover(pos_raton if turno_del_raton else pos_gato, fila, columna)
        if not es_pos_valida(nueva_posicion):
            continue
        
        #si es el turno del ratón, él es quien se mueve → se actualiza siguiente_pos_raton con la nueva_posicion.
        #Si no es su turno, el ratón no se mueve → se mantiene su posición actual.
        #Lo mismo para el gato, pero al revés.
        siguiente_pos_raton = nueva_posicion if turno_del_raton else pos_raton
        siguiente_pos_gato = nueva_posicion if not turno_del_raton else pos_gato

        #Simulamos el siguiente turno bajando la profundidad. Cuando llega a 0, se detiene la recursión.
        valor_jugada, _ = minimax(siguiente_pos_raton, siguiente_pos_gato, profundidad - 1, not turno_del_raton)

        #El ratón busca el valor más alto posible.
        #Si encuentra una jugada mejor que la anterior → la reemplaza
        #Si empata con la mejor hasta ahora → la añade como otra opción válida.
        if turno_del_raton:
            if valor_jugada > mejor_valor:
                mejor_valor = valor_jugada
                mejores_jugadas = [nueva_posicion] #se guarda en lista porque pueden haber varias jugadas igual de buenas. 
                                                #Después, en tu código se elige una de ellas al azar (como con random.choice(...)) para no ser predecible.
            elif valor_jugada == mejor_valor:
                mejores_jugadas.append(nueva_posicion)
        #el gato quiere acercarse al ratón, por eso minimiza el valor.
        #Si una jugada da un resultado más bajo → se guarda como la mejor.
        #Si hay empate con la mejor → también se guarda como opción válida.
        else:
            if valor_jugada < mejor_valor:
                mejor_valor = valor_jugada
                mejores_jugadas = [nueva_posicion]
            elif valor_jugada == mejor_valor:
                mejores_jugadas.append(nueva_posicion)

    #si hay jugadas validas elige una jugada al azar(Se elige una de ellas al azar (para evitar que siempre haga la misma jugada si hay empate) entre las mejores. 
    #Si no hay jugadas válidas, se queda en su posición actual.
    mejor_movimiento = random.choice(mejores_jugadas) if mejores_jugadas else (pos_raton if turno_del_raton else pos_gato)

    # Retornamos el valor óptimo y la jugada que lleva a ese resultado, luego de simular todos los turnos posibles.
    return mejor_valor, mejor_movimiento

# Código principal
modo = input("Seleccione modo: \n1) IA vs IA \n2) Ser el gato \n3) Ser el ratón \n4) Terminar el juego\n> ")
salir = False

while not salir:
    pos_raton = (0, 0)
    pos_gato = (8, 8)
    historial_valores = {}

    tablero = crear_tablero()
    agregar_obstaculos(tablero, pos_raton, pos_gato)
    colocar_elemento(tablero, *pos_raton, "R")
    colocar_elemento(tablero, *pos_gato, "G")
    imprimir_tablero(tablero)
    
    for turno in range(1, 21):
        limpiar_tablero(tablero)
        
        # Creamos una tupla ordenada del estado para que sea única sin importar quién se movió primero.
        #si importa pq en caso de que 2 estados se invertan no se tome como repeticion y se guarde como unico y no entre en una repeticion 
        estado_actual = tuple(sorted([pos_gato, pos_raton]))
        
        # Si el mismo estado del juego ocurre 3 veces, se fuerza un empate para evitar bucles infinitos.
        if estado_actual in historial_valores:
            historial_valores[estado_actual] += 1
        else:
            historial_valores[estado_actual] = 1

        if historial_valores[estado_actual] >= 3:
            print("Se repitió el mismo estado 3 veces. Empate forzado.")
            break

        if modo == "1":
            _, nuevo_gato = minimax(pos_raton, pos_gato, profundidad=3, turno_del_raton=False)
            if nuevo_gato is not None:
                pos_gato = nuevo_gato
           
            _, nuevo_raton = minimax(pos_raton, pos_gato, profundidad=6, turno_del_raton=True)
            if nuevo_raton is not None:
                pos_raton = nuevo_raton
            
        elif modo == "2":
            pos_gato = mover_con_tecla(pos_gato)
            _, nuevo_raton = minimax(pos_raton, pos_gato, profundidad=4, turno_del_raton=True)
            if nuevo_raton is not None:
                pos_raton = nuevo_raton
                
        elif modo == "3":
            _, nuevo_gato = minimax(pos_raton, pos_gato, profundidad=4, turno_del_raton=False)
            if nuevo_gato is not None:
                pos_gato = nuevo_gato
            pos_raton = mover_con_tecla(pos_raton)

        elif modo == "4":
            print("Terminando el juego...")
            salir = True
            break

        else:
            print("Modo inválido.")
            break

        if pos_raton == pos_gato:
            colocar_elemento(tablero, *pos_raton, "X")
            imprimir_tablero(tablero)
            print(f"Turno {turno}: ¡El gato atrapó al ratón!")
            break

        colocar_elemento(tablero, *pos_raton, "R")
        colocar_elemento(tablero, *pos_gato, "G")

        print(f"Turno {turno}")
        imprimir_tablero(tablero)

    else:
        print("El ratón logró escapar tras 20 turnos.")
        
    if modo != "4":
        continuar = validar_siono(input("¿Querés jugar otra vez? (si/no): ").lower())
        if continuar != "si":
            print("Gracias por jugar.")
            break
