from abc import ABC, abstractmethod

from infra.sokupad_client import SokupadClient


class AbstractRpa(ABC):

    def __init__(self, data):
        self._client = SokupadClient()
        self._data = data

    def run(self):
        self.start()
        self.process()
        self.end()

    def start(self) -> None:
        data = self._data
        self._client.login(data['id'], data['password'], data['p_ars'])

    def end(self) -> None:
        self._client.quit()

    @abstractmethod
    def process(self) -> None:
        pass
