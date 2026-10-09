import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run Chrome in headless=new mode",
    )


@pytest.fixture
def headless(request):
    return request.config.getoption("--headless")
