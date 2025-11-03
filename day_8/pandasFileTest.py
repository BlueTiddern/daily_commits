import pandas as pd
import os

class PandasFile:

    def __init__(self, filename):
        self.filename = filename

    def file_read(self):

        exist_flag = os.path.exists(self.filename)

        if exist_flag:
            sony_df = pd.read_csv(self.filename)
            print("##############################################\nThe first 5 row of the data frame are\n##############################################")
            print(sony_df.head())
            print("----------------------------------------------")
        else:
            print("file not exist")

    def clean_csv(self):

        exist_flag = os.path.exists(self.filename)

        if exist_flag:
            sony_df = pd.read_csv(self.filename)
            print("##############################################\nDropping null values and filling null values\n##############################################\n")
            print(f"Counting the null values in all columns : {sony_df.isna().sum()}")
            print("\nDropping rows where the platform has nulls")
            df_drop = sony_df.dropna(subset=["platforms"])
            print(f"Count after the dropping of nulls from platform: {df_drop["platforms"].isna().sum()}")
            print("**********************************************")
            print("Filling the null values in the platform column")
            df_fill = sony_df.fillna({"platforms":"UNKNOWN"})
            print(f"Count after filling the null values : {df_fill["platforms"].isna().sum()}")
            print("----------------------------------------------")

        else:
            print("file not exist")

    def rename_csv(self):

        exist_flag = os.path.exists(self.filename)

        if exist_flag:
            sony_df = pd.read_csv(self.filename)
            print("##############################################\nThe columns present in the csv are\n##############################################")
            print(sony_df.columns.tolist())
            print("\nRenaming the column - 'Japan Sales' to 'JP_Sales'")
            df_rename = sony_df.rename(columns={"Japan Sales":"JP_Sales"})
            print("----------------------------------------------")
            print(f"Below is the list of the columns after renaming : \n{df_rename.columns.tolist()}")
            print("----------------------------------------------")
        else:
            print("file not exist")


if __name__ == '__main__':
    obj = PandasFile('sony_data.csv')
    obj.file_read() # reading the file
    obj.clean_csv() # cleaning the file
    obj.rename_csv()

