import pygame

# Spiel initialisieren
pygame.init()

# Einstellungen für das Fenster
fenster_breite = 400
fenster_hoehe = 300

# Einstellungen für die Farben
schwarz = pygame.color.Color(0, 0, 0)
rot = pygame.color.Color(255, 0, 0)
farbe_ball = pygame.color.Color(255, 255, 255)
farbe_paddel = pygame.color.Color(255, 255, 255)

# Pygame-Fenster vorbereiten
pygame.display.set_caption("Block Breaker 🏆")
screen = pygame.display.set_mode([fenster_breite, fenster_hoehe])

# Zugriff auf die Uhr -> damit können wir die Geschwindigkeit des Spiels anpassen
clock = pygame.time.Clock()

# Einstellungen und Startposition Ball
ball_radius = 10
ball_startposition_x = (fenster_breite / 2)
ball_startposition_y = (fenster_hoehe / 2)
ball = [ball_startposition_x, ball_startposition_y]

ball_richtung = [-0.5, -1]

# Einstellungen und Startposition Paddel
paddel_breite = 100
paddel_hoehe = 10
paddel_start_x = (fenster_breite / 2) - (paddel_breite / 2)
paddel_y = (fenster_hoehe * 0.9) - (paddel_hoehe / 2)
paddel = [paddel_start_x, paddel_y, paddel_breite, paddel_hoehe]

# Sonstige Einstellungen
paddel_bewegung_distanz = 20


def aktualisiere_ball_position():
    global ball

    # Berechne Kollisionen mit der Wand
    kollision_links = ball[0] - ball_radius <= 0
    kollision_rechts = ball[0] + ball_radius >= fenster_breite
    kollision_oben = ball[1] - ball_radius <= 0
    kollision_unten = ball[1] + ball_radius >= fenster_hoehe

    # Berechne Kollisionen mit dem Paddel
    ball_mitte_x = ball[0]
    ball_mitte_y = ball[1]
    ball_box_x = ball_mitte_x - ball_radius
    ball_box_y = ball_mitte_y - ball_radius
    ball_box_breite = 2 * ball_radius
    kollisionsbox = [ball_box_x, ball_box_y, ball_box_breite, ball_box_breite]
    kollision_mit_paddel = pygame.rect.Rect(paddel).colliderect(kollisionsbox)

    # Passe Richtung an, falls eine Kollision entedeckt wurde
    if kollision_links or kollision_rechts:
        ball_richtung[0] = ball_richtung[0] * -1
    elif kollision_oben or kollision_unten or kollision_mit_paddel:
        ball_richtung[1] = ball_richtung[1] * -1

    # Berechne neue Position des Balls gemäss der Richtung
    ball = [ball[0] + ball_richtung[0], ball[1] + ball_richtung[1]]


spiel_aktiv = True
hintergrundfarbe = schwarz

while spiel_aktiv:
    clock.tick(100)
    screen.fill(hintergrundfarbe)

    pygame.draw.circle(screen, farbe_ball, ball, ball_radius)
    aktualisiere_ball_position()

    pygame.draw.rect(screen, farbe_paddel, paddel)

    if ball[1] > paddel_y:
        hintergrundfarbe = rot
        ball_richtung = [0, 0]
        paddel_bewegung_distanz = 0

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spiel_aktiv = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddel[0] = paddel[0] - paddel_bewegung_distanz
            if event.key == pygame.K_RIGHT:
                paddel[0] = paddel[0] + paddel_bewegung_distanz

