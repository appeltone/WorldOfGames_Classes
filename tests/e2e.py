from selenium import webdriver
import os

path = os.path.dirname(__file__)
url = "http://127.0.0.1:8777/"


def test_scores_service(url):
    driver = webdriver.Chrome("../chromedriver.exe")
    driver.get(url)

    element = driver.find_element_by_id("score")

    if (1 <= int(element.text) <= 1000):
        return True
    else:
        return False


def main_function():
    if test_scores_service(url):
        return 0
    else:
        return -1


print(main_function())
