from abc import ABCMeta, abstractmethod


class CommandHandler(object):
    # TODO: Загуглить для чего нужен метакласс
    __metaclass__ = ABCMeta

    @abstractmethod
    def command_handler(self) -> str:
        pass
