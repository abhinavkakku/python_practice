class Student:
    passingPercentage = 75

    # self is instance that will be passed throughout the class
    def studentDetails(self):
        self.name = 'Abhinav'  # if only name is used without self, the socpe is limited to function only and cannot be use by other functions in class
        print('Name = ', self.name)
        self.percentage = 74
        print('Percentage = ', self.percentage)
        pass

    def isPassed(self):
        # self.percentage if without self canot be accessed , as percentage is defined in other function above
        if self.percentage > Student.passingPercentage:
            print("Student is Passed")
        else:
            print('Student is not passed')

    @staticmethod  # we declare this way this is static method, else it, static method is also called class method as it is not related to other functions
    def welcomeToSchool():  # This is a static method that ideally does not takes instance or ... if static is not mentioned, it will pass self by default which will result into error
        # if we pass self to function still, it will ask for self as required argument
        print("Hey ! Welcome to School")


s1 = Student()
# s1.studentDetails()          # instance_name.function() same as below
# class_name.function(object_name) # This is same as above
Student.studentDetails(s1)


s1.isPassed()
s1.welcomeToSchool()
