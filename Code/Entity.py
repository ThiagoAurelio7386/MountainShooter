from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):

    def __init__(self, name: str, position: tuple): #Entidade base, que serve como fundação para outras entidades
        self.name = name
        self.surf = pygame.image.load('./Asset/' + name + '.png').convert_alpha() #imagem genérica, cAlpha ajuda a otimizar imagem
        self.rect = self.surf.get_rect(left=position[0], top=position[1]) # 0 Eixo X e 1 Eixo Y
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass