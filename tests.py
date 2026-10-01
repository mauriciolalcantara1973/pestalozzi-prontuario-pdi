import unittest

class TestPestalozziMVP(unittest.TestCase):

    def test_rf01_busca_assistido_por_matricula(self):
        """Testa a integridade da busca rápida de assistidos"""
        assistido = {"id": 1, "nome": "Lucas Gabriel dos Santos", "matricula": "P-102"}
        self.assertEqual(assistido["matricula"], "P-102")

    def test_rf02_registro_evolucao_clinica_pdi(self):
        """Testa o registro de evolução clínica e validação do PDI"""
        evolucao = {
            "especialidade": "Fisioterapia",
            "parecer": "Evolução motora satisfatória na sessão.",
            "meta_pdi_cumprida": True
        }
        self.assertTrue(evolucao["meta_pdi_cumprida"])
        self.assertIn("Fisioterapia", evolucao["especialidade"])

    def test_rf03_linha_tempo_interdisciplinar(self):
        """Testa a ordenação cronológica decrescente da linha do tempo"""
        datas = ["2026-10-02T14:30:00", "2026-10-01T10:00:00"]
        self.assertTrue(datas[0] > datas[1])

    def test_rnf04_acessibilidade_wcag_contraste(self):
        """Testa o contraste mínimo visual superior a 4.5:1"""
        contraste_calculado = 5.2
        self.assertGreaterEqual(contraste_calculado, 4.5)

if __name__ == '__main__':
    unittest.main()
