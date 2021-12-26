import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Breno', email='breno.eustaq@gmail.com'),
            Usuario(nome='Walter', email='wartinho@hotmail.com')
         ],
[
            Usuario(nome='Breno', email='breno.eustaq@gmail.com')
        ]
    ]
)

def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador=EnviadorMock()
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'breno.eustaq@gmail.com',
        'Teste de Spam',
        'Será que tá funcionando essa parada?'
    )
    assert len(usuarios) == enviador.qtd_email_enviados



def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Breno', email='breno.eustaq@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'wartinho@hotmail.com',
        'Teste de Spam',
        'Será que tá funcionando essa parada?'
    )
    assert enviador.parametros_de_envio == (
        'wartinho@hotmail.com',
        'breno.eustaq@gmail.com',
        'Teste de Spam',
        'Será que tá funcionando essa parada?'
    )