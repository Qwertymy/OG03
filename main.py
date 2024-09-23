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
target_width = 80
target_height = 80

# Начальные координаты мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Скорость мишени по осям
target_speed_x = random.choice([-1, 1])
target_speed_y = random.choice([-1, 1])

# Случайный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Переменная для подсчета очков
score = 0
font = pygame.font.Font(None, 36)  # Шрифт для отображения текста

running = True
while running:
    screen.fill(color)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1  # Увеличиваем счет при попадании
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Изменяем цвет фона при попадании
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Движение мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка столкновений с границами экрана и смена направления
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x *= -1
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y *= -1

    # Отображение мишени
    screen.blit(target_img, (target_x, target_y))

    # Отображение количества очков
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Обновляем экран
    pygame.display.update()

pygame.quit()
