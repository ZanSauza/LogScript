import pytest

from utils.abstract_report import ReportAverage

@pytest.fixture
def report_average():
    return [{'/api/context/...': [{'total': 21}, {'avg_response_time': 0.043}]}, {'/api/homeworks/...': [{'total': 71}, {'avg_response_time': 0.158}]}, {'/api/specializations/...': [{'total': 6}, {'avg_response_time': 0.035}]}, {'/api/users/...': [{'total': 1}, {'avg_response_time': 0.072}]}, {'/api/challenges/...': [{'total': 1}, {'avg_response_time': 0.056}]}]

def test_generate_report_all(report_average):
    result = report_average.generate_report()