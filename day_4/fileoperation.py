
def read_files(file_name):
    try:
        with open(file_name, mode = 'r') as f:
            text = f.read()
            print(text)
    except FileNotFoundError as e:
        print(f"This file does not exist : {e}")

def write_files_read(file_name):
    with open(file_name, mode = 'w') as f:
        f.write("This is to write into the file.\nHere this file is created to hold the data")
    with open(file_name, mode = 'r') as f:
        string_text = f.read()

    print(string_text)

if __name__ == '__main__':
    print('Execution starting...')
    read_files('nonexist.txt')
    write_files_read('created.txt')




