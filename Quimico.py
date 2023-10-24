import pygame
import random

# Inicializa Pygame
pygame.init()

# Definir colores y fuentes
WHITE = (255, 255, 255)
font = pygame.font.Font(None, 36)

# Definir ventana
window_width = 1000
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Alchemist - Juego de Cartas con Preguntas")

# Inicializar variables globales
player_name = ""  # Variable para almacenar el nombre del jugador
player_coins = 0  # Variable para almacenar las monedas del jugador
questions = {
    "¿Cuál es el símbolo químico del agua?": {
        "opciones": ["H2O", "CO2", "O2"],
        "correcta": "H2O"
    },
    # Agrega más preguntas y respuestas aquí
}
ranking = []  # Lista para almacenar el ranking de jugadores
getting_name = False  # Variable booleana para controlar la entrada del nombre
game_started = False  # Variable para rastrear si el juego ha comenzado

# Definir función para mostrar el menú principal
def mostrar_menu():
    # Limpia la pantalla
    window.fill(WHITE)

    # Muestra el título del juego
    text = font.render("Bienvenido Alchemist", True, (0, 0, 0))
    text_rect = text.get_rect(center=(window_width // 2, window_height // 2 - 100))
    window.blit(text, text_rect)

    # Muestra las opciones del menú
    opciones = ["Comenzar", "Ver Tabla de Ranking", "Salir"]
    y = window_height // 2
    for i, opcion in enumerate(opciones):
        text = font.render(opcion, True, (0, 0, 0))
        text_rect = text.get_rect(center=(window_width // 2, y))
        window.blit(text, text_rect)
        y += 50

    pygame.display.flip()

# Definir función para mostrar preguntas y respuestas
def mostrar_preguntas():
    # Reiniciar las vidas y las monedas
    vidas = 5
    player_coins = 0

    while vidas > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        window.fill(WHITE)

        # Mostrar pregunta y opciones en un recuadro
        pregunta, data_pregunta = random.choice(list(questions.items()))
        opciones = data_pregunta["opciones"]
        respuesta_correcta = data_pregunta["correcta"]
        random.shuffle(opciones)

        text = font.render(pregunta, True, (0, 0, 0))
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2 - 200))
        window.blit(text, text_rect)

        opciones_rect = pygame.Rect(0, 0, window_width // 2, window_height // 2)
        opciones_rect.center = (window_width // 2, window_height // 2)
        pygame.draw.rect(window, (200, 200, 200), opciones_rect, 2)

        y = opciones_rect.top + 20
        for i, opcion in enumerate(opciones):
            text = font.render(f"{chr(97 + i)}) {opcion}", True, (0, 0, 0))
            text_rect = text.get_rect(center=(opciones_rect.centerx, y))
            window.blit(text, text_rect)
            y += 50

        # Mostrar contador de vidas y monedas
        vidas_text = font.render(f"Vidas: {vidas}", True, (0, 0, 0))
        window.blit(vidas_text, (10, 10))

        monedas_text = font.render(f"Monedas: {player_coins}", True, (0, 0, 0))
        window.blit(monedas_text, (10, 50))

        pygame.display.flip()

        # Lógica para que el jugador elija una respuesta
        respuesta_elegida = None
        while respuesta_elegida is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.K_a <= event.key <= pygame.K_c:
                        respuesta_elegida = chr(event.key)

        if respuesta_elegida == respuesta_correcta:
            player_coins += 1
        else:
            vidas -= 1

    # Guardar el progreso en el ranking
    ranking.append((player_name, player_coins))
    ranking.sort(key=lambda x: x[1], reverse=True)

    mostrar_menu()

# Definir función para mostrar la tabla de ranking
def mostrar_ranking():
    window.fill(WHITE)
    y = window_height // 2 - 50
    for i, (name, coins) in enumerate(ranking):
        text = font.render(f"{i + 1}. {name}: {coins} monedas", True, (0, 0, 0))
        text_rect = text.get_rect(center=(window_width // 2, y))
        window.blit(text, text_rect)
        y += 50
    pygame.display.flip()

# Bucle principal del juego
mostrar_menu()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if window_width // 2 - 100 <= x <= window_width // 2 + 100:
                if window_height // 2 - 50 <= y <= window_height // 2:
                    # Opción "Comenzar" seleccionada
                    if not getting_name and not game_started:
                        getting_name = True  # Habilita la entrada del nombre
                elif window_height // 2 + 0 <= y <= window_height // 2 + 50:
                    # Opción "Ver Tabla de Ranking" seleccionada
                    if not getting_name and not game_started:
                        mostrar_ranking()
                elif window_height // 2 + 50 <= y <= window_height // 2 + 100:
                    # Opción "Salir" seleccionada
                    if not getting_name and not game_started:
                        pygame.quit()
                        exit()
    if getting_name:
        # Dentro del bucle principal, mostrar el campo para ingresar el nombre
        window.fill(WHITE)
        input_text = font.render(f"Nombre: {player_name}", True, (0, 0, 0))
        input_rect = input_text.get_rect(center=(window_width // 2, window_height // 2))
        pygame.draw.rect(window, (200, 200, 200), input_rect, 2)
        window.blit(input_text, input_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    getting_name = False  # Finaliza la entrada del nombre
                    game_started = True  # Comienza el juego
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]  # Borra el último carácter
                else:
                    player_name += event.unicode  # Agrega caracteres al nombre

    if game_started:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Aquí puedes manejar eventos adicionales, por ejemplo, clics en opciones de preguntas.
            # Implementa lógica para procesar la selección del jugador.

        mostrar_preguntas()


