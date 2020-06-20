from oop.human import Human


class HumanBuilder:
    def __init__(self):
        self.__nam__ = None
        self.__gender__ = None
        self.__physic__ = None
        self.__body_mark__ = None
        self.__financial_status__ = None
        self.__occupation__ = None
        self.__iq__ = None
        self.__hobbies__ = None
        self.__education__ = None
        self.__contact_number__ = None
        self.__body_mark__ = None
        self.__signature_scans__ = None
        self.__date_of_birth__ = None
        self.__identity__ = None

    def name(self, name):
        self.__nam__ = name
        return self

    def gender(self, gender):
        self.__gender__ = gender
        return self

    def physic(self, physic):
        self.__physic__ = physic
        return self

    def financial_status(self, financial_status):
        self.__financial_status__ = financial_status
        return self

    def occupation(self, occupation):
        self.__occupation__ = occupation
        return self

    def iq(self, iq):
        self.__iq__ = iq
        return self

    def hobbies(self, hobbies):
        self.__hobbies__ = hobbies
        return self

    def education(self, education):
        self.__education__ = education
        return self

    def contact_number(self, contact_number):
        self.__contact_number__ = contact_number
        return self

    def identity(self, identity):
        self.__identity__ = identity
        return self

    def body_mark(self, body_mark):
        self.__body_mark__ = body_mark
        return self

    def signature_scans(self, signature_scans):
        self.__signature_scans__ = signature_scans
        return self

    def date_of_birth(self, date_of_birth):
        self.__date_of_birth__ = date_of_birth
        return self

    def build(self):
        human = Human(
            gender=self.__gender__,
            name=self.__nam__,
            physic=self.__physic__,
            financial_status=self.__financial_status__,
            occupation=self.__occupation__,
            iq=self.__iq__,
            hobbies=self.__hobbies__,
            education=self.__education__,
            contact_number=self.__contact_number__,
            identity=self.__identity__,
            body_mark=self.__body_mark__,
            signature_scans=self.__signature_scans__,
            date_of_birth=self.__date_of_birth__,
        )
        return human
