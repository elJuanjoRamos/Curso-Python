from Order import Order
from Product import Product

product = Product('Camisa', 100.00)
product2 = Product('Pantalon', 150.00)
product3 = Product('Calcetin', 50.00)
product4 = Product('Sueter', 30.00)

productos = [product, product2]
productos2 = [product3, product4]

order = Order(productos)
order2 = Order(productos2)

print([3,5,7]+[3,7,5])
