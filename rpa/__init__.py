import time

from selenium.webdriver.chrome.webdriver import WebDriver


class SokupadRPA():

    def __init__(self, init_url="", sleep=5):
        self.__driver = WebDriver()
        self.__url = init_url
        self.__sleep = sleep

    def wait(self, sleep=None):
        time.sleep(sleep if sleep is not None else self.__sleep)

    def get(self, url=""):
