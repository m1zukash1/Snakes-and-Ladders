import pygame
import copy
from game import Game
from board_positions import board_positions

player_count = 2

pygame.init()
game: Game = Game(player_count)
player_sprites = []
players = game.board.player_queue.copy()

for i in range(player_count):
    player_sprites.append(pygame.image.load('assets/player'+str(i+1)+'.png'))

screen_width = 816
screen_height = 680

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snakes and Ladders')

background_image = pygame.image.load('assets/board.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.turn()

    screen.fill((77,77,77))
    screen.blit(background_image, (0, 0))

    for i in range(player_count):
        screen.blit(player_sprites[i], (board_positions[players[i].position][0] - 24, board_positions[players[i].position][1] - 32))


    pygame.display.flip()

pygame.quit()
