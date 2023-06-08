'''
The Pygame module is used for game development in Python.
Here's an example code for creating a simple game using Pygame:


'''


import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)
    pygame.display.flip()

pygame.quit()