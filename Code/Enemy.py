from Code.Const import ENTITY_SPEED, WIN_WIDTH
from Code.Entity import Entity

class Enemy(Entity):

    def __init__(self, name: str, position: tuple): #basico do inimigo
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name] # parte do efeito parallax, ajusta a velocidade de movimento de cada parte do fundo