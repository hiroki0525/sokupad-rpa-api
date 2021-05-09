from rpa import AbstractRpa


class Deposit(AbstractRpa):

    def process(self) -> None:
        params = self._get_params()
        client = self._client
        
        # 入出金メニュー
        client.move_money_account_page()

        # 入金ページ
        client.move_deposite_page()

        # 入金額を入力
        client.input_deposit_and_go(params.amount)

        # 暗証番号入力
        client.execute_deposit_and_go(params.user.password)