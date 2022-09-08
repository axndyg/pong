
""" 

    program: pong.cpp
    date: 08 - 25 - 2022
    author: andres gutierrez

    purpose: learn pygame library with python pong

"""

from calendar import c
import pygame, sys, random 

def ball_movement():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0: 
        player_score += 1

        score_time = pygame.time.get_ticks()
    if ball.right >= screen_width:
        opponent_score += 1

        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
def player_move():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
def ai_move():
    if opponent.top < ball.y: 
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
def ball_restart():
    global ball_speed_x, ball_speed_y, score_time

    cur_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    if cur_time - score_time < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
    if 700 < cur_time - score_time < 1400:
        number_two = game_font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))
    if 1400 < cur_time - score_time < 2100:
        number_one = game_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))

    if cur_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else: 
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        score_time = None 

#Intialization
pygame.init()
clock = pygame.time.Clock()

#window 
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

#game rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 -15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height/2 -70, 10, 140)


# colors 
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)


# game variables
ball_speed_x = 7 * random.choice((-1,1))
ball_speed_y = 7 * random.choice((-1,1))
player_speed = 0
opponent_speed = 7 

#text variables
player_score = 0
opponent_score = 0 
game_font = pygame.font.Font("freesansbold.ttf", 32)

#score timeer
score_time = True

while True: 
    #handling input 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7 
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7 
            if event.key == pygame.K_UP:
                player_speed += 7  

    #game logic 
    ball_movement()
    player_move()
    ai_move()
    
    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))

    if score_time:
        ball_restart()
        

    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (660,470))

    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (600, 470))

    #update window
    pygame.display.flip()
    clock.tick(60)