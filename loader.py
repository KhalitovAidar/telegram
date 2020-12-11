#Как анотировать не инитиализированный конструктов


class Loader:
    def __init__(self, some_classes: list):
        self._store: dict[str, object] = {}
        for i in some_classes:
            self._store[i.__name__] = i()

    def get(self, metadata):
        return self._store[metadata.__name__]
