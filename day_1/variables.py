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
        print(f"Hi my name is {self.name}")
        print('################################################################')
        print(f"This is my age {self.age}")
        print('################################################################')
        print(f"This is my salary{self.salary}")




