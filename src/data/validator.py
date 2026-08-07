"""
validator.py
--------------------------------
Validates real Nestlé DOM datasets.

Author: Sirama Avinash
"""


class DataValidator:


    def __init__(self):

        print("Nestlé Data Validator initialized.")



    def validate_dataframe(self, dataframe, name):

        """
        Basic dataframe validation.
        """

        print(f"\nValidating {name} dataset...")


        if dataframe.empty:

            raise ValueError(
                f"{name} dataset is empty"
            )


        if dataframe.columns.isnull().any():

            raise ValueError(
                f"{name} contains unnamed columns"
            )


        if dataframe.columns.duplicated().any():

            raise ValueError(
                f"{name} contains duplicate columns"
            )


        print(
            f"{name} basic validation passed ✅"
        )

        return True



    def validate_required_columns(
            self,
            dataframe,
            name,
            required_columns
    ):


        missing = [

            column

            for column in required_columns

            if column not in dataframe.columns

        ]


        if missing:

            raise ValueError(

                f"{name} missing columns: {missing}"

            )


        print(
            f"{name} required columns passed ✅"
        )


        return True



    def validate_all(self, datasets):


        print(
            "\n========== NESTLÉ DATA VALIDATION ==========\n"
        )


        # Orders validation

        self.validate_dataframe(
            datasets["orders"],
            "Orders"
        )


        self.validate_required_columns(

            datasets["orders"],

            "Orders",

            [

                "Plant",

                "MaterialNumber",

                "RequestedDeliveryDate",

                "OrderedQty_converted",

                "ZipCode"

            ]

        )



        # Capacity validation

        self.validate_dataframe(

            datasets["capacity_planning"],

            "Capacity Planning"

        )


        self.validate_required_columns(

            datasets["capacity_planning"],

            "Capacity Planning",

            [

                "LocationID",

                "MaterialID",

                "Available_inventory",

                "TotalDemand"

            ]

        )



        # Shipping validation

        self.validate_dataframe(

            datasets["shipping_cost"],

            "Shipping Cost"

        )


        self.validate_required_columns(

            datasets["shipping_cost"],

            "Shipping Cost",

            [

                "Plant",

                "TargetZip",

                "Shipping_Cost"

            ]

        )



        # Throughput validation

        self.validate_dataframe(

            datasets["throughput_capacity"],

            "Throughput Capacity"

        )


        self.validate_required_columns(

            datasets["throughput_capacity"],

            "Throughput Capacity",

            [

                "Plant",

                "util_case_picks",

                "order_count"

            ]

        )



        # Dock validation

        self.validate_dataframe(

            datasets["dock_capacity"],

            "Dock Capacity"

        )


        self.validate_required_columns(

            datasets["dock_capacity"],

            "Dock Capacity",

            [

                "Plant",

                "Dock_Capacity",

                "Dock_Remaining"

            ]

        )


        print(

            "\nAll Nestlé datasets validated successfully ✅"

        )


        return True