import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import WIN_HEIGHT, COLOR_WHITE
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode): #Lista genérica
        self.timeout = None
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) #instancia todos os objetos desejados
        self.timeout = 20000 # 20 segundos

    def run(self, ):
        pygame.mixer_music.load(f'./Asset/{self.name}.mp3') #coloca a musica escolhida no level indefinidamente
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock() #clock
        while True:
            clock.tick(60) #quanto maior o fps maior a velocidade de execução
            for ent in self.entity_list: #pega as imagens necessárias
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move() #parte do efeito parallax, faz o fundo mover
            for event in pygame.event.get(): #permite fechar o jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE,  (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE,  (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip() #Nos textos acima timeout mostra a duração da fase, fps colocar o fps na tela, entidades mostra quantas entidades tem na tela
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)