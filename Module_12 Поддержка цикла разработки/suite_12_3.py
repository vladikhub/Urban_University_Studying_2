from test_12_1 import RunnerTest
from test_12_2 import TournamentTest
import unittest

tests_suite = unittest.TestSuite()
tests_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
tests_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tests_suite)