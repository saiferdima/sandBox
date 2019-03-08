class MoneyBox:
    def __init__(self, capacity=0):
        # конструктор с аргументом – вместимость копилки
        self.cap = capacity
        self.current = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if v + self.current > self.cap:
            return False
        else:
            return True

    def add(self, v):
        # положить v монет в копилку
        self.current = self.current + v
