from random import randint
import random

class DataStructs:
    default_list = [random.randint(1,100) for _ in range(10)]
    default_emp = {'name':'P-0ne', 'age':30, 'salary': 340.45, 'DOJ': '2025-01-01'}
    def even_check(self):
        print("----***-------***--------***")
        print("#############################")
        print('The elements of the list are:')
        for i in self.default_list:
            print(f"Element : {i}")
        print("----***-------***--------***")
        print("#############################")
        print("Even check for the list elements under way.....")
        even_list = [x for x in self.default_list if x%2==0]
        print("Even check done..\nBelow is the even list")
        print("#############################")
        print(even_list)
        print("----***-------***--------***")
        print("#############################")

    def dict_display(self):
        print()
        print()
        print("----***-------***--------***")
        print("#############################")
        print("Key value pairs of the class dictionary are below : \n")
        for key,value in self.default_emp.items():
            print('####################################')
            print(f'# -> {key}  : {value}')
            print('####################################')




