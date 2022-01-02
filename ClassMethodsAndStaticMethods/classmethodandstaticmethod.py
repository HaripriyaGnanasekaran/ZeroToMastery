class ClassMethod:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    @classmethod
    def class_method(cls, arg1, arg2):
        return arg1 + arg2

    @staticmethod
    def static_method(arg1, arg2):
        return arg1 + arg2

    def normal_method(self):
        return self


# Both class method and static methods can be called without instantiating the class.
print(ClassMethod.class_method(2, 3))
print(ClassMethod.static_method(3, 4))

# However a normal method requires instantiation.
print(ClassMethod(2,3).normal_method())
