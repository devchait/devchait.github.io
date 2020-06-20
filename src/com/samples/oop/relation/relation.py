class Relation:
    def __init__(self, left_entity=None, right_entity=None):
        self.left_entity = left_entity
        self.right_entity = right_entity

    def relation(self):
        return {"left_entity": self.left_entity, "right_entity": self.right_entity}
