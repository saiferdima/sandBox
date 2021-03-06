class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, data):
        if data <= 0:
            raise NonPositiveError()
        else:
            super().append(data)
