import pandas as pd

class Dataset:
    
    def __init__(self, filename, problemSize) -> None:
        self._filename = filename
        self._problemSize = problemSize

    def readDataset(self):
        df = pd.read_csv(self._filename)
        return df