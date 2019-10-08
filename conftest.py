import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def lang(request):
    lang = request.config.getoption("language")
    if lang:
        print("\nstart test with lang: {}".format(lang))
    else:
        raise pytest.UsageError("--language should not be empty")
    yield lang