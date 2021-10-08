from random import uniform

# TODO terminar implementacao da classe


class TrainingStage:
    def __init__(
            self,
            dataset,
            problem_size,
            max_amount_of_detectors,
            distance) -> None:
        pass

    def get_detector_candidates(self, array_of_detectors: list) -> list:
        for i in range(self._configFile.problemSize):
            array_of_detectors[i] = self._configFile.getSearchSpaceIndex(2 * i)
            + (self._configFile.getSearchSpaceIndex(2 * i + 1) -
               self._configFile.getSearchSpaceIndex(2 * i)) * uniform(0.0, 1.0)
        return array_of_detectors

    def remove_self_detecting_detectors(
            self, detector: list, detectors: list) -> list:
        if not self._geometry.matches(
                detector,
                self._selfDataset,
                self._configFile.minDist):
            if not self._geometry.matches(detector, detectors, 0.0):
                detectors.append(detector)
                detector = [None] * self._configFile.problemSize
                print(f"{len(detectors)}/{self._configFile.maxDetectors}")

        return detectors

    def train(self) -> list:
        detectors = list()
        print("Generating detectors...")
        detector: list = [None] * self._configFile.problemSize
        while len(detectors) < self._configFile.maxDetectors:
            self.get_detector_candidates(detector)
            self.remove_self_detecting_detectors(detector, detectors)
        if detector is not None:
            del detector

        return detectors
