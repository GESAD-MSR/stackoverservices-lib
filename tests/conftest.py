from pathlib import Path
from pytest import fixture


@fixture
def test_root() -> Path:

    return Path(__file__).parent.resolve()