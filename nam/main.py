from nam.models.order import Order
from nam.models.product import Product
from nam.models.warehouse import Warehouse
from nam.services.order_service import OrderService
from nam.services.product_service import ProductService

if __name__ == "__main__":
    warehouse = Warehouse("Ware House 1", "Da Nang")

    product1 = Product(1, "Product A", 10000, "Red")
    product2 = Product(2, "Product B", 5000, "Black")

    ProductService.add_product(product1)
    ProductService.add_product(product2)

    order1 = Order(1, 5, 50000, 1)
    order2 = Order(2, 2, 20000, 2)
    order3 = Order(3, 3, 30000, 2)

    OrderService.add_order(order1)
    OrderService.add_order(order2)
    OrderService.add_order(order3)

    orders = OrderService().get_order_list()

    print(orders[0].total_price)

    for order in orders:
        print(order.total_price)

