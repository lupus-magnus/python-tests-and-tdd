from .excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome: str, valor_carteira: float = 500.0):
        self.__nome = nome
        self.__carteira = valor_carteira

    def propoe_lance(self, leilao, valor):
        if (valor > self.__carteira):
            raise LanceInvalido(
                "O valor proposto não pode ser maior que o que o usuario possui em carteira."
            )
        lance = Lance(self, valor)
        leilao.propoe(lance)
        # se o metodo propoe der exception, o codigo nao entra aqui
        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira


class Lance:

    def __init__(self, usuario: Usuario, valor: float):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao: str):
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances[:]

    def propoe(self, lance: Lance):
        if (not self.__lances) or (self.__lances[-1].usuario != lance.usuario) and lance.valor > self.__lances[-1].valor:
            if not self.__lances:
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor
            self.__lances.append(lance)

        else:
            msg = "Erro ao propor lance:\t"
            if(lance.valor <= self.__lances[-1].valor):
                msg += "A nova proposta deve ser mais alta que as demais"
            else:
                msg += "O mesmo usuario nao pode propor duas vezes seguidas"

            raise LanceInvalido(msg)
