import pygame
import Game
import sys

pygame.init()
pygame.display.set_caption('Flappy Bird by Long')
pygame.display.set_icon(pygame.image.load(
    "assets\Game Objects\yellowbird-midflap.png"))
screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))

clock = pygame.time.Clock()
game = Game.Game(screen)
running = True

while running:
    clock.tick(100)
    screen.fill(Game.LightBlue)

    if game.gameOver:
        game.GameOver()
    elif game.menu:
        game.Menu()
    else:
        game.update()
        game.render()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if game.gameOver:
                game.gameOver = False
            elif game.menu:
                game.menu = False
            else:
                game.bird.moveUp()

pygame.quit()
sys.exit()
