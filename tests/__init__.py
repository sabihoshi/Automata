# tests/__init__.py
import unittest


def run_all_tests():
    # Default test loader will discover all test cases in current directory and its subdirectories
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('.')

    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)  # You can adjust verbosity parameter as per your needs
    runner.run(test_suite)


# Run all the tests when this script is called
if __name__ == "__main__":
    run_all_tests()
