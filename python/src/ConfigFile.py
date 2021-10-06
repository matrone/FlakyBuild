from pathlib import Path
import configparser

config_dict = configparser.ConfigParser()
config_dict.read(Path('../config/config.ini'))


class ConfigFile:

    def __init__(self, configFileName: str) -> None:
        self._maxDetectors = int(config_dict[configFileName]['maxDetectors'])
        self._minDist = int(config_dict[configFileName]['minDistance'])
        self._amountOfProofs = int(config_dict[configFileName]['runs'])
        self._trainingDatasetCsvFile = config_dict[configFileName]['trainingFile']
        self._testingDatasetCsvFile = config_dict[configFileName]['testingFile']
        self._expectedDetected = list(
            map(int, config_dict[configFileName]['expectedDetected'][1:-1].split(',')))
        self._searchSpace = None
        self._searchSpaceIndex = None
        self._problemSize = int(config_dict[configFileName]['problemSize']
                                )

    @property
    def maxDetectors(self):
        return self._maxDetectors

    @property
    def minDist(self):
        return self._minDist

    @property
    def amountOfProofs(self):
        return self._amountOfProofs

    @property
    def trainingDatasetCsvFile(self):
        return self._trainingDatasetCsvFile

    @property
    def testingDatasetCsvFile(self):
        return self._testingDatasetCsvFile

    @testingDatasetCsvFile.setter
    def testingDatasetCsvFile(self, value):
        self._testingDatasetCsvFile = value

    @property
    def expectedDetected(self):
        return self._expectedDetected

    @property
    def searchSpace(self):
        return self._searchSpace

    def setSearchSpace(self):
        self._searchSpace = [0] * self._problemSize * 2

    def setSearchSpaceIndex(self, value, index):
        self._searchSpace[index] = value

    def getSearchSpaceIndex(self, index):
        return self._searchSpace[index]

    @property
    def problemSize(self):
        return self._problemSize
