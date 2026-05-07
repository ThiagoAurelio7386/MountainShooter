from Code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SPEED_SHOT_DELAY
from Code.EnemyShot import EnemyShot
from Code.Entity import Entity

class Enemy(Entity):

    def __init__(self, name: str, position: tuple): #basico do inimigo
        super().__init__(name, position)
        self.shot_delay = ENTITY_SPEED_SHOT_DELAY[self.name]  # cria um delay nos tiros

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name] # ajusta a velocidade de movimento de cada parte do fundo

    def shoot(self): #permite o inimigo atirar
        self.shot_delay -= 1  # delay nos tiros
        if self.shot_delay == 0:  # delay nos tiros
            self.shot_delay = ENTITY_SPEED_SHOT_DELAY[self.name]  # delay nos tiros
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))  # faz com que os tiros sejam instanciados no meio do atirador e então se mova para direita