import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import WIN_HEIGHT, C_WHITE, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from Code.Enemy import Enemy
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory
from Code.EntityMediator import EntityMediator
from Code.Player import Player


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]): #Lista genérica
        self.timeout = TIMEOUT_LEVEL # 20 parte do timer dos levels
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg')) #instancia todos os objetos desejados (levels)
        player = EntityFactory.get_entity('Player1') #coloca o jogador
        player.score = player_score[0] #score
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]: #Adiciona o Player2 se o modo correto for escolhido
            player = EntityFactory.get_entity('Player2') # coloca o jogador
            player.score = player_score[1]  # score
            self.entity_list.append(player) #coloca o Player2 no level
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME) #spawn dos inimigos
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP) #100ms, parte do timer dos levels


    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./Asset/{self.name}.mp3') #coloca a musica escolhida no level indefinidamente
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock() #clock
        while True:
            clock.tick(60) #quanto maior o fps maior a velocidade de execução
            for ent in self.entity_list: #pega as imagens necessárias
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move() #parte do efeito parallax, faz o fundo e (talvez) outras entidades mover
                if isinstance(ent, (Player, Enemy)): #tiros do player e inimigo
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot) #tiros do player e inimigo
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', C_CYAN, (10, 45))
            for event in pygame.event.get(): #permite fechar o jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list: #score
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

            found_player = False #Variavel verifica se o player esta vivo
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True

            if not found_player: # se o player morrer, volta pro menu principal
                return False

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip() #Nos textos acima timeout mostra a duração da fase, fps colocar o fps na tela, entidades mostra quantas entidades tem na tela
            #collisions
            EntityMediator.verify_collision(entity_list=self.entity_list) #verificação de colisão
            EntityMediator.verify_health(entity_list=self.entity_list) #verificação de HP


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)