class ProductService:
    __product_list = []

    @classmethod
    def add_product(cls, product):
        cls.__product_list.append(product)

    @classmethod
    def get_product_by_id(cls, product_id):
        for product in cls.__product_list:
            if product.id == product_id:
                return product
        return None
