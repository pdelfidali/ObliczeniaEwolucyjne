from math import log2, ceil


class Assumptions:
    minValue: float
    maxValue: float
    bitsLength: int

    def __init__(self, min_value: float, max_value: float, bits_length: int = None, precision: int = None):
        self.maxValue = max_value
        self.minValue = min_value
        if precision:
            self.precision = precision
            self.bitsLength = ceil(log2((max_value - min_value) * 10 ** precision) + log2(1))
        elif bits_length:
            self.bitsLength = bits_length
        else:
            raise Exception("Value of bits_length or precision must be provided.")
