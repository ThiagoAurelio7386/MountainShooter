import pygame

from Code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from Code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) #tamanho da janela, dados no arquivo const

    def run(self):
        while True:
            menu = Menu(self.window) #abre mini-janela com o jogo
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                pass
            elif menu_return == MENU_OPTION[4]:
                pygame.quit() # fecha janela (sai do jogo)
                quit() #end pygame
            else:
                pass
