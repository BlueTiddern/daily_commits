

from poke_Extract import extract
from poke_Transform import transform
from poke_Load import load


def etl_pipeline():

    print("Starting the data extract from Pokemon Web......\n")
    print("------------------------------------------------")
    print("*********---------*************----------*******")
    extract()
    print("data is extracted......")
    print("------------------------------------------------")
    print("*********---------*************----------*******")
    print("\nTransforming the data.......\n")
    transform()
    print("\nData is transformed.........\n")
    print("------------------------------------------------")
    print("*********---------*************----------*******")
    print("\nloading the data into sqlite DB.............\n")
    load()
    print("------------------------------------------------")
    print("*********---------*************----------*******")
    print("\nData is loaded pipeline ends.......")

if __name__ == '__main__':
    etl_pipeline()
