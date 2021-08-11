import pandas as pd

class Dataset:

    def __init__(self, filename, problemSize) -> None:
        self.filename = filename
        self.problemSize = problemSize

    
    def read_dataset(self):
        dataset = pd.read_csv(self.filename)
        return dataset