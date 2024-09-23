import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра-ТИР')
icon = pygame.image.load("img/TIR.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
targe_width = 80
targe_height = 80

target_x = random.randint(0, SCREEN_WIDTH - targe_width)
target_y = random.randint(0, SCREEN_HEIGHT - targe_height)

color = random.randint(0, 255)


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + targe_width and target_y < mouse_y < target_y + targe_height:
                target_x = random.randint(0, SCREEN_WIDTH - targe_width)
                target_y = random.randint(0, SCREEN_HEIGHT - targe_height)
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()




pygame.quit()