import pandas as pd
import numpy as np



def version_print():
    print("###########*****############****#############****#########")
    print("Printing the version of : PANDAS && NUMPY")
    print(f"The version of the installed pandas is --> : {pd.__version__}")
    print(f"The version of the installed numpy is --> : {np.__version__}")
    print("###########*****############****#############****#########")

def nump_trial_runs():

    print("Converting a python list to numpy array : ")
    print("------------------------------------------")
    print("single dimensional list to numpy array : ")
    list_sd = [1,2,3]
    print(f"The single dimensional list : {list_sd}")
    print("converting this list to numpy array......")
    arr_sd = np.array(list_sd)
    print(f"The converted array list : {arr_sd}")
    print()
    print()
    print("Multi (2) dimensional list to numpy array : ")
    list_md = [[1,2,3],[4,5,6]]
    print(f"The 2 dimensional list : {list_md}")
    print("converting this list to numpy array......")
    arr_md = np.array(list_md)
    print(f"The converted array list : {arr_md}")
    print("------------------------------------------")
    print("""
    
    # generating an numpy array
    # -> np.arange(start,end,step) This creates a single d numpy array
    # -> np.zeros((tuple)) The tuple passed is the dimensions rows, columns
    # -> np.ones((tuple)) -> np.ones(8) -> generates single d array with 9 values i.e 1's
    
    """)

    print("\n\n#########################################\n\nThe below is a generated numpy array")
    print(np.arange(0,5))
    print()
    print()
    print(np.zeros((4,5)))
    print()
    print()
    print(np.ones(9))
    print("------------------------------------------")

    print("""
    
    # -> linspace(0,5,100) --> 0 to 5 range and 100 indicates the number of values needed between them
    # for example 0 to 5, 10 points needed will return
    
    """)
    print()
    ex_1d_array = np.linspace(0,5,10)
    print(ex_1d_array)

    print("------------------------------------------")
    print()
    print("Below is about creating an identity matrix")
    print("""
    
    # creating an identity martix np.eye(num) -> num represents the num of rows = num of columns
    # The diagonal has all ones in it
    
    """)

    iden_matrix = np.eye(4)
    print()
    print(iden_matrix)

    print("------------------------------------------")

    print("Creating numpy random number arrays")
    print()
    print("# single - d random array")
    single_d_rand = np.random.rand(4)
    print(f"This is a single d rand array \n{single_d_rand}")
    print("# 2-d random array")
    two_d_rand = np.random.rand(4,3)
    print(f"This is a two d rand array \n{two_d_rand}")

    print("------------------------------------------")
    print()
    print("Creating an array of random int within a range")
    rand_arr = np.random.randint(1,100,6)
    print()
    print()
    print(f"The below is the random 1 d array for \n{rand_arr}")
    print("------------------------------------------")
    print("""
    
    # reshaping the array using the np.reshape(row, columns), 
      constraint the size of the array must be same as the number of the elements in the array
      
      I.E --> number of elements = rows * columns of the new reshape
    
    """)
    resh_arr = rand_arr.reshape(2,3)
    print(f"The reshaped array 2 * 3 = 6 elements of the 1 d array")
    print(resh_arr)

def arith_ops():

    list_1 = [[1,2,3],[9,8,7]]
    list_2 = [[5,6,12],[18,16,21]]
    arr_1 = np.array(list_1)
    arr_2 = np.array(list_2)
    print("****###########################---##############################****")
    print(f"Array 1 is : {arr_1}")
    print(f"Array 2 is : {arr_2}")

    print("****###########################---##############################****")
    print("Performing the basic arithmetic operations with numpy arrays\n1. Addition\n2. Subtraction\n3. Multiplication\n 4. Division")
    print("****###########################---##############################****")
    print(".....Addition")
    arr_add = arr_1 + arr_2
    print(f"Result : \n{arr_add}")
    print(".....Subtraction")
    arr_sub = arr_2 - arr_1
    print(f"Result : \n{arr_sub}")
    print(".....Multiplication")
    arr_mul = arr_1 * arr_2
    print(f"Result : \n{arr_mul}")
    print(".....Subtraction")
    arr_div = arr_2 / arr_1
    print(f"Result : \n{arr_div}")

if __name__ == "__main__":
    version_print()
    nump_trial_runs()
    arith_ops()

