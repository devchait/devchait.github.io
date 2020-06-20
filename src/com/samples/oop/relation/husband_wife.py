class HusbandWife(Relation):
    def __init__(husband=None, wife=None):
        if isinstance(husband, "Human") and isinstance(wife, "Human"):
            super().__init__(left_entity=husband, right_entity=wife)
        else:
            print("husband and wife must belong to same entity type")

    def husband():
        return self.left_entity

    def wife():
        return self.wife

    def relation():
        return {"husband": self.left_entity, "wife": self.right_entity}
