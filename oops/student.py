class student:
    # pass   mention pass when want to declare empty class
    pass


s1 = student()
s2 = student()
s3 = student()

print(s1, s2, s3)
print(type(s1))


s1.name = "Abhinav"
print(s1.name)
s2.rollno = 1
s3.name = "Ayushi"
s3.rollno = 2

print(s3.name)


print(s1.__dict__)  # check available attributes in dictionary
print(s2.__dict__)
print(s3.__dict__)


# check available attributes
print(hasattr(s1, 'name'))

# get an attribute
print(getattr(s1, 'name'))


# if getattr error, pass 3rd arg if not present
print(getattr(s1, 'rollno', '12'))

# delete attribute

delattr(s1, 'name')
print(s1.__dict__)
