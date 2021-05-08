from random import randrange

import time

from selenium import webdriver
# パスを通すためにimport
import chromedriver_binary

from const.page import page_config


def dispatch(func, *args, **kwargs):
    result = func(*args, **kwargs)
    time.sleep(randrange(2, 5))
    return result


class SokupadClient:

    def __init__(self, headless: bool = False, commit: bool = False):
        options = None
        if headless:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
        self.__driver = webdriver.Chrome(options=options)
        self.__commit = commit

    def get(self, url: str) -> None:
        return dispatch(self.__driver.get, url)

    def quit(self) -> None:
        return self.__driver.quit()

    def login(self, id: str, password: str, p_ars: str) -> None:
        driver = self.__driver
        pages = page_config.get('chiho')
        login_page = pages['login']
        login_elements = login_page['elements']
        driver.get(login_page['url'])
        id_input = driver.find_elements_by_css_selector(login_elements['id']['selector'])
        password_input = driver.find_elements_by_css_selector(login_elements['password']['selector'])
        p_ars_input = driver.find_elements_by_css_selector(login_elements['p_ars']['selector'])
        dispatch(id_input.send_keys, id)
        dispatch(password_input.send_keys, password)
        dispatch(p_ars_input.send_keys, p_ars)
        dispatch(driver.find_elements_by_css_selector(login_elements['login']['selector']).click)
