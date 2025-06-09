# El Laberinto del Gato y el Ratón

Es una simulación estratégica en Python puro que recrea un duelo mental entre un **ratón que escapa** y un **gato que persigue**, usando el algoritmo **Minimax** como núcleo de decisiones.  
Se desarrolla en un **tablero bidimensional con obstáculos**, donde cada turno es una batalla entre maximizar la evasión y minimizar la distancia.

## ¿Qué incluye el proyecto?

- Tablero dinámico con impresión visual en consola.
- Obstáculos generados aleatoriamente.
- Modos de juego:
  - IA vs IA
  - Jugador como Gato
  - Jugador como Ratón
- Implementación completa de Minimax con evaluación de estados y penalizaciones por repetición.
- Movimiento en 8 direcciones (diagonales incluidas).
- Reglas de finalización: captura, empate por repetición, o escape tras 20 turnos.

## Algoritmos e Inteligencia

- **Ratón Inteligente**: evalúa todos los movimientos posibles y simula los peores casos del gato para elegir la ruta más segura.
- **Gato Estratégico**: predice la mejor ruta del ratón y se posiciona para limitar su espacio de escape.
- **Minimax Recursivo**: árbol de decisiones con turnos alternados y profundidad variable.

## Lo que funcionó

- La visualización con emojis hizo el juego muy intuitivo.
- El ratón logró evadir con éxito cuando tenía suficiente espacio y la IA ajustó bien la estrategia.
- La penalización cuadrática evitó bucles infinitos.

## Lo que fue un desastre (al principio)

- Las paredes mal colocadas.
- La IA se repetía demasiado hasta que se aplicaron penalizaciones por estados repetidos.
- El algoritmo Minimax sin una evaluación heurística era lento y predecible.

## ¡Ajá! Moment

Cuando comprendi como funciona la creacion de matrices y todo lo que conlleva, como moverse en la matriz y que la **distancia Chebyshev** era ideal para medir escape/amenaza en movimiento diagonal, todo encajó.  
La IA se volvió mucho más humana (¡o más ratónida!).

## Aprendizajes

- Creacion de una matriz
- Implementación de Minimax desde cero en Python, adaptado a un juego personalizado.
- Balanceo del juego ajustando profundidad, condiciones de victoria y límites de turnos para evitar sesgos.
- Corrección de errores lógicos frecuentes, como repeticiones de movimientos o bucles infinitos.
- Registro de partidas en una base de datos para analizar jugadas, resultados y comportamientos.
- Aplicación de programación orientada a objetos y lógica de IA para anticipar decisiones del oponente.

## Cómo usarlo

desde la terminal, ejecuta: 
```bash

python challence_1_ratonygato.py
