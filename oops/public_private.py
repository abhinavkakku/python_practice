from datetime import date


class Student:
    passing_percentage = 80

    def __init__(self, name, age, percentage):
        self.__name = name  # if a object or function is prefixxed with __ double underscore, it becomes private and can only be accessd in class
        self.age = age
        self.percentage = percentage

    def studentDetails(self):
        print(f'Name : {self.__name}')
        print(f'Age : {self.age}')
        print(f'Percentage : {self.percentage}')

    @classmethod
    def fromBirthyear(studentclass, name, year, percentage):
        return studentclass(name, date.today().year - year, percentage)

    @staticmethod
    def welcomeMsg():
        print('Welcome to Class')

    def passed(self):
        if self.percentage > Student.passing_percentage:
            print("Student is Passed")
        else:
            print('Student is not passed')

    @staticmethod
    def isTeen(age):
        if age < 19:
            print("is Teen")
        else:
            print(" not Teen")


s1 = Student(name='Abhinav', age=28, percentage=72)
s2 = Student('Abhinav Kumar', 29, 70)
s3 = Student.fromBirthyear('Abhinav Kakku', 1995, 65)
# print(s1.__name) # wont works as private
s1.studentDetails()
s2.studentDetails()
s3.studentDetails()
s1.passed()
s1.welcomeMsg()

# print(s1.__name)  # will not work as private
s1. name = 'AK'
s1.age = 23
print(f'After Changing : {s1.__dict__}')

# print(s1.__name) # wont works as private
# Name_mangling ( not to be used by Devs, private can be accesssed by object._classname__attribute)
print(s1._Student__name)
