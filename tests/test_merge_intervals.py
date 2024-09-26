import unittest

from core.merge_intervals import merge_intervals
from models.types import Interval


# Klasse zum Testen der Funktion merge_intervals
class TestMergeIntervals(unittest.TestCase):
    def setup_intervals(self, intervals):
        return [Interval(start=interval[0], end=interval[1]) for interval in intervals]

    # Normale Eingabe mit Überlappungen
    def test_normal_input(self):
        intervals = self.setup_intervals([[25, 30], [2, 19], [14, 23], [4, 8]])
        expected_output = self.setup_intervals([[2, 23], [25, 30]])
        self.assertEqual(merge_intervals(intervals), expected_output)

    # Leere Eingabe
    def test_empty_input(self):
        intervals = []
        expected_output = []
        self.assertEqual(merge_intervals(intervals), expected_output)

    # Keine überlappenden Intervalle
    def test_no_overlap(self):
        intervals = self.setup_intervals([[1, 2], [3, 4], [5, 6]])
        expected_output = self.setup_intervals([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(merge_intervals(intervals), expected_output)

    # Alle Intervalle überlappen
    def test_all_overlap(self):
        intervals = self.setup_intervals([[1, 5], [2, 6], [3, 7], [4, 8]])
        expected_output = self.setup_intervals([[1, 8]])
        self.assertEqual(merge_intervals(intervals), expected_output)

    # Ein einziges Intervall
    def test_single_interval(self):
        intervals = self.setup_intervals([[1, 5]])
        expected_output = self.setup_intervals([[1, 5]])
        self.assertEqual(merge_intervals(intervals), expected_output)

    # Überlappende und nicht überlappende Intervalle
    def test_mixed_intervals(self):
        intervals = self.setup_intervals([[1, 3], [8, 10], [2, 6], [15, 18], [17, 20]])
        expected_output = self.setup_intervals([[1, 6], [8, 10], [15, 20]])
        self.assertEqual(merge_intervals(intervals), expected_output)

    # Ungültige Intervalle
    def test_invalid_intervals(self):
        with self.assertRaises(ValueError):
            intervals = self.setup_intervals(
                [[1, 5], [7, 3]]
            )  # Endpunkt kleiner als Startpunkt
            merge_intervals(intervals)

    # Negative Intervalle
    def test_negative_intervals(self):
        with self.assertRaises(ValueError):
            intervals = self.setup_intervals([[-1, 5], [7, 10]])
            merge_intervals(intervals)


# Unit-Tests ausführen
if __name__ == "__main__":
    unittest.main()
