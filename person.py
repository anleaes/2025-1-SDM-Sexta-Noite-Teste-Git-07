from pedido import Pedido
from produto import Produto

class ItemPedido:
    def __init__(self, quantidade, precoItem, pedido: Pedido, produto: Produto):
        self._quantidade = quantidade
        self._preco_item = precoItem   
        self._pedido = pedido
        self._produto = produto
    
    def __str__(self):
        return f"Quantidade: {self._quantidade}\nPreço do item: {self._preco_item}\nPedido: {self._pedido}\nProduto: {self._produto}"