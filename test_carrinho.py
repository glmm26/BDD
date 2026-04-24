from pytest_bdd import given, parsers, scenarios, then, when

from carrinho import adicionar_produto, criar_carrinho


scenarios("carrinho.feature")


@given("que o carrinho está vazio", target_fixture="estado")
def estado_inicial():
    return {"carrinho": criar_carrinho(), "estoque": 0}


@given(parsers.parse("que há {estoque:d} unidades em estoque"))
def definir_estoque(estado, estoque):
    estado["estoque"] = estoque
    return estado


@when(parsers.parse("eu adicionar {quantidade:d} unidades com preço unitário {preco:d}"))
def adicionar_com_sucesso(estado, quantidade, preco):
    adicionar_produto(estado["carrinho"], quantidade, estado["estoque"], preco)


@when(parsers.parse("eu tentar adicionar {quantidade:d} unidades com preço unitário {preco:d}"))
def tentar_adicionar(estado, quantidade, preco):
    try:
        adicionar_produto(estado["carrinho"], quantidade, estado["estoque"], preco)
    except ValueError as erro:
        estado["carrinho"]["erro"] = str(erro)


@then(parsers.parse("o carrinho deve ter {itens:d} itens"))
def validar_itens(estado, itens):
    assert estado["carrinho"]["itens"] == itens


@then(parsers.parse("o total do carrinho deve ser {total:d}"))
def validar_total(estado, total):
    assert estado["carrinho"]["total"] == total


@then(parsers.parse('deve ocorrer o erro "{mensagem}"'))
def validar_erro(estado, mensagem):
    assert estado["carrinho"]["erro"] == mensagem
