import pygame

from Code.Entity import Entity
from Code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode): #Lista genérica
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) #instancia todos os objetos desejados

    def run(self, ): #pega as imagens necessárias
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move() #parte do efeito parallax, faz o fundo mover
            pygame.display.flip()
        pass

