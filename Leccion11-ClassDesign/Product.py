class Product:

    contador_productos = 0

    def __init__(self, nombre, precio):
        Product.contador_productos += 1
        self._idProducto = Product.contador_productos
        self._name = nombre
        self._price = precio

    def __str__(self):
        return f'Id Producto: { self._idProducto }, Name: { self._name }, Price: { self._price }'

    @property
    def price(self):
        return self._price


if __name__ == '__main__':
    product = Product('Camisa', 100.00)
    product2 = Product('Pantalon', 150.00)

    print(product)
    print(product2)