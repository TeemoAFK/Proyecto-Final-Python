
import pygame
from OnBoard import OnBoard
from pygame import mixer

class Coin(OnBoard):
    def __init__(self, raw_image, position):
        super(Coin, self).__init__(raw_image, position)
        self.__value = 5
        self.__coinAnimState = 0  # Initialize animation state to 0

    # Getters and Setters
    def setValue(self, value):
        self.__value = value

    def getValue(self):
        return self.__value

    # Update the image of the coin
    def updateImage(self, raw_image):
        self.image = raw_image
        self.image = pygame.transform.scale(self.image, (15, 15))

    # Animate the coin
    def animateCoin(self):
        self.__coinAnimState = (self.__coinAnimState + 1) % 25
        if self.__coinAnimState / 5 == 0:
            self.updateImage(pygame.image.load('Assets/coin1.png'))
        if self.__coinAnimState / 5 == 1:
            self.updateImage(pygame.image.load('Assets/coin2.png'))
        if self.__coinAnimState / 5 == 2:
            self.updateImage(pygame.image.load('Assets/coin3.png'))
        if self.__coinAnimState / 5 == 3:
            self.updateImage(pygame.image.load('Assets/coin4.png'))
        if self.__coinAnimState / 5 == 4:
            self.updateImage(pygame.image.load('Assets/coin5.png'))

    def collectCoin(self):
        # Play coin sound when you collect a coin
        mixer.init()
        mixer.music.load('Assets/coin.mp3')
        mixer.music.set_volume(1)
        pygame.mixer.music.play()
        return self.__value
