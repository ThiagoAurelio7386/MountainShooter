import sys

import pygame

from Code.Const import WIN_HEIGHT
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode): #Lista genérica
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) #instancia todos os objetos desejados

    def run(self, ):
        pygame.mixer_music.load(f'./Asset/{self.name}.mp3') #coloca a musica escolhida no level indefinidamente
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock() #cloc
        while True:
            clock.tick(60) #quanto maior o fps maior a velocidade de execução
            for ent in self.entity_list: #pega as imagens necessárias
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move() #parte do efeito parallax, faz o fundo mover
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # printed text
            self.level_text(text_size 14, text f'{self.name} - Timeout {self.timeout / 1000 :.1d}s', COLOR_WHITE, text_pos (10, 5))
            self.level_text(text_size 14, text f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, text_pos (10, WIN_HEIGHT - 35))
            self.level_text(text_size 14, text f'entidades: {len(self.entity_list)}', COLOR_WHITE, text_pos (10, WIN_HEIGHT - 20))
            pygame.display.flip()
        pass