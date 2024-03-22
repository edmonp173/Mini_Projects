# need to download pygame

import random
import pygame
import os
pygame.init()

#library of the game 
white = (255, 255, 255)
yellow = (217, 200, 20)
black = (0, 0, 0)
gray = (128, 128, 128)
WIDTH = 400
HEIGHT = 500
background = yellow
fps = 60
script_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_directory, "player.png")
player = pygame.transform.scale(pygame.image.load(image_path), (90, 80))

font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()
Score = 0
game_over = False

#game variables
player_x = 170
player_y = 400
platforms = [[175, 490, 70, 10], [85,370, 70, 10], [265, 370 , 70, 10], [175, 260, 70, 10], [85,150, 70, 10], [265, 90 , 70, 10], [175, 150 , 70, 10]]
jump = False
y_change = 0
x_change = 0
player_speed = 3
#screen
screen =pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('epic jumper')

#check for collisions
def check_collisions(rect_list, j):
   global player_x
   global player_y
   global y_change
   for i in range(len(rect_list)):
      if rect_list[i].colliderect([player_x, player_y + 70, 56, 7]) and jump == False and y_change > 0:
         j = True
   return j





#update player y position every loop
def update_player(y_pos):
   global jump
   global y_change
   jump_height = 10
   gravity = .4
   if jump:
      y_change = -jump_height
      jump = False
   y_pos += y_change
   y_change += gravity
   return y_pos

#screen movment and platform
def update_platform(my_list, y_pos, change):
   global Score
   if player_y < 250 and change < 0:
      for i in range(len(my_list)):
         my_list[i][1] -= change
   else:
         pass
   for item in range(len(my_list)):
      if my_list[item][1] > 500:
        my_list[item] = [random.randint(10, 320), random.randint(-50, -10), 70, 10]
        Score += 1
   return my_list


running = True
while running == True:
    timer.tick(fps)
    screen.fill(background)
    screen.blit(player, (player_x, player_y))
    blocks = []
    Score_text = font.render('score:' + str(Score), True, black, background)
    screen.blit(Score_text, (320, 20))
    

    for i in range(len(platforms)):
       block = pygame.draw.rect(screen, black, platforms[i], 0, 3)
       blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running = False
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_a:
              x_change = -player_speed 
           if event.key == pygame.K_d:
              x_change = player_speed
        if event.type == pygame.KEYUP:
           if event.key == pygame.K_a:
              x_change = 0
           if event.key == pygame.K_d:
              x_change = 0
#גבולות משחק
    if player_y < 440:
      player_y = update_player(player_y)
    else:
       game_over = True
       y_change = 0

    if player_x < -20:
       player_x = -20
    elif player_x > 330:
       player_x = 330
    player_x += x_change
    jump = check_collisions(blocks, jump)
    platforms = update_platform(platforms, player_y, y_change)
    
    #if x_change > 0:
       # player1 = player
   # elif x_change < 0:
       # player = player1
   
    

       
       #player = pygame.transform.flip(pygame.transform.scale(pygame.image.load(r"C:\Users\avita\Desktop\first game\player.png"), (90, 80)), 1, 0)


    pygame.display.flip()
pygame.QUIT()