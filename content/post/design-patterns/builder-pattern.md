---
title: "Builder Pattern"
date: 2020-06-20T10:34:06+05:30
draft: false
---

# Builder Pattern: Building human objects

Let us assume a scenario where in we want to develop a system to store details of all **Humans** on the earth. Let us start quickly from simpler things without wasting much time in what we are going to do. Here I will be gradually creating a system similar to the marvel universe. Starting from very first entity known to all of us **the human-beings** on **Earth**. I have decided to go with python for this. I will start with very basic requirement of our trageted system and will implement it using suitable design pattern. While trying to keep the overall design clean and **SOLID** we may need to restructure many things as and when required. This is my attempt to explore most of the python paradigm starting from OOPs then moving towards many fascinating concepts.

> This blog focuses on basic design pattern the Builder Pattern in python.

Let us start from attributes of human being:
    
When we say human being we visualize some attributes. Like gender, address, physic, financial status, occupation, IQ, hobbies, education, contact number, ID, body mark, signature and so on.

Below is the basic Human Class which could be found in the [human.py](/src/com/samples/oop/human.py)

```
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
        self.gender = gender
        self.physic = physic
        self.financial_status = financial_status
        self.occupation = occupation
        self.iq = iq
        self.hobbies = hobbies
        self.education = education
        self.contact_number = contact_number
        self.body_mark = body_mark
        self.identity = identity
        self.signature_scans = signature_scans
        self.date_of_birth = date_of_birth
        self.name = name

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
            + "identity= "
            + self.identity
            + "body_mark="
            + self.body_mark
            + "signature_scans="
            + self.signature_scans
            + "date_of_birth="
            + self.date_of_birth
            + "name="
            + self.name
        )
```
The above structure is a class which is a file with name human.py. After initalizing the object of this class, memory is allocated from the RAM. Whenever system wants to access this block of memory it needs its definition. For which it refers to its type which in our case is class.Let us initialize the human class.

```
    tony_stark = Human(gender ='Male',
    physic='5.4ft 100 lbs brown hair blue eyes', 
    financial status='very rich',
    occupation ='scientist weapon business', 
    iq = '300', 
    hobbies ='reading discovering', 
    education= 'phd', 
    concat_number= '', 
    Id= 'ASO4389504', 
    body_mark='heat_light', 
    signature_scans='eye', 
    date_of_birth="may 29th, 1970")
```

In order to print the details of our object using print statement we have overwrite a str().This is also known as string representation of object. So now our class is like this. Now on printing the object we get this:
As I said earlier a memory location wherein all these values are saved is the object. So let us see how

> 
    id(tony_stark)
    139989539594592

and whatever is stored in memory to access it our run-time environment must know what structure it is of. So our runtime libs which manages these storage must know the kind of object in order to read it appropriately. To know the type of the object

> type(tony_stark)

<class 'oop.human.Human'>

Now let us dig into some other details of design. As you could see assigning all values to this human class while initializing is hectic. We need to gather so many values during initialization. Let us consider an example, where we are getting individual value of 1000 humans in a loop that too 1 value at a time, then how we will initialize the object. As seen above all variables are public and we don’t need getter setter thus we can access any property anywhere as shown here

> 
    tony_stark = Human()
    tony_stark.gender = gender

The flaw here is we need our property value public. What if our values are not public. Then we will either need setter getter or below is another approach.One thing we can do is save all values and then initialize the object. To avoid these situation a better solution is the builder design. This we use when there are too many properties and we are getting values few at one time and rest at other. So the builder pattern for this is given in [human_builder.py](/src/com/samples/oop/human_builder.py):
``` 
class HumanBuilder(Object):
    def __init__():
        pass

    def name(self, name):
        self.__name = name
        return self

    def gender(self, gender):
        self.__gender = gender
        return self

    def physic(self, physic):
        self.__physic = physic
        return self

    def financial_status(self, financial_status):
        self.__financial_status = financial_status
        return self

    def occupation(self, occupation):
        self.__occupation = occupation
        return self

    def iq(self, iq):
        self.__iq = iq
        return self

    def hobbies(self, hobbies):
        self.__hobbies = hobbies
        return self

    def education(self, education):
        self.__education = education
        return self

    def contact_number(self, contact_number):
        self.__contact_number = contact_number
        return self

    def identity(self, identity):
        self.__identity = identity
        return self

    def body_mark(self, body_mark):
        self.__body_mark = body_mark
        return self

    def signature_scans(self, signature_scans):
        self.__signature_scans = signature_scans
        return self

    def date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth
        return self

    def build()
        human = human(gender = self.__gender,
        name= self.__name, physic = self.__physic,
        financial_status = self.financial_status,
        occupation = self.__occupation, iq = self.iq,
        hobbies = self.__hobbies,
        education= self.__education,
        contact_number = self.__contact_number,
        Id = self.__id,
        body_mark = self.__body_mark,
        signature_scans = self.__signature_scans,
        date_of_birth = self.__date_of_birth)
        return human
```
As you may have noticed that the HumanBuilder is not as per the PEP8‘s suggestions but our Human object is. So the purpose of builder is accomplished without disturbing the PEP8 with respect to our object Human.
Let us go ahead and create some humans:
```
tony_stark_builder = HumanBuilder()
human_builder.name(‘Tony Stark”’)
             .gender(‘Male’)
             .
             .
             .
howard_stark = howard_stark_builder()
howard_stark.name(‘Howard Stark’).gender(‘Male’).occupation(‘’)
maria_stark = Maria_Stark_Builder()
maria_stark_builder.name(‘Maria Stark’).gender(‘Female')
```

As you may have notice there is one major thing lacking here and that is the relations between the humans. Accepting the facts provided by the Science Humans are born from Humans. So how shall we present the relationships. How to answer this question. As we all know the word relation means association with some one. So it obviously requires atleast two same subjects. In our case it is humans. In every relation both associates has some role to play. So we must know the role of the human in that relation. Let us assume all roles in binary relation are left to right. For example to represent relation below could be the code found in [relation.py](/src/com/samples/oop/relation/relation.py):

```
class Relation(Object):
    def __init__(left_entity=None, right_entity=None):
        self.left_entity = left_entity
        self.right_entity = right_entity

    def relation():
        return {"left_entity": self.left_entity, "right_entity": self.right_entity}
```
For Husband Wife relation. It is [here](/src/com/samples/oop/relation/husband_wife.py)
```
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
```
So using our relationship we can use it for our above human example as follows:

> 
    stark_husband_wife = HusbandWife(howard_stark, maria_stark)
    type(stark_husband_wife)
    <class 'oop.relation.husband_wife.HusbandWife'>