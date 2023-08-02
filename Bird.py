import pygame

g = 1/250


class Bird(object):
    def __init__(self):
        self.image = []
        self.image.append(pygame.image.load(
            "assets\Game Objects\yellowbird-upflap.png"))
        self.image.append(pygame.image.load(
            "assets\Game Objects\yellowbird-midflap.png"))
        self.image.append(pygame.image.load(
            "assets\Game Objects\yellowbird-downflap.png"))
        self.speed = 0.1
        self.frame = 0
        self.x = 50
        import Game
        self.y = Game.SCREEN_HEIGHT//2
        self.t = 0
        self.width = self.image[0].get_width()
        self.height = self.image[0].get_height()

    def moveUp(self):
        import Game
        pygame.mixer.Sound.play(Game.Sound.wing.value)
        self.y -= 20
        self.t = 0

    def update(self):
        self.t += 1
        self.y += (1/2) * g * self.t * self.t

    def render(self):
        import Main
        self.frame += self.speed
        if self.frame > 2:
            self.frame = 0
        rotateImg = pygame.transform.rotate(
            self.image[int(self.frame)], -self.t+45)
        Main.screen.blit(rotateImg, (self.x, self.y))

    def getCollider(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
