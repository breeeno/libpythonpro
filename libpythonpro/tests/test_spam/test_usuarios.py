from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Breno', email='breno.eustaq@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Breno', email='breno.eustaq@gmail.com'),
                Usuario(nome='Walter', email='breno.eustaq@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
