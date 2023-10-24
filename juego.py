import pygame
import random

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
window_width = 1000
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Juego de Cartas con Preguntas")

# Colores
WHITE = (255, 255, 255)

# Fuentes
font = pygame.font.Font(None, 36)

# Preguntas y respuestas
preguntas_respuestas = {
    "¿Cuál es el símbolo químico del agua?": {
        "opciones": ["H2O", "CO2", "O2"],
        "correcta": "H2O"
    },
    "¿Cuál es el número atómico del oxígeno?": {
        "opciones": ["8", "16", "32"],
        "correcta": "8"
    },
    "¿Cuál es el gas noble más abundante en la atmósfera?": {
        "opciones": ["Neón", "Helio", "Argón"],
        "correcta": "Neón"
    },
    "¿Cuál es el símbolo químico del hidrógeno?": {
        "opciones": ["H", "He", "O"],
        "correcta": "H"
    },
    "¿Cuál es el número atómico del carbono?": {
        "opciones": ["6", "12", "22"],
        "correcta": "6"
    },
    "¿Qué elemento químico forma la mayor parte de la atmósfera de la Tierra?": {
        "opciones": ["Nitrógeno", "Oxígeno", "Dióxido de carbono"],
        "correcta": "Nitrógeno"
    },
    "¿Cuál es el elemento químico más reactivo?": {
        "opciones": ["Fluor", "Oxígeno", "Potasio"],
        "correcta": "Fluor"
    },
    "¿Qué gas es conocido como el gas de la risa?": {
        "opciones": ["Óxido nitroso", "Metano", "Dióxido de carbono"],
        "correcta": "Óxido nitroso"
    },
    "¿Cuál es el proceso químico de combinar oxígeno con una sustancia?": {
        "opciones": ["Oxidación", "Fermentación", "Destilación"],
        "correcta": "Oxidación"
    },
    "¿Cuál es el compuesto químico comúnmente conocido como sal de mesa?": {
        "opciones": ["Cloruro de sodio", "Carbonato de calcio", "Sulfato de aluminio"],
        "correcta": "Cloruro de sodio"
    },
    "¿Cuál es el gas que las plantas toman del aire para llevar a cabo la fotosíntesis?": {
        "opciones": ["Dióxido de carbono", "Nitrógeno", "Oxígeno"],
        "correcta": "Dióxido de carbono"
    },
    "¿Cuál es el elemento químico más abundante en el cuerpo humano?": {
        "opciones": ["Oxígeno", "Hidrógeno", "Carbono"],
        "correcta": "Oxígeno"
    },
    "¿Cuál es el símbolo químico del agua?": {
        "opciones": ["H2O", "CO2", "O2"],
        "correcta": "H2O"
    },
    "¿Cuál es el número atómico del oxígeno?": {
        "opciones": ["8", "16", "32"],
        "correcta": "8"
    },
    "¿Cuál es el gas noble más abundante en la atmósfera?": {
        "opciones": ["Neón", "Helio", "Argón"],
        "correcta": "Neón"
    },
    "¿Qué elemento químico tiene el símbolo 'Fe'?": {
        "opciones": ["Hierro", "Plata", "Fluoruro"],
        "correcta": "Hierro"
    },
    "¿Cuál es el componente principal del gas natural?": {
        "opciones": ["Metano", "Etano", "Propano"],
        "correcta": "Metano"
    },
    "¿Cuál es el ácido presente en las bebidas gaseosas que les da su sabor característico?": {
        "opciones": ["Ácido carbónico", "Ácido acético", "Ácido cítrico"],
        "correcta": "Ácido carbónico"
    },
    "¿Qué gas es esencial para la respiración aeróbica en los seres vivos?": {
        "opciones": ["Oxígeno", "Dióxido de carbono", "Nitrógeno"],
        "correcta": "Oxígeno"
    },
    "¿Cuál es el metal más ligero en la tabla periódica?": {
        "opciones": ["Litio", "Sodio", "Potasio"],
        "correcta": "Litio"
    },
    "¿Cuál es el proceso químico de descomposición de sustancias orgánicas por acción de microorganismos?": {
        "opciones": ["Descomposición", "Fermentación", "Oxidación"],
        "correcta": "Fermentación"
    },
    "¿Cuál es el nombre químico del azúcar de mesa?": {
        "opciones": ["Sacarosa", "Glucosa", "Fructosa"],
        "correcta": "Sacarosa"
    },
    "¿Qué grupo de elementos químicos comparten propiedades similares y se encuentran en la misma columna de la tabla periódica?": {
        "opciones": ["Familia o grupo", "Período", "Isótopo"],
        "correcta": "Familia o grupo"
    },
    "¿Qué se llama a la cantidad de sustancia que contiene el mismo número de entidades elementales que átomos en 12 gramos de carbono-12?": {
        "opciones": ["Mol", "Átomo", "Elemento"],
        "correcta": "Mol"
    },
    "¿Cuál es el proceso químico que implica la unión de dos átomos de hidrógeno para formar una molécula de hidrógeno (H2)?": {
        "opciones": ["Hidrogenación", "Ionización", "Electrólisis"],
        "correcta": "Hidrogenación"
    },
    "¿Cuál es el ácido presente en el jugo de limón?": {
        "opciones": ["Ácido cítrico", "Ácido sulfúrico", "Ácido acético"],
        "correcta": "Ácido cítrico"
    },
    "¿Cuál es el símbolo químico del cloro?": {
        "opciones": ["Cl", "Co", "Cr"],
        "correcta": "Cl"
    },
    "¿Cuál es el elemento químico utilizado en las linternas y baterías recargables?": {
        "opciones": ["Litio", "Plomo", "Sodio"],
        "correcta": "Litio"
    },
    # Agrega más preguntas y respuestas aquí
}

# Estado del juego
vidas = 5
monedas = 0

# Función para mostrar pregunta
def mostrar_pregunta():
    pregunta, data_pregunta = random.choice(list(preguntas_respuestas.items()))
    opciones = data_pregunta["opciones"]
    respuesta_correcta = data_pregunta["correcta"]
    random.shuffle(opciones)  # Mezcla las opciones de respuesta
    return pregunta, opciones, respuesta_correcta

# Respuesta correcta fuera del bucle
pregunta_actual, opciones_actuales, respuesta_correcta = mostrar_pregunta()

# Bucle principal del juego
running = True
while running and vidas > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos

            for i, opcion in enumerate(opciones_actuales):
                # El centro vertical de la opción se corrige aquí
                y_option = window_height // 2 - 25 + i * 50
                if window_width // 2 - 100 <= x <= window_width // 2 + 100 and y_option <= y <= y_option + 50:
                    selected_option = opciones_actuales[i]
                    
                    if selected_option == respuesta_correcta:
                        monedas += 1
                    else:
                        vidas -= 1

                    pregunta_actual, opciones_actuales, respuesta_correcta = mostrar_pregunta()

    window.fill(WHITE)

    text = font.render(pregunta_actual, True, (0, 0, 0))
    text_rect = text.get_rect(center=(window_width // 2, window_height // 2 - 200))
    window.blit(text, text_rect)

    for i, opcion in enumerate(opciones_actuales):
        y_option = window_height // 2 - 25 + i * 50  # Corrección
        text = font.render(f"{chr(97 + i)}) {opcion}", True, (0, 0, 0))
        text_rect = text.get_rect(center=(window_width // 2, y_option))
        pygame.draw.rect(window, (200, 200, 200), (window_width // 2 - 100, y_option - 25, 200, 50), 2)
        window.blit(text, text_rect)

    vidas_text = font.render(f"Vidas: {vidas}", True, (0, 0, 0))
    window.blit(vidas_text, (10, 10))

    monedas_text = font.render(f"Monedas: {monedas}", True, (0, 0, 0))
    window.blit(monedas_text, (10, 50))

    pygame.display.flip()

# Limpia Pygame y sale
pygame.quit()
