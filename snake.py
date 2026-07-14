# will make a snake game using pygame or something

import sys
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game Scoreboard")
clock = pygame.time.Clock()

COLOR_BG = (20, 24, 33)
COLOR_TEXT = (255, 255, 255)

score_font = pygame.font.Font(None, 40)
current_score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(COLOR_BG)

    score_surface = score_font.render(f"Score: {current_score}", True, COLOR_TEXT)
    screen.blit(score_surface, (30, 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
