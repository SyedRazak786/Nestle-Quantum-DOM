from src.data.loader import DataLoader
from src.data.validator import DataValidator



loader = DataLoader()


datasets = loader.load_all_datasets()



validator = DataValidator()


validator.validate_all(datasets)