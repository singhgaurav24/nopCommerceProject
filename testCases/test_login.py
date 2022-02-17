import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from utlities.readProperties import ReadConfig
from utlities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*********************Test_001_Login*******************")
        self.logger.info("*********************Verifying Home Page Title*******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        acutal_title = self.driver.title
        if acutal_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********************Home page title test passed*******************")
        else:
            self.driver.save_screenshot(".\\Screenshorts\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********************Home page title test failed*******************")
            assert False

    def test_login(self, setup):
        self.logger.info("*********************Verifying login test*******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*********************Home page title passed*******************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshorts\\" + "test_login.png")
            self.driver.close()
            self.logger.error("*********************Home page title failed*******************")
            assert False
