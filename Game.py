import pygame
from Bird import Bird
from Pipe import Pipe
from enum import Enum

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512


LightBlue = (204, 255, 255, 0)


class Sound(Enum):
    pygame.mixer.init()
    die = pygame.mixer.Sound("assets/Sound Efects/die.wav")
    hit = pygame.mixer.Sound("assets/Sound Efects/hit.wav")
    point = pygame.mixer.Sound("assets/Sound Efects/point.wav")
    swoosh = pygame.mixer.Sound("assets/Sound Efects/swoosh.wav")
    wing = pygame.mixer.Sound("assets/Sound Efects/wing.wav")


class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.bird = Bird()

        self.background = pygame.image.load(
            "assets/Game Objects/background-day.png")
        self.menuImg = pygame.image.load("assets/UI/message.png")
        self.ground = pygame.image.load(
            "assets/Game Objects/base.png")
        self.gameOverImg = pygame.image.load("assets/UI/gameover.png")

        self.delayPipeSpawn = 200
        self.pipes = []
        self.score = 0
        self.menu = True
        self.gameOver = False

        self.xBase = 0

    def update(self):
        self.bird.update()
        self.delayPipeSpawn -= 1
        if self.delayPipeSpawn == 0:
            self.createPipe()
            self.delayPipeSpawn = 200
        for pipe in self.pipes:
            if pipe.update():
                self.pipes.remove(pipe)
        if self.checkEnd():
            self.restart()
        self.increaseScore()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        for pipe in self.pipes:
            pipe.render()
        if self.xBase > -20:
            self.xBase -= 1
        else:
            self.xBase = 0
        self.screen.blit(self.ground, (self.xBase, SCREEN_HEIGHT-112))
        self.bird.render()
        self.showScore()

    def checkEnd(self):
        if self.bird.y > SCREEN_HEIGHT:
            pygame.mixer.Sound.play(Sound.die.value)
            self.menu = True
            self.gameOver = True
            return True
        birdCollider = self.bird.getCollider()
        for pipe in self.pipes:
            pipeCollider = pipe.getCollider()
            for collider in pipeCollider:
                if birdCollider.colliderect(collider):
                    pygame.mixer.Sound.play(Sound.hit.value)
                    self.gameOver = True
                    self.menu = True
                    return True
        return False

    def createPipe(self):
        self.pipes.append(Pipe())

    def restart(self):
        self.bird = Bird()
        self.delayPipeSpawn = 200
        self.pipes = []
        self.score = 0

    def increaseScore(self):
        for pipe in self.pipes:
            if pipe.x+pipe.width < self.bird.x and not pipe.passed:
                self.score += 1
                pygame.mixer.Sound.play(Sound.point.value)
                pipe.passed = True

    def showScore(self):
        import Main
        import Game
        scoreString = str(self.score)
        for i in range(0, len(scoreString)):
            path = "assets/UI/Numbers/" + scoreString[i] + ".png"
            numberImg = pygame.image.load(path)
            Main.screen.blit(numberImg, (Game.SCREEN_WIDTH/2-20+i*24, 10))

    def Menu(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.menuImg, (50, 50))

    def GameOver(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.gameOverImg, (50, 100))
