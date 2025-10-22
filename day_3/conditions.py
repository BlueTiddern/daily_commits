

class WorkNums:

    def pos_neg_zero(self):
        print("######**********############*********#########")
        print('This function checks what type of number is entered')
        print("######**********############*********#########")
        num = int(input('Enter a number --> :=:  '))

        if num > 0:
            print(f'This number "{num}" is positive')
        elif num < 0:
            print(f'This number "{num}" is negative')
        else:
            print('It is zero')
    def print_nums(self):
        print("######**********############*********#########")
        print("Below print is with FOR loop")
        print("######**********############*********#########")
        for i in range(20):
            i +=1
            print(i)
        j = 1
        print("######**********############*********#########")
        print("Below print is with WHILE loop")
        print("######**********############*********#########")
        while j <= 20:
            print(j)
            j+=1

    def num_sum(self,a,b):
        c = a + b
        print("######**********############*********#########")
        print(f"The sum of {a} and {b} is : {c}")
        print("######**********############*********#########")







