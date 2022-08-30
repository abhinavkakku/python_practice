from datetime import date


class Student:
    passingPercentage = 75

    # self is instance that will be passed throughout the class
    def __init__(self, name, age, percentage):
        self.name = name  # if only name is used without self, the socpe is limited to function only and cannot be use by other functions in class
        print('Name = ', self.name)
        self.percentage = percentage
        print('Percentage = ', self.percentage)
        self.age = age
        pass

    def studentDetails(self):
        print('Name : ', self.name)
        print('Age : ', self.age)
        print('Percentage : ', self.percentage)

    @classmethod
    def fromBirthYear(cls, name, year, percentage):
        return cls(name, date.today().year - year, percentage)

    def isPassed(self):
        # self.percentage if without self canot be accessed , as percentage is defined in other function above
        if self.percentage > Student.passingPercentage:
            print("Student is Passed")
        else:
            print('Student is not passed')

    @staticmethod  # we declare this way this is static method, else it,
    def welcomeToSchool():  # This is a static method that ideally does not takes instance or ... if static is not mentioned, it will pass self by default which will result into error
        # if we pass self to function still, it will ask for self as required argument
        print("Hey ! Welcome to School")

    @staticmethod
    def isTeen(age):
        return age > 16


s1 = Student('Abhinav', 27, 72,)


s2 = Student.fromBirthYear('Abhinav', 1995, 85)


print(s1.studentDetails())
print(s2.studentDetails())
print(s2.__dict__)
print(s2.isTeen(18))
