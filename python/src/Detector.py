from Geometry import Geometry


class Detector:
    def __init__(self, configFile, selfDataset) -> None:
        self._geometry = Geometry(self._configFile.problemSize)
        self._selfDataset = selfDataset