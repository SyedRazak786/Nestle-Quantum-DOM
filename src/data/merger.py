"""
merger.py
--------------------------------
Merges cleaned Nestlé DOM datasets.

Author: Sirama Avinash
"""

import pandas as pd



class DataMerger:


    def __init__(self):

        print("Nestlé Data Merger initialized.")



    def merge_orders_shipping(
            self,
            orders,
            shipping
    ):

        print("Merging orders with shipping cost...")


        merged = orders.merge(

            shipping,

            left_on=[
                "Plant",
                "ZipCode"
            ],

            right_on=[
                "Plant",
                "TargetZip"
            ],

            how="left"

        )


        print(
            "Orders + Shipping merged:",
            merged.shape
        )


        return merged
    def merge_capacity(
        self,
        dataframe,
        capacity
    ):

        print("Merging inventory capacity...")


        merged = dataframe.merge(

            capacity,

            left_on=[

                "Plant",

                "MaterialNumber",

                "RequestedDeliveryDate"

            ],

            right_on=[

                "LocationID",

                "MaterialID",

                "DATE"

            ],

            how="left"

        )


        print(
            "Capacity merged:",
            merged.shape
        )


        return merged
    def merge_throughput(
        self,
        dataframe,
        throughput
    ):

        print("Merging throughput capacity...")

        merged = dataframe.merge(

            throughput,

            on=[
                "Plant",
                "transportationplanningdate"
            ],

            how="left"

        )

        print(
            "Throughput merged:",
            merged.shape
        )

        return merged
    
    def merge_dock(
    self,
    dataframe,
    dock
    ):

        print("Merging dock capacity...")

        merged = dataframe.merge(
            dock,
            left_on=[
                "Plant",
                "transportationplanningdate"
            ],
            right_on=[
                "Plant",
                "Date"
            ],
            how="left"
        )

    # -------------------------------
    # Fill missing dock information
    # -------------------------------

        dock_columns = [
            "Dock_Capacity",
            "InboundAppointments",
            "TotalAppointments",
            "Dock_Booked",
            "Dock_Remaining"
        ]

        for col in dock_columns:
            if col in merged.columns:
                merged[col] = merged[col].fillna(0)

        text_columns = [
            "Comments",
            "ActiveFlag",
            "isChanged"
        ]

        for col in text_columns:
            if col in merged.columns:
                merged[col] = merged[col].fillna("Unknown")

        print(f"Dock merged: {merged.shape}")

        return merged