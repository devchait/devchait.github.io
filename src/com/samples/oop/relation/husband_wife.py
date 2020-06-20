from oop.relation.relation import Relation
from oop.human import Human


class HusbandWife(Relation):
    def __init__(self, husband=None, wife=None):
        if isinstance(husband, Human) and isinstance(wife, Human):
            super().__init__(left_entity=husband, right_entity=wife)
        else:
            print("husband and wife must belong to same entity type")

    def husband(self):
        return self.left_entity

    def wife(self):
        return self.wife

    def relation(self):
        return {"husband": self.left_entity, "wife": self.right_entity}
