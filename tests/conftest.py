import pytest

@pytest.fixture(scope="session")
def load_env():
    from dotenv import load_dotenv
    load_dotenv()
