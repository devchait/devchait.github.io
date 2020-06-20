class Human:
    def __init__(
        self,
        gender=None,
        physic=None,
        financial_status=None,
        occupation=None,
        iq=None,
        hobbies=None,
        education=None,
        contact_number=None,
        identity=None,
        body_mark=None,
        signature_scans=None,
        date_of_birth=None,
        name=None,
    ):
        self.__gender__ = gender
        self.__physic__ = physic
        self.__financial_status__ = financial_status
        self.__occupation__ = occupation
        self.__iq__ = iq
        self.__hobbies__ = hobbies
        self.__education__ = education
        self.__contact_number__ = contact_number
        self.__body_mark__ = body_mark
        self.__identity__ = identity
        self.__signature_scans__ = signature_scans
        self.__date_of_birth__ = date_of_birth
        self.__name__ = name

    def __str__(self):
        return (
            "gender ="
            + self.__gender__
            + "physic="
            + self.__physic__
            + "financial status="
            + self.__financial_status__
            + "occupation ="
            + self.__occupation__
            + "iq="
            + self.__iq__
            + "hobbies ="
            + self.__hobbies__
            + "education="
            + self.__education__
            + " concat_number= "
            + self.__contact_number__
            + "identity= "
            + self.__identity__
            + "body_mark="
            + self.__body_mark__
            + "signature_scans="
            + self.__signature_scans__
            + "date_of_birth="
            + self.__date_of_birth__
            + "name="
            + self.__name__
        )
