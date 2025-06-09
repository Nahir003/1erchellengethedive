# El Laberinto del Gato y el Ratón

Desarrollé una simulación estratégica en Python puro, donde un ratón intenta escapar y un gato lo persigue en un tablero con obstáculos. Usé el algoritmo Minimax como núcleo de decisión para que ambos personajes actúen con inteligencia en cada turno.

## ¿Qué hice en este proyecto?
Programé un tablero dinámico que se imprime en consola.
Incorporé generación aleatoria de obstáculos en cada partida.
Implementé tres modos de juego:
IA vs IA (totalmente automatizado)
Jugador como Gato
Jugador como Ratón
Desarrollé una versión funcional de Minimax con penalizaciones por repetición y evaluación de estado.
Habilité movimientos en ocho direcciones, incluyendo diagonales.
Establecí reglas claras para finalizar el juego: captura, empate por repetición o escape tras 20 turnos.

## Cómo pensé la inteligencia artificial
Hice que el ratón evalúe todos los movimientos posibles simulando los peores escenarios para elegir la ruta más segura.
Hice que el gato anticipe al ratón, bloqueando caminos y minimizando su espacio de escape.
Construí un Minimax recursivo con turnos alternados y profundidad configurable.

## Lo que funcionó bien
La lógica de evasión del ratón fue efectiva cuando el tablero tenía espacio suficiente.
La penalización cuadrática por repetición evitó bucles infinitos en IA vs IA.
La visualización en consola permitió entender el juego en tiempo real de forma clara.

## Lo que no funcionó al inicio
Los obstáculos mal ubicados hacían que las partidas fueran injustas o imposibles.
La IA quedaba atrapada en ciclos hasta que implementé control de estados repetidos.
Minimax sin evaluación heurística resultó lento y predecible, así que desarrollé una mejor función de evaluación.

## Lo que aprendí
A crear y recorrer matrices de forma eficiente.
A implementar el algoritmo Minimax desde cero, adaptándolo a reglas personalizadas.
A ajustar profundidad, condiciones de victoria y límites de turnos para balancear el juego.
A corregir errores de lógica como repeticiones, estados inválidos y condiciones de empate.
A registrar cada jugada y resultado en una base de datos para futuros análisis.
A usar programación orientada a objetos para estructurar todo el sistema de juego e IA.

## Cómo ejecutar el juego
Desde la terminal, simplemente correr:

''bash
python challence_1_ratonygato.py
