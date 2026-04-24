# language: pt
Funcionalidade: Carrinho de compras

  Cenário: Adicionar um produto com sucesso
    Dado que o carrinho está vazio
    E que há 10 unidades em estoque
    Quando eu adicionar 2 unidades com preço unitário 50
    Então o carrinho deve ter 2 itens
    E o total do carrinho deve ser 100

  Cenário: Tentar adicionar um produto sem estoque suficiente
    Dado que o carrinho está vazio
    E que há 3 unidades em estoque
    Quando eu tentar adicionar 5 unidades com preço unitário 20
    Então deve ocorrer o erro "Estoque insuficiente"
    E o total do carrinho deve ser 0
