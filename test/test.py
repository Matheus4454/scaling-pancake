import pytest

from src.main import *
from unittest.mock import patch

def test_read_root():
    result = read_root()
    assert result == {"message": "Olá Mundo!"}


def test_read_item():
    result = read_item(1, None)
    assert result == {"item_id": 1, "q": None}


@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()

    assert result == {"teste": True, "numero_aleatorio": 12345}
