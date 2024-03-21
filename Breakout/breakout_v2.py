import pygame

# Spiel initialisieren
pygame.init()

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


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/58-Breakout-Tiles.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = (-1, -2)

    def update_position(self):
        if self.rect.left <= 0 or self.rect.right >= window_width:
            new_x_direction = self.direction[0] * -1
            new_y_direction = self.direction[1]
            self.direction = (new_x_direction, new_y_direction)

        if self.rect.top <= 0 or self.rect.bottom >= window_height:
            new_x_direction = self.direction[0]
            new_y_direction = self.direction[1] * -1
            self.direction = (new_x_direction, new_y_direction)

        new_x = self.rect.center[0] + self.direction[0]
        new_y = self.rect.center[1] + self.direction[1]
        self.rect.center = (new_x, new_y)


ball = Ball(500, 300)
balls = pygame.sprite.Group()
balls.add(ball)


run = True
while run:
    clock.tick(100)
    screen.fill(background_color)

    ball.update_position()
    balls.update()
    balls.draw(screen)

    # Die Änderungen im Spielfenster sichtbar machen.
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
