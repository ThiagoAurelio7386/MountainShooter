from abc import ABC, abstractmethod

import pygame.image

from Code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):

    def __init__(self, name: str, position: tuple): #Entidade base, que serve como fundação para outras entidades
        self.name = name
        self.surf = pygame.image.load('./Asset/' + name + '.png').convert_alpha() #imagem genérica, cAlpha ajuda a otimizar imagem
        self.rect = self.surf.get_rect(left=position[0], top=position[1]) # 0 Eixo X e 1 Eixo Y
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name] #Vida de cada entidade do jogo
        self.damage = ENTITY_DAMAGE[self.name] #dano de cada entidade do jogo
        self.score = ENTITY_SCORE[self.name] #score de cada inimigo
        self.last_dmg = 'None' #variavel para que o score só conte o que o jogador mexeu

    @abstractmethod
    def move(self, ):
        pass