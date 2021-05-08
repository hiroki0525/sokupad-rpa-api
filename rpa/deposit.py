from rpa import AbstractRpa


class Deposit(AbstractRpa):

    def process(self) -> None:
        params = self._get_params()
        print(params)