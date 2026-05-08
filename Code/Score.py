import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE
from pygame.font import Font

from Code.Const import C_YELLOW, SCORE_POS, MENU_OPTION, C_WHITE
from Code.DBProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./Asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)  #
        pass

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./Asset/Score.mp3')  # seleciona arquivo da musica
        pygame.mixer_music.play(-1)  # faz música tocar indefinidamente
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', C_YELLOW, SCORE_POS['Title']) #texto score
            if game_mode == MENU_OPTION[0]: #1 jogador
               score = player_score[0]
               text = 'Enter Player 1 (4 characters):'
            if game_mode == MENU_OPTION[1]: #2 jogadores coop
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team name (4 characters):'
            if game_mode == MENU_OPTION[2]: #2 jogador competitivo
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter Player 1 name (4 characters):'
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 characters):'
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get(): #permite fechar o jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4: #escrever nome
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()}) #coloca data no score
                    elif event.key == K_BACKSPACE: #apaga caracter
                        name = name [:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./Asset/Score.mp3')  # seleciona arquivo da musica
        pygame.mixer_music.play(-1)  # faz música tocar indefinidamente
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple): #texto score
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date(): #pega a data atual
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime ("%d/%m/%y")
    return f"{current_time} - {current_date}"