from src.main import *
from unittest.mock import patch

def test_root():
    assert read_root() == {"message": "Olá Mundo!"}


def test_read_item(item_id: int, q: str | None = None):
    assert read_item() == {"item_id": item_id, "q": q}

# 127.0.0.1:8000/teste1
def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()

    assert result() == {"teste": True, "numero_aleatorio": 12345}
