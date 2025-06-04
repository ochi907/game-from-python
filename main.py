from __future__ import absolute_import
import OpenGL.GL as gl
import imgui
import sys
import pygame


pygame.init()
pygame.display.set_caption("fuck pygame")

screen_width = 900
screen_height = 700
sky_display = (0,184,194)
sprite = (0,0,0)

screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(sky_display)

img = pygame.image.load("asset/image/personal-picture.jpg")
img = pygame.transform.scale(img,(200,200))


pygame.draw.circle(screen,(255,255,255),(200,200),90.0,0,True,False,True,False)

cus_font = pygame.font.Font("asset/font/CascadiaMonoPL-Regular.otf",20)
text_display = cus_font.render("hello",True,sprite)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(text_display,(400,300))
    screen.blit(img,(600,300))
    
    pygame.display.update()
pygame.quit()
