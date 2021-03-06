from abc import ABC, abstractmethod

from entity.state import RpaState
from infra.sokupad_client import SokupadClient


class AbstractRpa(ABC):

    def __init__(self, state: RpaState):
        self._client = SokupadClient()
        self._state = state

    def run(self):
        try:
            self.start()
            self.process()
        except Exception as e:
            print(e)
        finally:
            self.end()

    def start(self) -> None:
        user = self._get_params().user
        self._client.login(user.id, user.password, user.p_ars)

    def end(self) -> None:
        self._client.quit()

    @abstractmethod
    def process(self) -> None:
        pass

    def _get_params(self):
        return self._state.params