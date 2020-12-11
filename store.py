from handlers.abstract import CommandHandler


class Store:
    def __init__(self):
        self._state: dict[str, CommandHandler] = {}
        self._count = 1

    def create(self, command: str, handle_class: CommandHandler):
        self._state[command] = handle_class

    def fetch(self, command: str) -> CommandHandler:
        return self._state[command]


GLOBAL_STORE = Store()
