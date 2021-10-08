from Result import Result


class DetectionStage:
    def __init__(self, dataset, config_file) -> None:
        self.dataset = dataset
        self._config_file = config_file

    def matches(self, vector: list, dataset: list, minDist: int) -> bool:
        for it in dataset:
            dist: float = self.euclideanDistance(vector, it)
            if dist <= minDist:
                return True
        return False

    def print_expected_detected(self, config_expected_detected):
        print("Expected to be detected: ", end='')
        for it in config_expected_detected:
            print(it, end='')
            it += 1
            if it != config_expected_detected[-1]:
                print(",", end=' ')

    def print_found(self, detected: set, config_expected_detected):
        print("\nFound: ", end='')
        for it in detected:
            print(it, end='')
            it += 1
            if it != config_expected_detected[-1]:
                print(",", end=' ')

    def remove_found_from_expected_detected(self, detected: set, expected_detected):
        for it in detected:
            for found in expected_detected:
                if it == found:
                    expected_detected.remove(found)
                    break

    def remove_found_from_detected(self, detected: set, expected_detected):
        for it in expected_detected:
            for found in detected:
                if it == found:
                    detected.remove(found)
                    break

    def apply_detectors(self, detectors: list) -> Result:
        detected = set()
        config_expected_detected = self._config_file.expected_detected
        trial = 1
        for it in self._selfDataset:
            actual: bool = self._geometry.matches(
                it, detectors, self._config_file.minDist)
            expected: bool = self._geometry.matches(
                it, self._selfDataset, self._config_file.minDist)
            if actual == expected:
                detected.add(trial)
            trial += 1

        self.print_expected_detected(config_expected_detected)
        self.print_found(detected, config_expected_detected)

        expected_detected = set(config_expected_detected)
        expected_detected_size = len(expected_detected)
        self.remove_detected(detected, expected_detected)
        new_expected_detected_size = len(expected_detected)

        result = Result()
        result.calculate_DR(expected_detected_size, new_expected_detected_size)

        expected_detected.clear()
        expected_detected = [value for value in config_expected_detected]
        self.remove_found_from_detected(detected, expected_detected)
        new_detected_size = len(detected)
        result.calculate_FAR(expected_detected_size, new_detected_size) 
        return result
