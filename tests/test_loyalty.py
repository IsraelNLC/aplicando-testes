import unittest
from src.loyalty import calculate_points

class TestLoyaltyEngine(unittest.TestCase):
    def test_calculate_points(self):
        # Testa se os pontos são calculados corretamente
        result = calculate_points(100, 1.5)
        self.assertEqual(result, 150)

    def test_calculate_points_zero(self):
        # Testa o caso de uma campanha de valor zero
        result = calculate_points(0, 1.5)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
