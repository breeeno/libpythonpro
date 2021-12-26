import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


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
    enviador=Enviador()
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'breno.eustaq@gmail.com',
        'Teste de Spam',
        'Será que tá funcionando essa parada?'
    )
    assert len(usuarios) == enviador.qtd_email_enviados
