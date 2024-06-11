#imports 
import pygame
import time
import random

speed = 15

#colours and sizes
horizontal =720
vertical = 480
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

pygame.init()
pygame.display.set_caption('Snek Game')
screen = pygame.display.set_mode((horizontal,vertical))
fps = pygame.time.Clock()
position = [100,50]
body = [[11,50],[90,50],[80,50],[70,50]]
fruit = [random.randrange(1, (horizontal//10)) * 10, random.randrange(1, (vertical//10)) * 10]
spawn = True
direction = 'RIGHT'
change = direction
score = 0
def show_score(choice, color, font, size):
    font = pygame.font.SysFont(font, size)
    surface = font.render('Score : ' + str(score), True, color)
    rect = surface.get_rect()
    screen.blit(surface, rect)
    
def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    surface = font.render('Your Score is : ' + str(score), True, red)
    
    rect = surface.get_rect()
    rect.midtop = (horizontal/2, vertical/4)
    screen.blit(surface, rect)
    pygame.display.flip()
    
    time.sleep(2)
    pygame.quit()
    quit()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change = 'UP'
            if event.key == pygame.K_DOWN:
                change = 'DOWN'
            if event.key == pygame.K_LEFT:
                change = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change = 'RIGHT'
    
    if change == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
        
    #movements
    if direction == 'UP':
        position[1] -= 10
    if direction == 'DOWN':
        position[1] += 10
    if direction == 'LEFT':
        position[0] -= 10
    if direction =='RIGHT':
        position[0] += 10
    
        





