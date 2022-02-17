import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Chrome(executable_path="F:\selemium\chromedriver.exe")
    return driver

