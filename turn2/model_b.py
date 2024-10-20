import unittest
from parameterized import parameterized

class TestProfitabilityAnalysis(unittest.TestCase):

    @parameterized.expand([
        (0.15, 0.16, 0.01, "Pass"),
        (0.17, 0.16, 0.01, "Fail"),  # Actual rate is higher than expected
        (0.13, 0.16, 0.01, "Fail"),  # Actual rate is lower than expected
        (0.145, 0.15, 0.005, "Pass"),  # Tolerance threshold is adjusted
    ])
    def test_profit_rate_tolerance(self, actual_profit_rate, expected_profit_rate, tolerance_threshold, expected_result):
        """
        Test profit rate calculation with tolerance threshold.
        """
        # Calculate the actual profit rate based on your data profitability analysis logic
        # actual_profit_rate is now a parameter passed from the test case

        # Set the expected profit rate and the tolerance threshold
        # expected_profit_rate and tolerance_threshold are now parameters

        # Check if the actual profit rate falls within the tolerance range
        difference = abs(actual_profit_rate - expected_profit_rate)
        if difference <= tolerance_threshold:
            result = "Pass"
        else:
            result = "Fail"

        # Compare the result with the expected result
        self.assertEqual(result, expected_result,
                         msg=f"Profit rate test failed. "
                             f"Expected: {expected_result}, "
                             f"Actual Result: {result}, "
                             f"Expected Profit Rate: {expected_profit_rate:.2f}, "
                             f"Actual Profit Rate: {actual_profit_rate:.2f}, "
                             f"Tolerance: {tolerance_threshold:.2f}")

if __name__ == '__main__':
    unittest.main()
