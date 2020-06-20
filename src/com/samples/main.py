if __name__ == "__main__":

    from oop.human import *

    tony_stark = Human(
        gender="Male",
        physic="5.4ft 100 lbs brown hair blue eyes",
        financial_status="very rich",
        occupation="scientist weapon business",
        iq="300",
        hobbies="reading discovering",
        education="phd",
        contact_number="",
        identity="ASO4389504",
        body_mark="heat_light",
        signature_scans="eye",
        date_of_birth="may 29th, 1970",
    )
    print(id(tony_stark))
    print(type(tony_stark))

    from oop.human_builder import *

    howard_stark_builder = HumanBuilder()
    howard_stark = howard_stark_builder.name("Howard Stark").gender("Male").build()

    maria_stark_builder = HumanBuilder()
    maria_stark = maria_stark_builder.name("Maria Stark").gender("Female").build()

    from oop.relation.husband_wife import HusbandWife

    stark_husband_wife = HusbandWife(howard_stark, maria_stark)

    print(id(stark_husband_wife))
    print(type(stark_husband_wife))
