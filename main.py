import pygame

# Pong

pygame.init()
screen_height = 800
screen_width = 600

screen = pygame.display.set_mode((screen_width, screen_height))

first_pong_paddle = pygame.image.load("Paddle.png")
first_paddle_x = 30

second_pong_paddle = pygame.image.load("Paddle.png")
second_paddle_x = 770

running = True

while running:
    for event in pygame.event.get():
        if event == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
