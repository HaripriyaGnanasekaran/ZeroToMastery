"""
Encapsulation is packaging data and functions into attributes and methods. Classes can
be used to achieve this packaging. This process is called as Encapsulation. Encapsulate means
"express the essential features of something succintly".  (Or enclose something in a capsule)
"""


class Human:
    def __init__(self, gender, origin, age, location):
        self.gender = gender
        self.age = age
        self.origin = origin
        self.location = location

    def migrate(self, country):
        print(
            f"Human from {self.origin} currently living in {self.location} wishes to move to {country}."
        )

    def settle(self):
        IsMarried = self.get_married()
        HasHome = self.build_home()
        if IsMarried and HasHome:
            print(f"This human has succesfully settled in {self.location}")
        else:
            print("Can't settle down yet.")

    def get_married(self):
        if self.age > 18:
            print(f"Human with {self.age} is allowed to get married.")
            return True
        else:
            print(f"Too young to get married.")
            return False

    def build_home(self):
        print("Anyone can build a home now.")
        return True


Ram = Human("Male", "India", 29, "Netherlands")
Ram.migrate("New Zeeland")
Ram.settle()

"""
If we do not package this information into a class, everytime we perform a function, we need to pass the arguments.
"""
