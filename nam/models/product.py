from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=50, null=False)
    price = models.DecimalField()
    color = models.TextField(max_length=50, null=False)

    def __init__(self, _id, name, price, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = _id
        self.name = name
        self.price = price
        self.color = color
