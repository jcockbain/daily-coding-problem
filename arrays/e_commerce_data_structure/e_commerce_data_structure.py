class order_array():
    def __init__(self):
        self.orders = []

    def record(self, order_id):
        self.orders.append(order_id)

    def get_last(self, i):
        return self.orders[-i]