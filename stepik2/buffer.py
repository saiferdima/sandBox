class Buffer:
    def __init__(self):
        self.arr = []
        self.current_position = 0
        self.sum = 0
        # конструктор без аргументов

    def add(self, *a):
        for elem in a:
            self.arr.append(elem)
            if len(self.arr) % 5 == 0:
                # print('SUM ' + str(elem))
                # print('len ' + str(len(self.arr)))
                for i in range(len(self.arr) - 5, len(self.arr)):
                    self.sum = self.sum + self.arr[i]
                print(self.sum)
                self.sum = 0


                # добавить следующую часть последовательности

    def get_current_part(self):
        a = len(self.arr) - len(self.arr) % 5

        return self.arr[a:]

    # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
    # добавлены


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part()  # вернуть [6]
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part()  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part()  # вернуть [1]
