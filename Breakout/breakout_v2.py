import pygame

# Farben definieren
black = pygame.color.Color('black')
red = pygame.color.Color('red')

# Farben zuweisen
background_color = black

# Einstellungen für das Fenster
window_width = 800
window_height = 600

# Pygame-Fenster vorbereiten
pygame.display.set_caption("Breakout 👾")
screen = pygame.display.set_mode([window_width, window_height])

# Zugriff auf die Uhr -> damit können wir die Geschwindigkeit des Spiels anpassen
clock = pygame.time.Clock()

game_active = True

while game_active:
    clock.tick(100)
    screen.fill(background_color)

    # Die Änderungen im Spielfenster sichtbar machen.
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
