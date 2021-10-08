class Nsa:
    def __init__(self, training, detection, results, configs) -> None:
        self.training_stage = training
        self.detection_stage = detection
        self.results = results
        self.config_file = configs

    def run(self):
        for _ in range(self.config_file.amount_of_proofs):
            detectors = self.training_stage.train()
            self.results.append(
                self.detection_stage.applyDetectors(detectors))
        print(f'Detectors: {self.config_file.maxDetectors}/{len(detectors)}')
        print(f'Min. distance: {self.config_file.minDist}')
        print(f'Runs: {self.config_file.amount_of_proofs}')
