import pygame

pygame.init()
pygame.display.set_caption("fuck pygame")

screen_width = 800
screen_height = 600
sky_display = (0,184,194)
sprite = (0,0,0)

screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(sky_display)


sys_font = pygame.font.SysFont("cascadiamonoplregular",20)
text_display = sys_font.render("hello",True,sprite)


pygame.draw.line(screen,sprite,(400,350),(0,0),2)
pygame.draw.rect(screen,(225,225,225),(100,100,100,100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(text_display,(400,350))
    pygame.display.update()
pygame.quit()
