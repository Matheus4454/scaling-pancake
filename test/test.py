from src.main import *
from unittest.mock import patch


def test_root():
    result = read_root()
    yield  result
    assert result == {"message": "Olá Mundo!"}


def test_read_item(item_id: int, q: str | None = None):
    result = read_item()
    yield result
    assert result == {"item_id": item_id, "q": q}

# 127.0.0.1:8000/teste1
def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()
        yield result

    assert result == {"teste": True, "numero_aleatorio": 12345}
