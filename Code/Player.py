import pygame.key

from Code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SPEED_SHOT_DELAY
from Code.Entity import Entity
from Code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple): #basico do player
        super(). __init__(name, position)
        self.shot_delay = ENTITY_SPEED_SHOT_DELAY[self.name] #cria um delay nos tiros


    def move(self, ): #movimento do jogador
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0: #faz a nave SUBIR quando (^) é pressionado, top>0 evita o player sair da tela
            self.rect.centery -= ENTITY_SPEED[self.name] #faz a nave SUBIR quando (^) é pressionado,Espeed é a velocidade de subida
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT: #faz a nave DESCER quando (\/) é pressionado, WinHeight evita o player sair da tela
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0: #faz a nave ir pra ESQUERDA quando (<) é pressionado, left>0 evita o player sair da tela
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.bottom < WIN_WIDTH: #faz a nave ir pra DIREITA quando (>) é pressionado, WinWidth evita o player sair da tela
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        self.shot_delay -= 1 #delay nos tiros
        if self.shot_delay == 0: #delay nos tiros
            self.shot_delay = ENTITY_SPEED_SHOT_DELAY[self.name] #delay nos tiros
            pressed_key = pygame.key.get_pressed() #faz a nave atirar quando pressionado
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery)) #faz com que os tiros sejam instanciados no meio do atirador e então se mova para direita