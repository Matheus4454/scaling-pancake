import pytest
from src.main import *
from unittest.mock import patch


@pytest.mark.asyncio
async def test_read_root():
    result = await read_root()
    assert result == {"message": "Olá Mundo!"}


@pytest.mark.asyncio
async def test_read_item():
    result = await read_item(1, None)
    assert result == {"item_id": 1, "q": None}


@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()

    assert result == {"teste": True, "numero_aleatorio": 12345}


@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Ciclano", curso="ADS", ativo=True)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result


@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result


@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result



@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result


@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(5)
    assert result