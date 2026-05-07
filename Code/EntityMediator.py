from Code.Enemy import Enemy
from Code.Entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity): # verifica se atingiu limite da tela
        if isinstance(ent, Enemy):
            if ent.rect.right < 0: #se o inimigo passar da tela o HP será zerado
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]): #verificação de colisão
        for i in range(len(entity_list)):
            teste_entity = entity_list[i]
            EntityMediator.__verify_collision_window(teste_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]): #verifica hp, recebe Entity como parametro
        for ent in entity_list:
            if ent.health <= 0: #se HP da entity for igual ou maior que zero, ela sera removida
                entity_list.remove(ent)  #se HP da entity for igual ou maior que zero, ela sera removida