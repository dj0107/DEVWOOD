import pygame

pygame.init()
screen_width = 448
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Puzzle Dongble")
clocks = pygame.time.Clock()

game_running = True
while game_running == True:
    clocks.tick(60) # FPS를 60으로 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

pygame.quit()