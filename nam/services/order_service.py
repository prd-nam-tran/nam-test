from nam.services.base_service import BaseService
from nam.services.product_service import ProductService


class OrderService(BaseService):
    __order_list = []

    def get_order_list(self):
        return self.__order_list

    @classmethod
    def add_order(cls, order):
        if cls.__validate_before_add(order):
            order.total_price = cls.get_discount(order.total_price)
            cls.__order_list.append(order)

    @classmethod
    def __validate_before_add(cls, order):
        if order.quantity <= 0\
                or order.total_price <= 0\
                or ProductService.get_product_by_id(order.product_id) is None:
            print(ProductService.get_product_by_id(order.product_id))
            return False
        return True

    @staticmethod
    def get_discount(total_price):
        if total_price >= 50000:
            return total_price - total_price * 5 / 100
        return total_price
