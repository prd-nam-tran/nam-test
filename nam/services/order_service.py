from nam.services.product_service import ProductService


class OrderService:
    order_service_type = 'Single Order Service'
    order_list = []

    def __init__(self, owner="Nam"):
        self.owner = owner

        # print(f'Get order_list by self ', self.order_list)
        #
        # self.order_list = [1, 2]
        # print(f'Get order_list by self after changing value ', self.order_list)
        # print(f'Get order_list by self.__class__ ', self.__class__.order_list)
        #
        # self.__class__.order_list = [2, 2]
        # print(f'Get order_list by self.__class__ after changing value', self.__class__.order_list)

    def get_order_list(self):
        return self.order_list

    @classmethod
    def add_order(cls, order):
        if cls.__validate_before_add(order):
            order.total_price = cls.get_discount(order.total_price)
            cls.order_list.append(order)

    @classmethod
    def __validate_before_add(cls, order):
        if order.quantity <= 0\
                or order.total_price <= 0\
                or ProductService.get_product_by_id(order.product_id) is None:
            return False
        return True

    @staticmethod
    def get_discount(total_price):
        if total_price >= 50000:
            return total_price - total_price * 5 / 100
        return total_price


if __name__ == '__main__':
    print(OrderService.order_service_type)

    orderService1 = OrderService()
    orderService1.owner = "New Nam"
    print(orderService1.owner)

    print(orderService1.get_order_list())

    orderService1.order_list += [3, 4]
    print(orderService1.order_list)

    print(OrderService.order_list)

    print('--------------------')
    orderService2 = OrderService()
    print(orderService2.get_order_list())
