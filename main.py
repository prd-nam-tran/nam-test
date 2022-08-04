from nam.models.order import Order
from nam.models.warehouse import Warehouse

if __name__ == "__main__":
    warehouse = Warehouse("Ware House 1", "Da Nang")
    order = Order("04/08/2022", 1)
    print(order)
