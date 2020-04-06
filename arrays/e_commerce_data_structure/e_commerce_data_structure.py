class order_array():
    def __init__(self, n):
        self.orders = []
        self.n = n

    def record(self, order_id):
        if len(self.orders) >= self.n:
            self.orders.pop(0)
        self.orders.append(order_id)

    def get_last(self, i):
        return self.orders[-i]


class order_circular_array(object):
    def __init__(self, n):
        self.n = n
        self.orders = []
        self.cur = 0

    def record(self, order_id):
        if len(self.orders) == self.n:
            self.orders[self.cur] = order_id
        else:
            self.orders.append(order_id)
        self.cur = (self.cur + 1) % self.n

    def get_last(self, i):
        return self.orders[self.cur - i]
