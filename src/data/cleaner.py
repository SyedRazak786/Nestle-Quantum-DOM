"""
cleaner.py
--------------------------------
Cleans real Nestlé DOM datasets.

Author: Sirama Avinash
"""

import pandas as pd



class DataCleaner:


    def __init__(self):

        print("Nestlé Data Cleaner initialized.")



    def remove_empty_columns(self, dataframe):

        """
        Remove completely empty columns
        and Excel artifacts.
        """

        df = dataframe.copy()


        # Remove unnamed Excel columns

        df = df.loc[
            :,
            ~df.columns.str.contains(
                "^Unnamed"
            )
        ]


        # Remove fully empty columns

        df = df.dropna(
            axis=1,
            how="all"
        )


        return df




    def handle_missing_values(self, dataframe):

        """
        Handle missing values.
        """

        df = dataframe.copy()


        numeric_columns = df.select_dtypes(
            include="number"
        ).columns


        # Numeric missing values -> 0

        df[numeric_columns] = (
            df[numeric_columns]
            .fillna(0)
        )


        categorical_columns = df.select_dtypes(
            include="object"
        ).columns


        # Text missing values

        df[categorical_columns] = (
            df[categorical_columns]
            .fillna("Unknown")
        )


        return df



    def standardize_dates(
            self,
            dataframe,
            date_columns
    ):

        df = dataframe.copy()


        for column in date_columns:

            if column in df.columns:

                df[column] = pd.to_datetime(
                    df[column],
                    errors="coerce",
                    format="mixed"
                )


        return df




    def clean_dataset(
            self,
            dataframe,
            date_columns=[]
    ):


        print("Cleaning dataset...")


        df = dataframe.copy()


        # Remove duplicates

        df = df.drop_duplicates()



        # Remove unwanted columns

        df = self.remove_empty_columns(df)



        # Missing values

        df = self.handle_missing_values(df)



        # Date formatting

        df = self.standardize_dates(
            df,
            date_columns
        )



        print(
            f"Cleaning completed: {df.shape}"
        )


        return df