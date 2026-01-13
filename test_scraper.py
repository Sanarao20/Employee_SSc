import unittest
from unittest.mock import patch
from scraper import fetch_employee_data, process_employee_data

MOCK_API_RESPONSE = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@test.com",
        "phone": "1234567890",
        "gender": "Male",
        "age": 30,
        "job_title": "Engineer",
        "years_of_experience": 6,
        "salary": 80000,
        "department": "IT",
        "hire_date": "2020-01-15"
    }
]


class TestEmployeeScraper(unittest.TestCase):

    # Test Case 1: Verify JSON File Download
    @patch("scraper.requests.get")
    def test_json_download(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_API_RESPONSE

        data = fetch_employee_data("fake_url")
        self.assertIsNotNone(data)

    # Test Case 2: Verify JSON File Extraction
    def test_json_extraction(self):
        processed = process_employee_data(MOCK_API_RESPONSE)
        self.assertEqual(processed[0]["full_name"], "John Doe")

    # Test Case 3: Validate File Type and Format
    def test_file_format(self):
        processed = process_employee_data(MOCK_API_RESPONSE)
        self.assertIsInstance(processed, list)
        self.assertIsInstance(processed[0], dict)

    # Test Case 4: Validate Data Structure
    def test_data_structure(self):
        processed = process_employee_data(MOCK_API_RESPONSE)
        self.assertIn("designation", processed[0])
        self.assertIn("salary", processed[0])

    # Test Case 5: Handle Missing or Invalid Data
    def test_missing_data(self):
        invalid_data = [{"first_name": "John"}]
        processed = process_employee_data(invalid_data)
        self.assertEqual(processed, [])


if __name__ == "__main__":
    unittest.main()
