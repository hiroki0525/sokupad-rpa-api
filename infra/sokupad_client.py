from random import randrange

import time

from selenium import webdriver
# パスを通すためにimport
import chromedriver_binary

from const.page import page_config

def commit(func):
    def wrapper(*args, **kwargs):
        print(args)
        client = args[0]
        if not client.commit:
            return
        func(*args, **kwargs)
    return wrapper

class SokupadClient:

    def __init__(self, headless: bool = False, commit: bool = False):
        options = None
        if headless:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
        self.__driver = webdriver.Chrome(options=options)
        self.__commit = commit
        self.__pages = page_config.get('chiho')

    @property
    def commit(self):
        return self.__commit

    def get(self, url: str) -> None:
        return self._dispatch(self.__driver.get, url)

    def quit(self) -> None:
        return self.__driver.quit()

    def move_money_account_page(self):
        driver = self.__driver
        selector = self.__pages['top']['elements']['money']['selector']
        button = driver.find_elements_by_css_selector(selector)[0]
        self._dispatch(button.click)
        # 別タブで開かれるので切り替える
        handles = driver.window_handles
        driver.switch_to.window(handles[len(handles) - 1])

    def move_deposite_page(self):
        selector = self.__pages['money']['elements']['deposit']['selector']
        button = self.__driver.find_elements_by_css_selector(selector)[0]
        self._dispatch(button.click)

    def input_deposit_and_go(self, price):
        driver = self.__driver
        deposit_elements = self.__pages['deposit']['elements']
        deposit_input = driver.find_elements_by_css_selector(deposit_elements['price']['selector'])[0]
        confirm_button = driver.find_elements_by_css_selector(deposit_elements['confirm']['selector'])[0]
        self._dispatch(deposit_input.send_keys, price)
        self._dispatch(confirm_button.click)

    @commit
    def execute_deposit_and_go(self, password):
        driver = self.__driver
        elements = self.__pages['execute_deposit']['elements']
        password_input = driver.find_elements_by_css_selector(elements['password']['selector'])[0]
        execute_button = driver.find_elements_by_css_selector(elements['excute']['selector'])[0]
        self._dispatch(password_input.send_keys, password)
        self._dispatch(execute_button.click)

    def login(self, id: str, password: str, p_ars: str) -> None:
        driver = self.__driver
        pages = self.__pages

        # ログイン
        login_page = pages['login']
        login_elements = login_page['elements']
        driver.get(login_page['url'])
        id_input = driver.find_elements_by_css_selector(login_elements['id']['selector'])[0]
        password_input = driver.find_elements_by_css_selector(login_elements['password']['selector'])[0]
        p_ars_input = driver.find_elements_by_css_selector(login_elements['p_ars']['selector'])[0]
        self._dispatch(id_input.send_keys, id)
        self._dispatch(password_input.send_keys, password)
        self._dispatch(p_ars_input.send_keys, p_ars)
        self._dispatch(driver.find_elements_by_css_selector(login_elements['login']['selector'])[0].click)

        # お知らせ（あれば）
        try:
            notice_ok = driver.find_elements_by_css_selector(pages['notice']['elements']['ok'])[0]
            self._dispatch(notice_ok.click)
        except Exception as e:
            print('No notice page.')

    def _dispatch(self, func, *args, **kwargs):
        result = func(*args, **kwargs)
        time.sleep(randrange(2, 5))
        return result