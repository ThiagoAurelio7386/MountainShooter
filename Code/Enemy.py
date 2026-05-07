from Code.Const import ENTITY_SPEED, WIN_WIDTH
from Code.Entity import Entity

class Enemy(Entity):

    def __init__(self, name: str, position: tuple): #basico do inimigo
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name] # parte do efeito parallax, ajusta a velocidade de movimento de cada parte do fundo
        if self.rect.right <= 0: #parte do efeito parallax, faz a imagem se repetir
            self.rect.left =  WIN_WIDTH #parte do efeito parallax, pega o que esta na esquerda e joga na direita