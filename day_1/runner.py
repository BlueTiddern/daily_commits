# module imports

from variables import Variable

def main_entry():
    print("Enter the name:\n ")
    name = input()
    print('---------------------------------')
    print("Enter the age:\n")
    age = input("Enter an integer only: ")
    print('---------------------------------')
    print("Enter the salary:\n")
    salary = input("Enter a double value: $")
    print()
    cls_obj = Variable(name,age,salary)
    print('################################################################')
    cls_obj.plain_print()
    print('################################################################')
    cls_obj.declare_print()
    print('################################################################')

if __name__ == '__main__':
    main_entry()