import time
from selenium import webdriver

from const.page import page_setting


def deposit(data):
    driver = webdriver.Chrome()
    # テスト用
    pages = page_setting.get('chiho')
    login_page = pages['login']
    login_elements = login_page['elements']
    driver.get(login_page.url)
    time.sleep(5)

    id_input = driver.find_elements_by_css_selector(login_elements['id']['selector'])
    password_input = driver.find_elements_by_css_selector(login_elements['password']['selector'])
    p_ars_input = driver.find_elements_by_css_selector(login_elements['p_ars']['selector'])
    id_input.send_keys('12345678')
    password_input.send_keys('1234')
    p_ars_input.send_keys('5678')
    driver.find_elements_by_css_selector(login_elements['login']['selector']).click()

    time.sleep(5)
    driver.quit()
