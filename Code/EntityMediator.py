from Code.Const import WIN_WIDTH
from Code.Enemy import Enemy
from Code.EnemyShot import EnemyShot
from Code.Entity import Entity
from Code.Player import Player
from Code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity): # verifica se atingiu limite da tela
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0: #se o inimigo passar da tela o HP será zerado
                ent.health = 0
        if isinstance(ent, PlayerShot): #remove tiros não usados
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0: #se o inimigo passar da tela o HP será zerado
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2): #colisões de tiro com entidade (player and enemy)
        valid_interaction = False
        if  isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_collision = True
        elif  isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_collision = True
        elif  isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_collision = True
        elif  isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_collision = True

        if valid_interaction: #if valid_interaction == True:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage #sistema de colisão, dano
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def verify_collision(entity_list: list[Entity]): #verificação de colisão
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1) #verifica se esta na janela
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]): #verifica hp, recebe Entity como parametro
        for ent in entity_list:
            if ent.health <= 0: #se HP da entity for igual ou maior que zero, ela sera removida
                entity_list.remove(ent)  #se HP da entity for igual ou maior que zero, ela sera removida