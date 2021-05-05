from abc import ABC, abstractmethod

from infra.sokupad_client import SokupadClient


class AbstractRpa(ABC):

    def __init__(self):
        self.__client = SokupadClient()

    def run(self):
        self.start()
        self.process()
        self.end()

    def start(self, **kwargs) -> None:
        self.__client.login(kwargs['id'], kwargs['password'], kwargs['p_ars'])

    def end(self) -> None:
        self.__client.quit()

    @abstractmethod
    def process(self) -> None:
        pass
