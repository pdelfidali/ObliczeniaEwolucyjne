from unittest import TestCase
from Assumptions import Assumptions


class TestAssumptions(TestCase):
    def test_calculating_bits_length_from_precision(self):
        assumptions = Assumptions(-10, 10, precision=6)
        self.assertEqual(25, assumptions.bitsLength)
