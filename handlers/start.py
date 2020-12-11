from handlers.abstract import CommandHandler
from store import GLOBAL_STORE


class StartHandler(CommandHandler):
    def __init__(self):
        GLOBAL_STORE.create('start', self)

    def command_handler(self):
        return 'Привет Айдар'
