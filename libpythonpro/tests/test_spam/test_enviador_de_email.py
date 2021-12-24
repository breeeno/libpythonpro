import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['brenolupi@yahoo.com.br', 'breno.eustaq@gmail.com' ]
)

def test_remetente(destinatario):
    enviador=Enviador()
    resultado = enviador.enviar(
        destinatario,
        'bx.sptf@gmail.com',
        'Teste de Spam de email',
        'Teste p ver se tá funcionando.'
    )

    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['brenolupi', 'breno.eustaq' ]
)

def test_remetente_invalido(remetente):
    enviador=Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'bx.sptf@gmail.com',
            'Teste de Spam de email',
            'Teste p ver se tá funcionando.'
    )

