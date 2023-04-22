import Assumptions
from abc import ABC, abstractmethod


class Gene(ABC):
    binaryRepresentation: str
    decimalRepresentation: float

    @staticmethod
    @abstractmethod
    def generate_random_gene() -> 'Gene':
        pass
