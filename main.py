from handlers.lol import LolHandler
from handlers.start import StartHandler
from handlers.test import TestHandler
from loader import Loader
from store import GLOBAL_STORE


loader = Loader([StartHandler, LolHandler, TestHandler, 2])


# print(GLOBAL_STORE.fetch('start').command_handler())
# print(GLOBAL_STORE.fetch('lol').command_handler())
# print(GLOBAL_STORE.fetch('test').command_handler())

print(loader.get(StartHandler).command_handler())
