import pygame
from random import choice

# Pong

pygame.init()
screen_height = 800
screen_width = 600

screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load("Ball.png"))

# First paddle
first_pong_paddle = pygame.image.load("Paddle.png")
first_paddle_x = 30
first_paddle_y = 230  # Starting y

# Second paddle
second_pong_paddle = pygame.image.load("Paddle.png")
second_paddle_x = 770
second_paddle_y = 230  # Starting y

first_paddle_y_change = 0
second_paddle_y_change = 0

# Ball
ball = pygame.image.load("Ball.png")
ball_x = 370  # Starting x & y
ball_y = 270
ball_x_change = choice([0.3, -0.3])
ball_y_change = choice([0.3, -0.3])

font = pygame.font.Font("freesansbold.ttf", 16)
score_first = 0
score_second = 0

running = True


def paddle(paddle, x, y):
    screen.blit(paddle, (x, y))


def balle(x, y):
    screen.blit(ball, (x, y))


def score(text, x, y):
    screen.blit(text, (x, y))


while running:

    screen.fill((50, 50, 50))

    # Event gestion
    for event in pygame.event.get():

        # QUIT
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.QUIT:
            running = False

        # Paddle movement

        if event.type == pygame.KEYDOWN:
            # First paddle
            if event.key == pygame.K_s:
                first_paddle_y_change = 0.3
            elif event.key == pygame.K_z:
                first_paddle_y_change = -0.3

            # Second paddle
            if event.key == pygame.K_DOWN:
                second_paddle_y_change = 0.3
            elif event.key == pygame.K_UP:
                second_paddle_y_change = -0.3

        if event.type == pygame.KEYUP:
            # First paddle
            if event.key == pygame.K_s:
                first_paddle_y_change = 0
            elif event.key == pygame.K_z:
                first_paddle_y_change = 0

            # Second paddle
            if event.key == pygame.K_DOWN:
                second_paddle_y_change = 0
            elif event.key == pygame.K_UP:
                second_paddle_y_change = 0

    # Paddle movement
    first_paddle_y += first_paddle_y_change
    second_paddle_y += second_paddle_y_change

    # Paddle boundaries
    if first_paddle_y < 0:
        first_paddle_y = 0
    elif first_paddle_y >= 460:
        first_paddle_y = 460

    if second_paddle_y < 0:
        second_paddle_y = 0
    elif second_paddle_y >= 460:
        second_paddle_y = 460

    # Ball movement

    ball_x += ball_x_change
    ball_y += ball_y_change

    # Ball boundaries

    if ball_y <= 0:  # Vertical bounce
        ball_y_change = 0.3
    elif ball_y >= 570:
        ball_y_change = -0.3
    if first_paddle_x <= ball_x + 15 < first_paddle_x + 10 and first_paddle_y < ball_y + 15 < first_paddle_y + 140:  # Horizontal bounce (first paddle)
        ball_x_change = 0.3
    elif second_paddle_x < ball_x + 15 < second_paddle_x + 10 and second_paddle_y < ball_y + 15 < second_paddle_y + 140:  # Horizontal bounce (second paddle)
        ball_x_change = -0.3

    if ball_x <= 0:  # If left wall is hit
        ball_x_change = 0.3
        ball_x = 370
        ball_y = choice([x for x in range(0, 570)])  # Random y
        score_first += 1
    elif ball_x >= 770:  # If right wall is hit
        ball_x_change = -0.3
        ball_x = 370
        ball_y = choice([x for x in range(0, 570)])  # Random y
        score_second += 1

    # Blit

    paddle(first_pong_paddle, first_paddle_x, first_paddle_y)
    paddle(second_pong_paddle, second_paddle_x, second_paddle_y)

    balle(ball_x, ball_y)

    # Score printing

    score(font.render(f"Score 1 : {score_first}    Score 2 : {score_second}", True, (255, 255, 255)), 200, 20)

    pygame.display.update()
