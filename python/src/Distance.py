from abc import ABC, abstractmethod


class Distance(ABC):

    def __init__(self, problem_size: int) -> None:
        self.problem_size = problem_size

    @property
    def problem_size(self):
        return self.problem_size

    @problem_size.setter
    def problem_size(self, problem_size):
        self.problem_size = problem_size

    @abstractmethod
    def calculate(self, vector: list, points: list) -> float:
        pass
