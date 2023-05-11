from unittest import TestCase

from Assumptions import Assumptions


class TestAssumptions(TestCase):
    def test_calculating_bits_length_from_precision(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, precision=6)
        self.assertEqual(25, assumptions.bitsLength)

    def test_assumption_is_singleton(self):
        assumptions = Assumptions()
        assumptions2 = Assumptions()
        self.assertEqual(id(assumptions), id(assumptions2))

    def test_second_assumption_object_keeps_first_data(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, precision=6)
        assumptions2 = Assumptions()
        self.assertEqual(25, assumptions2.bitsLength)
