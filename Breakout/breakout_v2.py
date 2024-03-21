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

# Sonstige einstellungen
paddle_speed = 20
paddle_y = window_height * 0.9

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

    def hits_side_of_window(self):
        return self.rect.left <= 0 or self.rect.right >= window_width

    def hits_top_of_window(self):
        return self.rect.top <= 0

    def is_below_paddle(self):
        return self.rect.center[1] > paddle_y

    def stop(self):
        self.direction = (0, 0)

    def move(self):
        new_x = self.rect.center[0] + self.direction[0]
        new_y = self.rect.center[1] + self.direction[1]
        self.rect.center = (new_x, new_y)

    def flip_x_direction(self):
        new_x_direction = self.direction[0] * -1
        new_y_direction = self.direction[1]
        self.direction = (new_x_direction, new_y_direction)

    def flip_y_direction(self):
        new_x_direction = self.direction[0]
        new_y_direction = self.direction[1] * -1
        self.direction = (new_x_direction, new_y_direction)


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/49-Breakout-Tiles.png')
        self.image = pygame.transform.scale(self.image, (150, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def left(self):
        new_x = self.rect.center[0] - paddle_speed
        new_y = self.rect.center[1]
        self.rect.center = (new_x, new_y)

    def right(self):
        new_x = self.rect.center[0] + paddle_speed
        new_y = self.rect.center[1]
        self.rect.center = (new_x, new_y)


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/01-Breakout-Tiles.png')
        self.image = pygame.transform.scale(self.image, (150, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


ball = Ball(500, 300)
balls = pygame.sprite.Group()
balls.add(ball)

paddle = Paddle(window_width / 2, paddle_y)
paddles = pygame.sprite.Group(paddle)

blocks = pygame.sprite.Group()
blocks.add([
    Block(100, 50),
    Block(250, 50),
    Block(400, 50),
    Block(550, 50),
    Block(700, 50),

    Block(100, 90),
    Block(250, 90),
    Block(400, 90),
    Block(550, 90),
    Block(700, 90),

    Block(100, 130),
    Block(250, 130),
    Block(400, 130),
    Block(550, 130),
    Block(700, 130),

    Block(100, 170),
    Block(250, 170),
    Block(400, 170),
    Block(550, 170),
    Block(700, 170),

    Block(100, 210),
    Block(250, 210),
    Block(400, 210),
    Block(550, 210),
    Block(700, 210),
])

run = True
while run:
    clock.tick(100)
    screen.fill(background_color)

    ball.move()
    balls.update()
    balls.draw(screen)

    paddles.update()
    paddles.draw(screen)

    blocks.update()
    blocks.draw(screen)

    if ball.hits_top_of_window():
        ball.flip_y_direction()

    if ball.hits_side_of_window():
        ball.flip_x_direction()

    if ball.is_below_paddle():
        background_color = red
        paddle_speed = 0
        ball.stop()

    ball_hits_paddle = pygame.sprite.spritecollide(ball, paddles, False)
    if ball_hits_paddle:
        ball.flip_y_direction()

    ball_hits_block = pygame.sprite.spritecollide(ball, blocks, True)
    if ball_hits_block:
        print(ball_hits_block)
        ball.flip_y_direction()


    # Die Änderungen im Spielfenster sichtbar machen.
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.left()
            if event.key == pygame.K_RIGHT:
                paddle.right()

