import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Asset/MenuBg.png').convert_alpha() #carrega imagem selecionada, cAlpha ajuda a otimizar imagens
        self.rect = self.surf.get_rect(left=0, top=0) #coordenadas da imagem, default


    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./Asset/Menu.mp3')  # seleciona arquivo da musica
        pygame.mixer_music.play(-1)  # faz música tocar indefinidamente
        while True:
            #DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect) #desenha imagem
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))  # escreve texto
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))  # escreve texto
            #no menu_text, o text_center_pos configura a posição do text em eixo X e Y.

            for i in range(len(MENU_OPTION)): #Seleção no menu
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            #check for all events     #fecha janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #close window
                    quit() #end pygame
                if event.type == pygame.KEYDOWN: # Faz menu descer quando a seta "pra baixo" é pressionada
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                         menu_option += 1
                        else:
                            menu_option = 0 # termina aqui
                    if event.key == pygame.K_UP: # Faz menu subir quando a tecla "^" é pressionada
                        if menu_option > 0:
                           menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1 #termina
                    if event.key == pygame.K_RETURN: #ENTER #Faz botões funcionarem
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)