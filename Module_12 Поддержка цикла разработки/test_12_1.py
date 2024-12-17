from runner import Runner
import unittest
class RunnerTest(unittest.TestCase):
    is_frozen = False
    def test_walk(self):
        run1 = Runner("Влад")
        for _ in range(10):
            run1.walk()
        self.assertEqual(run1.distance, 50)

    def test_run(self):
        run1 = Runner("Влад")
        for _ in range(10):
            run1.run()
        self.assertEqual(run1.distance, 101)

    def test_challenge(self):
        run1 = Runner("Влад")
        run2 = Runner("Alphred")
        for _ in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance, run2.distance)

if __name__ == '__main__':
    unittest.main()