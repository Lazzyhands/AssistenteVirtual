import unittest

from assistente import *
AUDIO_CHAT = 'C:/Users/vitin/Desktop/IA/audios_ia/chat_fechar_steam.m4a'
AUDIO_CHAMANDO_OUTRO_NOME = 'C:/Users/vitin/Desktop/IA/audios_ia/chat_gpt.m4a'
AUDIO_LIGAR_GRAVADOR = 'C:/Users/vitin/Desktop/IA/audios_ia/chat_ligar_gravador.m4a'
AUDIO_DESLIGAR_GRAVADOR = 'C:/Users/vitin/Desktop/IA/audios_ia/chat_desligar_gravador.m4a'
AUDIO_INICIAR_STEAM = 'C:/Users/vitin/Desktop/IA/audios_ia/chat_iniciar_steam.m4a'
AUDIO_FECHAR_STEAM = 'C:/Users/vitin/Desktop/IA/audios_ia/chat_fechar_steam.m4a'

class TesteNomeAssistente(unittest.TestCase):
    def setUp(self):
        iniciar()

    def testar_reconhecer_nome(self):
        transcricao = escutar_fala(AUDIO_CHAT)
        transcricao = transcricao.split()

        nome_assistente = ""
        if len(transcricao):
            nome_do_assistente = transcricao[0].lower()
            print(f"nome do assistente: {nome_do_assistente}")

        self.assertIn("chat", nome_do_assistente)

    def testar_nao_reconhecer_outro_nome(self):
        transcricao = escutar_fala(AUDIO_CHAMANDO_OUTRO_NOME)
        transcricao = transcricao.split()

        nome_do_assistente = ""
        if len(transcricao):
            nome_do_assistente = transcricao[0].lower()
            print(f"nome do assistente: {nome_do_assistente}")

        self.assertNotIn("chat", nome_do_assistente)


class TesteGravador(unittest.TestCase):

    def setUp(self):
        iniciar()

    def testar_ligar_gravador(self):
        transcricao = escutar_fala(AUDIO_LIGAR_GRAVADOR)
        print(f"comando reconhecido: {transcricao}")

        acao, objeto = obter_tokens(transcricao)
        valido = validar_comando(acao, objeto)

        self.assertTrue(valido)

    def testar_desligar_desligar(self):
        transcricao = escutar_fala(AUDIO_DESLIGAR_GRAVADOR)
        print(f"comando reconhecido: {transcricao}")

        acao, objeto = obter_tokens(transcricao)
        valido = validar_comando(acao, objeto)

        self.assertTrue(valido)


class TesteSteam(unittest.TestCase):

    def setUp(self):
        iniciar()

    def testar_iniciar_steam(self):
        transcricao = obter_tokens(AUDIO_INICIAR_STEAM)
        print(f"comando reconhecido: {transcricao}")

        acao, objeto = obter_tokens(transcricao)
        valido = validar_comando(acao, objeto)

        self.assertTrue(valido)

    def testar_fechar_steam(self):
        transcricao = obter_tokens(AUDIO_FECHAR_STEAM)
        print(f"comando reconhecido: {transcricao}")

        acao, objeto = obter_tokens(transcricao)
        valido = validar_comando(acao, objeto)

        self.assertTrue(valido)


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeAssistente))
    testes.addTest(carregador.loadTestsFromTestCase(TesteGravador))
    testes.addTest(carregador.loadTestsFromTestCase(TesteSteam))

    executor = unittest.TextTestRunner()
    executor.run(testes)
    
