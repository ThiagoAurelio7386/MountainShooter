import pygame

from Code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from Code.Level import Level
from Code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) #tamanho da janela, dados no arquivo const

    def run(self):
        while True:
            menu = Menu(self.window) #abre mini-janela com o jogo
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]: #escolhe modo de jogo
                player_score = [0,0] #score do Player1 e Player2
                level = Level(self.window, 'Level1', menu_return, player_score) #level 1
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score) #level 2
                    level_return = level.run(player_score)

            elif menu_return == MENU_OPTION[4]:
                pygame.quit() # fecha janela (sai do jogo)
                quit() #end pygame
            else:
                pass
