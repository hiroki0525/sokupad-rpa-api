from rpa import AbstractRpa


class Deposit(AbstractRpa):

    def process(self) -> None:
        data = self._data