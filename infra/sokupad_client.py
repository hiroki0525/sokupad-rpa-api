from random import randrange

import time

from selenium import webdriver
# パスを通すためにimport
import chromedriver_binary

from const.page import page_setting


class SokupadClient:

    def __init__(self):
        self.__driver = webdriver.Chrome()

    @staticmethod
    def wait() -> None:
        time.sleep(randrange(5, 10))

    def get(self, url: str) -> None:
        return self.__driver.get(url)

    def quit(self) -> None:
        return self.__driver.quit()

    def login(self, id: str, password: str, p_ars: str) -> None:
        driver = self.__driver
        pages = page_setting.get('chiho')
        login_page = pages['login']
        login_elements = login_page['elements']
        driver.get(login_page.url)
        time.sleep(5)
        id_input = driver.find_elements_by_css_selector(login_elements['id']['selector'])
        password_input = driver.find_elements_by_css_selector(login_elements['password']['selector'])
        p_ars_input = driver.find_elements_by_css_selector(login_elements['p_ars']['selector'])
        id_input.send_keys(id)
        password_input.send_keys(password)
        p_ars_input.send_keys(p_ars)
        driver.find_elements_by_css_selector(login_elements['login']['selector']).click()
