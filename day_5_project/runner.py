from project_1 import BasicProject

obj = BasicProject()

if __name__ == '__main__':
    data = obj.user_input()
    obj.csv_store('a_csv',data)
    obj.csv_read('a_csv')
