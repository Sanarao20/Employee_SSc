import requests
import json
import time
from utils import normalize_employee_data, format_date

API_URL = "https://api.slingacademy.com/v1/sample-data/files/employees.json"  
MAX_RETRIES = 3
TIMEOUT = 5


def fetch_employee_data(url=API_URL):
    """Fetch employee data from API with retries"""
    retries = 0

    while retries < MAX_RETRIES:
        try:
            response = requests.get(url, timeout=TIMEOUT)

            if response.status_code == 200:
                return response.json()

            else:
                print(f"Error: Status Code {response.status_code}")
                return None

        except requests.exceptions.Timeout:
            retries += 1
            print("Timeout occurred. Retrying...")
            time.sleep(1)

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    print("Max retries exceeded")
    return None


def process_employee_data(raw_data):
    """Validate, normalize, and format employee data"""
    processed_data = []

    for emp in raw_data:
        try:
            normalized = normalize_employee_data(emp)
            normalized["hire_date"] = format_date(emp.get("hire_date"))
            processed_data.append(normalized)

        except Exception as e:
            print(f"Skipping invalid record: {e}")

    return processed_data


def save_to_json(data, filename="employees_processed.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
