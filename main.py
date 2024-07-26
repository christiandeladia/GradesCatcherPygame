import pygame
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Grades Catcher")
icon = pygame.image.load("robot.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

background = pygame.image.load("back1.png")
background = pygame.transform.scale(background, (600, 500))
robot = pygame.image.load("robot.png")
robot = pygame.transform.scale(robot, (100, 100))
uno = pygame.image.load("uno.png")
uno = pygame.transform.scale(uno, (80, 80))
dos = pygame.image.load("dos.png")
dos = pygame.transform.scale(dos, (80, 80))
singko = pygame.image.load("singko.png")
singko = pygame.transform.scale(singko, (80, 80))

robot_x = 300
robot_y = 400
robot_speed = 10
items = []
item_speed = 5
lives = 5
font = pygame.font.Font(None, 36)
paused = False

def display_lives():
    lives_text = font.render("lives: " + str(lives), True, (255, 255, 255))
    screen.blit(lives_text, (10, 10))

def game_over():
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(game_over_text, (250, 230))
    pygame.display.update()
    pygame.time.delay(2000)

def pause():
    game_pause_text = font.render("PAUSED", True, (255, 0, 0))
    screen.blit(game_pause_text, (250, 230))
    global paused
    paused = not paused
    

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause()

    if not paused:
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and robot_x > 0:
            robot_x -= robot_speed
        if keys[K_RIGHT] and robot_x < 500:
            robot_x += robot_speed
        if keys[K_a] and robot_x > 0:
            robot_x -= robot_speed
        if keys[K_d] and robot_x < 500:
            robot_x += robot_speed

        if len(items) < 3:
            if random.randint(0, 50) == 0:
                item_x = random.randint(50, 450)
                item_y = 0
                item_type = random.choice(["uno", "dos", "singko"])
                items.append([item_x, item_y, item_type])

        for item_pos in items:
            item_pos[1] += item_speed
            if item_pos[1] > 500:
                items.remove(item_pos)
                item_type = item_pos[2]
                if item_type == "uno":
                    lives -= 1

            if item_pos[1] + 30 >= robot_y and item_pos[0] + 30 >= robot_x and item_pos[0] <= robot_x + 100:
                items.remove(item_pos)
                item_type = item_pos[2]
                if item_type == "uno":
                    lives += 1
                if item_type == "dos":
                    lives -= 1
                if item_type == "singko":
                    lives -= 2

    screen.blit(background, (0, 0))
    screen.blit(robot, (robot_x, robot_y))
    for item_pos in items:
        if item_pos[2] == "uno":
            screen.blit(uno, (item_pos[0], item_pos[1]))
        elif item_pos[2] == "dos":
            screen.blit(dos, (item_pos[0], item_pos[1]))
        elif item_pos[2] == "singko":
            screen.blit(singko, (item_pos[0], item_pos[1]))
    display_lives()
    pygame.display.update()
    clock.tick(60)

    if lives <= 0:
        game_over()
        running = False

pygame.quit()