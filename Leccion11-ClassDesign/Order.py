from Product import Product


class Order:
    contador_orden = 0

    def __init__(self, products):
        Order.contador_orden += 1
        self._idOrder = Order.contador_orden
        self._products = list(products)

    def agregar_producto(self, product):
        self._products.append(product)

    def calculate_total(self):
        total = 0
        for product in self._products:
            total += product.price
        return total

    def __str__(self):
        productos_str = '\t'
        for product in self._products:
            productos_str += product.__str__() + '\n\t'
        return f'Orden: { self._idOrder },\nProductos: [ \n{ productos_str } ]'


if __name__ == '__main__':
    product = Product('Camisa', 100.00)
    product2 = Product('Pantalon', 150.00)
    productos = [product, product2]

    order = Order(productos)
    print(order)