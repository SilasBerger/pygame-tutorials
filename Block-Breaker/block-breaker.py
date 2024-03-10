import pygame

# Spiel initialisieren
pygame.init()  

# Einstellungen für das Fenster
fenster_breite = 400
fenster_hoehe = 300

# Einstellungen für die Farben
schwarz = pygame.color.Color(0, 0, 0)
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

ball_geschwindigkeit = 10
ball_richtung = [-(ball_geschwindigkeit / 2), -ball_geschwindigkeit]

# Einstellungen und Startposition Paddel
paddel_breite = 100
paddel_hoehe = 10
paddel_startposition_x = (fenster_breite / 2) - (paddel_breite / 2)
paddel_startposition_y = (fenster_hoehe * 0.9) - (paddel_hoehe / 2)
paddel = [paddel_startposition_x, paddel_startposition_y, paddel_breite, paddel_hoehe]

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
    kollisionsbox = [ball[0] - (ball_radius / 2), ball[1] - (ball_radius / 2), 2 * ball_radius, 2 * ball_radius]
    kollision_mit_paddel = pygame.rect.Rect(paddel).colliderect(kollisionsbox)
    
    if kollision_links or kollision_rechts:
        ball_richtung[0] = ball_richtung[0] * -1  
    elif kollision_oben or kollision_unten or kollision_mit_paddel:
        ball_richtung[1] = ball_richtung[1] * -1
    
    ball_x_neu = ball[0] + ball_richtung[0]
    ball_y_neu = ball[1] + ball_richtung[1]
    ball = [ball_x_neu, ball_y_neu]
    

while True:
    clock.tick(10)
    screen.fill(schwarz)
    
    pygame.draw.circle(screen, farbe_ball, ball, ball_radius)
    aktualisiere_ball_position()
    
    pygame.draw.rect(screen, farbe_paddel, paddel)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddel[0] = paddel[0] - paddel_bewegung_distanz
            if event.key == pygame.K_RIGHT:
                paddel[0] = paddel[0] + paddel_bewegung_distanz
