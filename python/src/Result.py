class Result(object):

    def __init__(self) -> None:
        self.results = []
        self.DR = 0
        self.FAR = 0

    def calculate_DR(self, expected_detected_size: int,
                     new_expected_detected_size: int):
        self.DR = (-(new_expected_detected_size -
                   expected_detected_size) / expected_detected_size)

    def calculate_FAR(
            self,
            expected_detected_size: int,
            new_detected_size: int):
        self.DR = new_detected_size / expected_detected_size

    def get_general_results(self, amount_of_proofs) -> None:
        sumDR: float = 0
        sumFAR: float = 0
        for r in self.results:
            print(f'{r.DR}, {r.FAR}')
            sumDR += 1
            sumFAR += 1
        print(f'Average: {sumDR/amount_of_proofs}')
