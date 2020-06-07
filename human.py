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
    ):
        self.gender = gender
        self.physic = physic
        self.financial_status = financial_status
        self.occupation = occupation
        self.iq = iq
        self.hobbies = hobbies
        self.education = education
        self.contact_number = contact_number
        self.body_mark = body_mark
        self.id = identity
        self.signature_scans = signature_scans
        self.date_of_birth = date_of_birth

    def __str__(self):
        return (
            "gender ="
            + self.gender
            + "physic="
            + self.physic
            + "financial status="
            + self.financial_status
            + "occupation ="
            + self.occupation
            + "iq="
            + self.iq
            + "hobbies ="
            + self.hobbies
            + "education="
            + self.education
            + " concat_number= "
            + self.contact_number
            + "Id= "
            + self.id
            + "body_mark="
            + self.body_mark
            + "signature_scans="
            + self.signature_scans
            + "date_of_birth="
            + self.date_of_birth
        )
