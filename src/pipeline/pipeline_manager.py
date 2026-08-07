"""
pipeline_manager.py
--------------------------------
Runs the complete data pipeline.

Author: Sirama Avinash
"""

from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner
from src.data.merger import DataMerger
from src.data.preprocessing import DataPreprocessor
from src.data.scaler import DataScaler

from src.pipeline.save_dataset import DatasetSaver


class PipelineManager:

    def __init__(self):

        print("\nPipeline Manager initialized.")

    def run(self):

        print("\n========== RUNNING DATA PIPELINE ==========\n")

        loader = DataLoader()

        datasets = loader.load_all_datasets()

        cleaner = DataCleaner()

        orders = cleaner.clean_dataset(
            datasets["orders"],
            [
                "RequestedDeliveryDate",
                "transportationplanningdate"
            ]
        )

        shipping = cleaner.clean_dataset(
            datasets["shipping_cost"]
        )

        capacity = cleaner.clean_dataset(
            datasets["capacity_planning"],
            [
                "DATE",
                "report_date"
            ]
        )

        throughput = cleaner.clean_dataset(
            datasets["throughput_capacity"],
            [
                "transportationplanningdate",
                "Report_Run_Date"
            ]
        )

        dock = cleaner.clean_dataset(
            datasets["dock_capacity"],
            [
                "Date",
                "Modified_Date",
                "SnapshotDate",
                "Report_Run_Date"
            ]
        )

        merger = DataMerger()

        result = merger.merge_orders_shipping(
            orders,
            shipping
        )

        result = merger.merge_capacity(
            result,
            capacity
        )

        result = merger.merge_throughput(
            result,
            throughput
        )

        result = merger.merge_dock(
            result,
            dock
        )

        preprocessor = DataPreprocessor()

        result = preprocessor.preprocess(
            result
        )

        scaler = DataScaler()

        result = scaler.scale(result)

        saver = DatasetSaver()

        saver.save(result)

        print("\n========== PIPELINE COMPLETED ==========\n")

        return result