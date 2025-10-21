# Task is to print different variables


# Text, int, floating numbers

# Declare variables for name, age and salary

###############################################################
# Below code snippet does it
################################################################


class Variable:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary



    def plain_print(self):
        print('################################################################')
        print('This function just prints the data types\n-int\n-string\n-float')
        print('################################################################')
        print(f'This is a string ->' + '  Hello Im a string')
        print('################################################################')
        print(f'This is a number : {1}')
        print('################################################################')
        print(f'This is a double value : {1.23}')


    def declare_print(self):
        print('This is the function that prints the declared values\n-name\n-age\n-salary')
        print('################################################################')
        print(f"Hi {self.name}, response recorded")
        print('################################################################')
        print(f"Your age is recorded as {self.age}")
        print('################################################################')
        print(f"Your salary is recorded as {self.salary}")
        print('################################################################')
        print(f"WELCOME {self.name}, I see you are {self.age} old, hope you have a good time")




