import pygame
from fighter import Fighter

pygame.init()

#Create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colour
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

#define fighter variables use paint to crop it
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]


#load background image 
bg_image = pygame.image.load("asset/img/background.jpg").convert_alpha()

#load spritesheets
warrior_sheet = pygame.image.load("asset/img/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("asset/img/wizard.png").convert_alpha()

#define number of step in each animation
WARRIOR_ANIMATION_STEP = [10,8,1,7,7,3,7]
WIZAED_ANIMATION_STEP = [8,8,1,8,8,3,7]



#function for drawing background
def draw_bg():
    scale_bg = pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scale_bg,(0,0))

#Health Bar
def draw_health_bar(health,x,y):
    ratio = health / 100
    pygame.draw.rect(screen,WHITE,(x-2,y-2,404,34))
    pygame.draw.rect(screen,RED,(x,y,400,30))
    pygame.draw.rect(screen,YELLOW,(x,y,400*ratio,30))

#Create instance of fighters
fighter_1 = Fighter(200,310,False,WARRIOR_DATA,warrior_sheet,WARRIOR_ANIMATION_STEP)
fighter_2 = Fighter(700,310,True,WIZARD_DATA,wizard_sheet,WIZAED_ANIMATION_STEP)

#game loop
run = True
while run:

    clock.tick(FPS)
    #draw background
    draw_bg()

    #show health bar
    draw_health_bar(fighter_1.health,20,20)
    draw_health_bar(fighter_2.health,580,20)

    #move fighter
    fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2)
    #draw fighter
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.update()

#exit pygame
pygame.quit()
