"""
Abstraction is bascially hiding the methods inside a baseclass.
A user using this method do not really have to know the intricate details of it.
This way we provide the user with a functionality, however prevent them from understanding it
"""


class Number:
    def __init__(self, number):
        if type(number) in [int, float]:
            self.number = number
        else:
            raise TypeError(
                f"Given value {number} is of type {type(number)}. We expect 'class <int>' or 'class <float>'."
            )

    def iseven(self):
        return self.number % 2 == 0


our_number = Number(12.46)
print(our_number.iseven())

"""
With abstraction however the user is now tempted to change the hidden elements.
For example, the user may now override the iseven function to always be true.
"""

our_number.iseven = True
print(our_number.iseven)

"""
One way to prevent this is to create a private variable and method.
Python has no true privacy. So we use a _name. This however is just a convention.
It doesn't prevent someone from overwriting the 'private _' methods or attributes.
"""


class PrivateExample:
    def __init__(self, param):
        self._param = param

    def _method(self):
        print("Private method")


peo = PrivateExample(3)
print(peo._param)
print(peo._method())

peo._param = "Hi"
peo._method = "Modified"
print(peo._param, peo._method) 
