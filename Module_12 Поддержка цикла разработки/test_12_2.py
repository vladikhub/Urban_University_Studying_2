from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = False
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        print("dadadasdsa")

    def setUp(self):
        self.run1 = Runner("Усэйн", 10)
        self.run2 = Runner("Андрей", 9)
        self.run3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for place, runner in cls.all_results:
            print(f"На {place} месте {runner}")

    def test_start_run1_run2(self):
        tour = Tournament(90, self.run1, self.run3)
        self.all_results = tour.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == "Ник")

    def test_start_run2_run3(self):
        tour = Tournament(90, self.run2, self.run3)
        self.all_results = tour.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == "Ник")

    def test_start_run1_run2_run3(self):
        tour = Tournament(90, self.run1, self.run2, self.run3)
        self.all_results = tour.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == "Ник")

    # # Дополнительные тесты в том случае,
    # # если подаются бегуны в разной последовательности,
    # # а количество итераций для каждого бегуна будет одинаково,
    # # чтобы пробежать всю дистанцию
    # def test_start_run2_run1(self):
    #     tour = Tournament(35, self.run2, self.run1)
    #     self.all_results = tour.start()
    #     self.assertTrue(self.all_results[max(self.all_results.keys())] == "Андрей")
    #
    # def test_start_run3_run2(self):
    #     tour = Tournament(5, self.run3, self.run2)
    #     self.all_results = tour.start()
    #     self.assertTrue(self.all_results[max(self.all_results.keys())] == "Ник")

if __name__ == '__main__':
    unittest.main()