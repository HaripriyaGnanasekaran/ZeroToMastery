'''
Inheritance is a concept where a class can form as a framework. This base class 
can contain all the common functions that can be given up to child nodes. Thus the 
child nodes can inherit all the functionality of the parent class.
'''

class Worker:
    def __init__(self, wallet=0):
        self._wallet = 0

    def receive_salary(self, amount):
        self._wallet += amount
        print(f'Current Balance is: {self._wallet}')

    def pay_expense(self,amount):
        self._wallet -= amount
        print(f"Current Balance is: {self._wallet}")

class Developer(Worker):
    def __init__(self, id, skills):
        super().__init__()
        self._id = id
        self._skills = skills

    def get_skills(self, skill):
        self._skills.append(skill)
        self.receive_salary(2000)

Ram = Developer(25393, ["C++", "Fortran 99"])
Ram.get_skills("Python")
print(Ram._skills)