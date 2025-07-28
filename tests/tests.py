import pytest

from utils.abstract_report import ReportAverage, ReportUserAgent


@pytest.fixture
def f_handlers():
    return ['/api/context/...', '/api/homeworks/...']


@pytest.fixture
def f_handlers_with_date():
    return ['/api/homeworks/...']


@pytest.fixture
def f_user_agents():
    return ['chrome', 'Mozila', 'yandex']


@pytest.fixture
def f_user_agents_with_date():
    return ['Mozila', 'yandex']


@pytest.fixture
def f_data():
    return [
        {'@timestamp': '2025-06-22T13:57:32+00:00', 'status': 200, 'url': '/api/context/...', 'request_method': 'GET',
         'response_time': 0.024, 'http_user_agent': 'chrome'},
        {'@timestamp': '2025-06-22T13:57:32+00:00', 'status': 200, 'url': '/api/context/...', 'request_method': 'GET',
         'response_time': 0.02, 'http_user_agent': 'chrome'},
        {'@timestamp': '2025-06-22T13:57:32+00:00', 'status': 200, 'url': '/api/context/...', 'request_method': 'GET',
         'response_time': 0.024, 'http_user_agent': 'chrome'},
        {'@timestamp': '2024-08-21T13:57:32+00:00', 'status': 200, 'url': '/api/homeworks/...', 'request_method': 'GET',
         'response_time': 0.06, 'http_user_agent': 'Mozila'},
        {'@timestamp': '2024-08-21T13:57:32+00:00', 'status': 200, 'url': '/api/homeworks/...', 'request_method': 'GET',
         'response_time': 0.032, 'http_user_agent': 'yandex'}
    ]


@pytest.fixture
def f_report_average(f_data, f_handlers):
    return ReportAverage(f_data, f_handlers)


@pytest.fixture
def f_report_average_with_date(f_data, f_handlers_with_date):
    return ReportAverage(f_data, f_handlers_with_date)


@pytest.fixture
def f_report_user_agent(f_data, f_handlers, f_user_agents):
    return ReportUserAgent(f_data, f_handlers, f_user_agents)


@pytest.fixture
def f_report_user_agent_with_date(f_data, f_handlers_with_date, f_user_agents_with_date):
    return ReportUserAgent(f_data, f_handlers_with_date, f_user_agents_with_date)


def test_generate_average_report_all(f_report_average):
    result = f_report_average.generate_report()
    assert result == [
        {'/api/context/...': [{'total': 3}, {'avg_response_time': 0.023}]},
        {'/api/homeworks/...': [{'total': 2}, {'avg_response_time': 0.046}]}
    ]


def test_generate_average_report(f_report_average_with_date):
    result = f_report_average_with_date.generate_report('2024-08-21')
    assert result == [{'/api/homeworks/...': [{'total': 2}, {'avg_response_time': 0.046}]}]


def test_generate_user_agent_all(f_report_user_agent):
    result = f_report_user_agent.generate_report()
    assert result == [
        {'/api/context/...': [{'total': 3}, {'user_agent': [{'chrome': 3}, {'Mozila': 0}, {'yandex': 0}]}]},
        {'/api/homeworks/...': [{'total': 2}, {'user_agent': [{'chrome': 0}, {'Mozila': 1}, {'yandex': 1}]}]}
    ]


def test_generate_user_agent(f_report_user_agent_with_date):
    result = f_report_user_agent_with_date.generate_report('2024-08-21')
    assert result == [{'/api/homeworks/...': [{'total': 2}, {'user_agent': [{'Mozila': 1}, {'yandex': 1}]}]}]
