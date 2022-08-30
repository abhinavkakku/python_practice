from datetime import date


class Student:
    passing_percentage = 80

    def __init__(self, name, age, percentage):
        self.name = name
        self.age = age
        self.percentage = percentage

    def studentDetails(self):
        print(f'Name : {self.name}')
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

    # @staticmethod
    def isTeen(self):
        if self.age < 19:
            print("is Teen")
        else:
            print(" not Teen")


s1 = Student(name='Abhinav', age=28, percentage=72)
s2 = Student('Abhinav Kumar', 29, 70)
s3 = Student.fromBirthyear('Abhinav Kakku', 1995, 65)
s1.studentDetails()
s2.studentDetails()
s3.studentDetails()
s1.passed()
s1.welcomeMsg()
s1.isTeen()
