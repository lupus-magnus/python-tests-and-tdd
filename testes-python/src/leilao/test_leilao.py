from unittest import TestCase
from dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):

    def setUp(self):
        self.gui = Usuario("Gui")
        self.yuri = Usuario("Yuri")

        self.lance_do_yuri = Lance(self.yuri, 100.0)
        self.lance_do_gui = Lance(self.gui, 150.0)

        self.leilao = Leilao("celular")

    def test_deve_retornar_o_maior_e_menor_valor_de_lances_quando_adicionados_em_ordem_crescente(self):

        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_tiver_so_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_maior_e_menor_valor_devem_funcionar_quando_tiver_mais_de_dois_lances(self):
        vini = Usuario("Vini")

        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_vini)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(200.0, self.leilao.maior_lance)

    # um usuario deve poder propor se nao houver lances ainda
    def test_deve_permitir_propor_lance_caso_nao_haja_lances(self):
        self.leilao.propoe(self.lance_do_gui)
        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances)

    # se o ultimo usuario for diferente, deve permitir propor lance
    def test_deve_permitir_propor_lance_caso_o_ultimo_usuario_seja_diferente(self):

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_yuri)
        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances)

    # se o ultimo usuario for o mesmo, n deve permitir propor lance
    def test_deve_permitir_propor_lance_caso_o_ultimo_usuario_seja_diferente(self):
        try:
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(Lance(self.gui, 250.0))

        except ValueError:
            quantidade_de_lances = len(self.leilao.lances)
            self.assertEqual(1, quantidade_de_lances)
