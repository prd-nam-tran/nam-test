from django.db import models


class Warehouse(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=50, null=False)
    address = models.TextField(max_length=100, null=False)

    def __init__(self, name, address, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.address = address
