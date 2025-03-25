import unittest

# Import all test classes
from page_loading_test import PageLoadingTimeTest
from os_compatibility_test import OperatingSystemTest
from user_authentication_test import UserAuthenticationTest
from user_registration_test import UserRegistrationTest
from weather_api_test import WeatherAPITest
from activity_recommendation_test import ActivityRecommendationTest

def run_tests():
    """
    Run all test suites
    """
    # Create a test suite
    test_suite = unittest.TestSuite()

    # Add test cases to the suite
    test_cases = [
        PageLoadingTimeTest,
        OperatingSystemTest,
        UserAuthenticationTest,
        UserRegistrationTest,
        WeatherAPITest,
        ActivityRecommendationTest
    ]

    for test_case in test_cases:
        test_suite.addTests(unittest.makeSuite(test_case))

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Return True if tests passed, False otherwise
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)