import pandas as pd
import os

# Filter row data on a number

# sort the values - [ ORDER BY]

# Group by values - [ GROUP BY ]


class Analytics:

    def __init__(self, filename):
        self.filename = filename

    def file_check(self):

        exist_flag = os.path.exists(self.filename)

        if exist_flag:
            sony_df = pd.read_csv(self.filename)
            print("##############################################\nThe first 5 row of the data frame are\n##############################################")
            print(sony_df.head())
            print(f"Columns of the csv : \n{sony_df.columns.tolist()}")
            print("----------------------------------------------")

            # The filter block

            print(f"Sample of the numeric columns where the filter will be used \n----------------------------------------------\n{sony_df[["Total Sales","NA Sales"]].head(10)}\n")
            filter_df = sony_df[(sony_df["Total Sales"] > 100000) & (sony_df["NA Sales"] > 10000)] # the filter
            print(f"----------------------------------------------\nTotal sales and NA sales after filtering\n----------------------------------------------\n{filter_df[["Total Sales","NA Sales"]]}")

            # The sort block

            print("\nSorting the values....\n")

            df_sort = filter_df.sort_values(by ='Total Sales', ascending= True)

            print(f"----------------------------------------------\nSorted sales value\n----------------------------------------------\n{df_sort[["Total Sales","NA Sales"]]}")

            print(f"Grouping by the publisher names : \n{df_sort[["Publisher"]].head()}")
            df_group = df_sort.groupby('Publisher').sum()
            print(f"----------------------------------------------\nDf After grouping by\n----------------------------------------------\n{df_group.head(10)}")


            # Drop na

            df_cleaned = df_group.dropna()
            # Write to CSV
            df_cleaned.to_csv('output.csv', index=False)
        else:
            print("file does not exist not exist")



if __name__ == "__main__":
    obj = Analytics('sony_data.csv')
    obj.file_check()

