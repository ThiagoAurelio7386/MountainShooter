import random

from Code.Background import Background
from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Enemy import Enemy
from Code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg': #Matchcase da lista
                list_bg = [] #lista com os backgrounds
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}',  (0,0))) #vai juntando todos os backgrounds Level1Bg do 1 até 6
                    list_bg.append(Background(f'Level1Bg{i}',  (WIN_WIDTH, 0))) #parte do efeito parallax
                return list_bg #cada linha "list_bg.append" é um conjunto de 7 imagens, sempre use 2 linhas para ter boa estica
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30)) #define posição do player, neste projeto esta no meio do canto esquerdo
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))  # define posição do player, neste projeto esta no meio do canto esquerdo
            case 'Enemy1':
                return Enemy('Enemy1',(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))