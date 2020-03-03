import pygame
import pygame_gui

WIDTH = 1600
HEIGHT = 1200

# pygame init
pygame.init()

window_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MGS Driver Station')

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#000000'))

clock = pygame.time.Clock()

# pygame_gui init
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text='Say Hello', manager=manager)

exit = False

while not exit:
    delta_t = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        manager.process_events(event)
    
    window_surface.blit(background, (0, 0))
    manager.update(delta_t)
    manager.draw_ui(window_surface)

    pygame.display.update()