import pygame
import random


class Pipe(object):
    def __init__(self):
        import Game
        self.imageBottom = pygame.image.load(
            "assets\Game Objects\pipe-green.png")
        self.height = self.imageBottom.get_height()
        self.width = self.imageBottom.get_width()
        self.yBottom = random.randint(
            Game.SCREEN_HEIGHT//3, Game.SCREEN_HEIGHT-112)
        self.yTop = self.yBottom - 150 - self.height
        self.imageUp = pygame.transform.rotate(self.imageBottom, 180)
        self.x = Game.SCREEN_WIDTH
        self.passed = False

    def update(self):
        self.x -= 1
        if self.x < 0-self.width:
            self.destroy()
            return True
        return False

    def render(self):
        import Main
        import Game

        Main.screen.blit(self.imageBottom, (self.x, self.yBottom))
        Main.screen.blit(
            self.imageUp, (self.x, self.yTop))

    def destroy(self):
        del self

    def getCollider(self):
        return [pygame.Rect(self.x, self.yBottom, self.width, self.height), pygame.Rect(self.x, self.yTop, self.width, self.height)]
