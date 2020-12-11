from handlers.abstract import CommandHandler
from store import GLOBAL_STORE


class TestHandler(CommandHandler):
    def __init__(self):
        GLOBAL_STORE.create('test', self)

    def command_handler(self):
        return 'Привет test'
