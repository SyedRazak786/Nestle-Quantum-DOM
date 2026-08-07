"""
feature_engineering.py
--------------------------------
Prepares the master dataset for AI models.

Responsibilities
----------------
1. Remove unnecessary columns
2. Handle missing values
3. Encode categorical features
4. Select input features
5. Prepare target variable

Author: Sirama Avinash
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


class AIFeatureEngineer:

    def __init__(self):

        print("AI Feature Engineering initialized.")

    def prepare_dataset(self, dataframe, target_column):

        print("\n========== AI FEATURE ENGINEERING ==========\n")

        df = dataframe.copy()

        # ----------------------------------
        # Remove identifier columns
        # ----------------------------------

        columns_to_drop = [

            "Group_Flag",
            "LoadNumber",
            "RequestedDeliveryDate",
            "transportationplanningdate"

        ]

        existing_columns = [

            col for col in columns_to_drop
            if col in df.columns

        ]

        df = df.drop(columns=existing_columns)

        print(f"After removing identifiers : {df.shape}")

        # ----------------------------------
        # Check target column
        # ----------------------------------

        if target_column not in df.columns:

            raise ValueError(
                f"{target_column} not found in dataset."
            )

        # ----------------------------------
        # Remove rows where target is missing
        # ----------------------------------

        before_rows = len(df)

        df = df.dropna(
            subset=[target_column]
        ).reset_index(drop=True)

        removed_rows = before_rows - len(df)

        print(f"Removed rows with missing target : {removed_rows}")

        # ----------------------------------
        # Fill missing numeric values
        # ----------------------------------

        numeric_columns = df.select_dtypes(
            include=["number"]
        ).columns

        for col in numeric_columns:

            if col != target_column:

                df[col] = df[col].fillna(
                    df[col].median()
                )

        # ----------------------------------
        # Fill missing categorical values
        # ----------------------------------

        categorical_columns = df.select_dtypes(
            include=["object"]
        ).columns

        for col in categorical_columns:

            df[col] = df[col].fillna("Unknown")

        print("Missing values handled.")

        # ----------------------------------
        # Encode categorical columns
        # ----------------------------------

        encoder = LabelEncoder()

        categorical_columns = df.select_dtypes(
            include=["object"]
        ).columns

        for column in categorical_columns:

            df[column] = encoder.fit_transform(
                df[column].astype(str)
            )

        print(
            f"Encoded categorical columns : "
            f"{len(categorical_columns)}"
        )

        # ----------------------------------
        # Prepare Features & Target
        # ----------------------------------

        X = df.drop(columns=[target_column])

        y = df[target_column]

        print(f"Features Shape : {X.shape}")
        print(f"Target Shape   : {y.shape}")

        # ----------------------------------
        # Return cleaned dataset
        # ----------------------------------

        return df, X, y