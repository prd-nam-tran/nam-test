from django.db import models


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField(null=False)
    total_price = models.DecimalField(null=False)
    product_id = models.IntegerField(null=False, db_index=True)

    def __init__(self, _id, quantity, total_price, product_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = _id
        self.quantity = quantity
        self.total_price = total_price
        self.product_id = product_id
