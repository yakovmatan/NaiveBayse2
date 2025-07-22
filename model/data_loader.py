import pandas as pd

class DataLoader:
    def __init__(self):
        self.df = None

    def load_data(self, path):
        try:
            file_type = path.split('.')[-1]
            if file_type == "csv":
                self.df = pd.read_csv(path)
            elif file_type == "excel":
                self.df = pd.read_excel(path)
            elif file_type == "json":
                self.df = pd.read_json(path)
            else:
                raise ValueError("Unsupported file type.")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")
        except ValueError as ve:
            raise ValueError(f"Value error while loading data: {ve}")
        except Exception as e:
            raise Exception(f"Unexpected error while loading data: {e}")

