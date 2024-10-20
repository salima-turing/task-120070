import unittest
from parameterized import parameterized


class TestProfitabilityAnalysis(unittest.TestCase):
    @parameterized.expand([
        ("scenario_1", 0.15, 0.16, 0.01),
        ("scenario_2", 0.20, 0.18, 0.02),
        ("scenario_3", 0.08, 0.08, 0.005),
        # Add more scenario tuples as needed
    ])
    def test_profit_rate_tolerance(self, scenario_name, actual_profit_rate, expected_profit_rate, tolerance_threshold):
        """
        Test profit rate calculation with tolerance threshold for various scenarios.
        """
        difference = abs(actual_profit_rate - expected_profit_rate)
        self.assertLessEqual(difference, tolerance_threshold,
                             msg=f"Profit rate difference exceeds tolerance for {scenario_name}. "
                                 f"Expected: {expected_profit_rate:.2f}, "
                                 f"Actual: {actual_profit_rate:.2f}, "
                                 f"Tolerance: {tolerance_threshold:.2f}")


if __name__ == '__main__':
    unittest.main()
