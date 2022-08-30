class Student:
    def __init__(self, name, rollNumber):  # declare the arguments any instance object will take
        # this helps to assign must have attributes, class object cannot go without these attributes
        self.name = name  # self.name = name will take the name argument passed
        # self.rollNumber = rollNumber will take the rollNumber argument passed
        self.rollNumber = rollNumber
    pass


'''s1 = Student()
print(s1.__dict__)'''


s1 = Student('Abhinav', 2)
print(s1.__dict__)

# s2 = Student()   #since no arguments are given, this will throw error of missing positional arguments

# if positional args are not specified in order, it will take as defined
s2 = Student(rollNumber=3, name='test')
print(s2.__dict__)
