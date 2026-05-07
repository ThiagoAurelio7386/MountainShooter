from Code.Const import WIN_WIDTH, ENTITY_SPEED
from Code.Entity import Entity

class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name] # parte do efeito parallax, ajusta a velocidade de movimento de cada parte do fundo
        if self.rect.right <= 0: #parte do efeito parallax, faz a imagem se repetir
            self.rect.left =  WIN_WIDTH #parte do efeito parallax, pega o que esta na esquerda e joga na direita