import pandas as pd
import numpy as np
import sys
from ConfigFile import ConfigFile
from Dataset import Dataset
from Geometry import Geometry
import Random


def initSearchSpace(configFile):
    configFile.setSearchSpace()
    for i in range(configFile.problemSize):
        configFile.setSearchSpaceIndex(0.0, (2 * i))
        configFile.setSearchSpaceIndex(1.0, (2 * i + 1))


def run(configFile):
    initSearchSpace(configFile)
    trainingDataset = Dataset(configFile.trainingDatasetCsvFile, configFile.problemSize)
    testingDataset = Dataset(configFile.testingDatasetCsvFile, configFile.problemSize)
    selfDatasetForTraining = trainingDataset.readDataset()
    generateSelfDataSetForTesting = testingDataset.readDataset()
    


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        configFile = ConfigFile(filename)
        run(configFile)
    else:
        print(f'Usage {sys.argv[0]} <CONFIG-FILE>')
        return -1

    return 0


if __name__ == '__main__':
    main()
