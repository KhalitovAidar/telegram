from handlers.abstract import CommandHandler
from store import GLOBAL_STORE


class LolHandler(CommandHandler):
    def __init__(self):
        GLOBAL_STORE.create('lol', self)

    def command_handler(self):
        return 'Привет lol'
