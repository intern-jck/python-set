import pygame
import time
import math

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

set_display = pygame.display.set_mode((400,400))
set_display.fill(white)




def test_all_shapes():
        
    #Empty
    #square
    pygame.draw.rect(set_display, red, (100,100,50,50), width=1)
    #circle
    pygame.draw.circle(set_display, green, (200, 125), 25, width=1)
    #triangle
    pygame.draw.polygon(set_display, blue, ((250,150), (300,150), (275,100)), width=1)

    #Shaded
    #square
    pygame.draw.rect(set_display, red, (100,175,50,50), width=1)
    pygame.draw.line(set_display, red, (112,175), (112,225), width=1)
    pygame.draw.line(set_display, red, (125,175), (125,225), width=1)
    pygame.draw.line(set_display, red, (137,175), (137,225), width=1)
    #circle
    radius = 25
    circle_x = 200
    circle_y = 200
    alpha = math.sin(79)
    pygame.draw.circle(set_display, green, (circle_x, circle_y), radius, width=1)
    pygame.draw.line(set_display, green, (circle_x-radius/2, circle_y-radius*0.75), (circle_x-radius/2,circle_y+radius*0.75), width=1)
    pygame.draw.line(set_display, green, (circle_x, circle_y-radius), (circle_x,circle_y+radius), width=1)
    pygame.draw.line(set_display, green, (circle_x+radius/2, circle_y+radius*0.75), (circle_x+radius/2,circle_y-radius*0.75), width=1)
    #triangle
    pygame.draw.polygon(set_display, blue, ((250,225), (300,225), (275,175)), width=1)
    pygame.draw.line(set_display, blue, (262, 225), (262,200), width=1)
    pygame.draw.line(set_display, blue, (275, 225), (275,175), width=1)
    pygame.draw.line(set_display, blue, (287, 225), (287,200), width=1)

    #Filled
    #square
    pygame.draw.rect(set_display, red, (100,250,50,50), width=0)
    #circle
    pygame.draw.circle(set_display, green, (200, 275), 25, width=0)
    #triangle
    pygame.draw.polygon(set_display, blue, ((250,300), (300,300), (275,250)), width=0)

#Functions for shapes

def empty_square(x, y):
    pygame.draw.rect(set_display, red, (x,y,50,50), width=1)

def empty_circle(x, y):
    pygame.draw.circle(set_display, green, (x, y), 25, width=1)

def empty_trianlge(x, y):
    x_1, y_1 = x ,y
    x_2, y_2 = x + 50, y
    x_3, y_3= x + 25, y - 50
    pygame.draw.polygon(set_display, blue, ((x_1, y_1), (x_2,y_2), (x_3,y_3)), width=1)


def shaded_square(x, y):
    pygame.draw.rect(set_display, red, (100,175,50,50), width=1)
    pygame.draw.line(set_display, red, (112,175), (112,225), width=1)
    pygame.draw.line(set_display, red, (125,175), (125,225), width=1)
    pygame.draw.line(set_display, red, (137,175), (137,225), width=1)

def shaded_circle(x , y):
    circle_x, circle_y = x, y
    radius= 25
    pygame.draw.circle(set_display, green, (circle_x, circle_y), radius, width=1)
    pygame.draw.line(set_display, green, (circle_x-radius/2, circle_y-radius*0.75), (circle_x-radius/2,circle_y+radius*0.75), width=1)
    pygame.draw.line(set_display, green, (circle_x, circle_y-radius), (circle_x,circle_y+radius), width=1)
    pygame.draw.line(set_display, green, (circle_x+radius/2, circle_y+radius*0.75), (circle_x+radius/2,circle_y-radius*0.75), width=1)

def shaded_triangle(x, y):
    x_1, y_1 = x ,y
    x_2, y_2 = x + 50, y
    x_3, y_3= x + 25, y - 50
    pygame.draw.polygon(set_display, blue, ((x_1,y_1), (x_2,y_2), (x_3,y_3)), width=1)
    pygame.draw.line(set_display, blue, (x_1+12, y_1), (x_1+12,y_1 - 25), width=1)
    pygame.draw.line(set_display, blue, (x_1+25, y_1), (x_1+25,y_1 - 50), width=1)
    pygame.draw.line(set_display, blue, (x_1+37, y_1), (x_1 + 37,y_1 - 25), width=1)    


def filled_square(x, y):    
    pygame.draw.rect(set_display, red, (x,y,50,50), width=0)

def filled_circle(x, y):
    pygame.draw.circle(set_display, green, (x, y), 25, width=0)

def filled_triangle(x, y):
    x_1, y_1 = x ,y
    x_2, y_2 = x + 50, y
    x_3, y_3= x + 25, y - 50
    pygame.draw.polygon(set_display, blue, ((x_1,y_1), (x_2,y_2), (x_3,y_3)), width=0)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()