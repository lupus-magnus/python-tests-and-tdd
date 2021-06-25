from src.leilao.dominio import Leilao, Usuario
from src.leilao.excecoes import LanceInvalido
import pytest


@pytest.fixture
def matt():
    return Usuario("Matt", 100.0)


@pytest.fixture
def leilao():
    return Leilao("Celular")


def test_deve_subtrair_valor_do_lance_da_carteira_do_usuario(matt, leilao):
    leilao = Leilao("Notebook")
    matt.propoe_lance(leilao, 50.0)

    assert(matt.carteira == 50.0)


def test_deve_permitir_propor_lance_quando_proposta_menor_que_valor_carteira(matt, leilao):
    leilao = Leilao("Notebook")
    matt.propoe_lance(leilao, 0.01)

    assert(matt.carteira == 99.99)


def test_deve_permitir_proposta_se_o_valor_for_igual_ao_da_carteira(matt, leilao):
    leilao = Leilao("Notebook")
    matt.propoe_lance(leilao, 100.0)

    assert(matt.carteira == 0.0)


def test_nao_deve_permitir_lance_maior_que_valor_em_carteira(matt, leilao):
    with pytest.raises(LanceInvalido):

        leilao = Leilao("Notebook")
        matt.propoe_lance(leilao, 200.0)
