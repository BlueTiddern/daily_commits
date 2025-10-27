import os
import csv

class BasicProject:


    def user_input(self):
        print('############*****############*****#############')
        print('Enter your:\n1. Name\n2. Age\n3. salary')
        name = input('Enter your name : ')
        age = int(input('How old are you : '))
        salary = int(input('What salary do you get : '))
        print('############*****############*****#############')
        return name,age,salary


    def csv_store(self,filename,data):

        file_path = f'{filename}.csv'
        headers = ['Name', 'Age', 'Salary']

        # Check if file exists
        file_exists = os.path.exists(file_path)

        # Open in appropriate mode
        mode = 'a' if file_exists else 'w'

        with open(file_path, mode=mode, newline='') as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow(headers)
                print(f"Created new CSV: {file_path} with headers.")

            # Always write the data row
            writer.writerow(list(data))
            print(f"Appended record to {file_path}: {data[0]}, {data[1]}, {data[2]}")

    def csv_read(self,filename):
        try:
            with open(f'{filename}.csv', mode = 'r') as f:
                data_read = f.read()
                print("Below is the content of the file")
                print(data_read)

        except FileNotFoundError as e:
            print(f"The file {filename} you are trying to open is not found\n{e}")




