import pytest
import json
import os


def pytest_generate_tests(metafunc):
    """Generate test parameters from JSON file for test_credentials_list fixture"""
    if "test_credentials_list" in metafunc.fixturenames:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(current_dir, "Data", "credentials.json")

        with open(data_file) as f:
            test_data = json.load(f)
            test_credentials = test_data["credentials"]

        print(f"Test data loaded from json file in conftest: {test_data}")
        metafunc.parametrize("test_credentials_list", test_credentials)
