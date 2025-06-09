import pygame

# setting
pygame.init()
pygame.display.set_caption("fuck pygame")
clock = pygame.time.Clock()
running = True
screen_width = 1400
screen_height = 900
sky_display = (0,184,194)
sprite = (0,0,1)

screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(sky_display)

icon = pygame.image.load("asset/image/rap_is_now.jpg")
pygame.display.set_icon(icon)
img = pygame.image.load("asset/image/personal-picture.jpg")
img = pygame.transform.scale(img,(200,200))

screen_rect = screen.get_rect()    
display_res = screen_rect.size
mouse_pos = pygame.mouse.get_pos()
mouse_click = pygame.mouse.get_pressed(num_buttons=5)


pygame.draw.circle(screen,(255,255,255),(200,200),90.0,0,True,False,True,False)

#debug display
cus_font = pygame.font.Font("asset/font/CascadiaMonoPL-Regular.otf",15)
text_display = cus_font.render("Fong is GAYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",True,sprite)
tdy = cus_font.render(f"{display_res}",True,sprite)
mouse_pos_display = cus_font.render(f"{mouse_pos}",True,sprite)
mouse_click_display = cus_font.render(f"{mouse_click}",True,sprite)


# loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(text_display,(400,300))
    screen.blit(img,(600,300))
    screen.blit(tdy,(10,10))
    screen.blit(mouse_pos_display,(10,40))
    screen.blit(mouse_click_display,(10,70))
    pygame.display.update()
pygame.quit()
