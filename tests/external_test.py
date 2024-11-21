import unittest
from unittest.mock import patch
from src.external import fetch_campaign_data

class TestExternalService(unittest.TestCase):
    @patch("src.external_service.requests.get")
    def test_fetch_campaign_data_success(self, mock_get):
        # Mocka a API para simular uma resposta bem-sucedida
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "id": "123",
            "name": "Test Campaign",
            "points": 100,
        }

        result = fetch_campaign_data("http://fakeapi.com", "123")
        self.assertEqual(result["name"], "Test Campaign")
        self.assertEqual(result["points"], 100)

    @patch("src.external_service.requests.get")
    def test_fetch_campaign_data_failure(self, mock_get):
        # Mocka a API para simular uma resposta com erro
        mock_get.return_value.status_code = 404

        with self.assertRaises(ValueError) as context:
            fetch_campaign_data("http://fakeapi.com", "999")
        
        self.assertIn("Erro ao buscar campanha", str(context.exception))

if __name__ == "__main__":
    unittest.main()
