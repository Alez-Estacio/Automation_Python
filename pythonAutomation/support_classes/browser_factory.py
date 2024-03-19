from .system_enums import TargetBrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowserFactory:

    name: str = ""
    browser: TargetBrowser = TargetBrowser.Chrome
    driver = ""

    def __init__(self):
        self.name = "NoName"


    def SetBrowserByString(self, targetBrowser: str):
        if targetBrowser.upper() == "GC":
            self.browser = TargetBrowser.Chrome
            self.driver = webdriver.Chrome()
        elif targetBrowser.upper() == "FF":
            self.browser = TargetBrowser.FF
            self.driver = webdriver.Firefox()
        else:
            self.browser = TargetBrowser.Chrome
            self.driver = webdriver.Chrome()


    def SetBrowserByEnum(self, targetBrowser: TargetBrowser):
        if targetBrowser == TargetBrowser.Chrome:
            self.browser = TargetBrowser.Chrome
            self.driver = webdriver.Chrome()
        elif targetBrowser == TargetBrowser.FF:
            self.browser = TargetBrowser.FF
            self.driver = webdriver.Firefox()
        else:
            self.browser = TargetBrowser.Chrome
            self.driver = webdriver.Chrome()

    def RefreshBrowser(self):
        self.driver.refresh()


    def MaximizeBrowser(self):
        self.driver.maximize_window()


    def NavigateToThisPage(self, url: str):
        self.driver.get(url)


    def SearchElements(self, method: str, selector: str, waitSize: int, intervals: int, expected: bool):
        cycles: int = 0
        listElements = []
        dataFound: bool = False
        while cycles < intervals:
            if method.lower() == "css":
                listElements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            elif method.lower() == "xpath":
                listElements = self.driver.find_elements(By.XPATH, selector)
            elif method.lower() == "id":
                listElements = self.driver.find_elements(By.ID, selector)
            else:
                listElements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            if expected:
                if len(listElements) > 0:
                    dataFound = True
                    break
                else:
                    time.sleep(waitSize)
                    cycles = cycles + 1
            else:
                if len(listElements) > 0:
                    time.sleep(waitSize)
                    cycles = cycles + 1
                else:
                    dataFound = True
                    break
        if not dataFound:
            print("The selector didnt return the expected results: "+selector)
            print("Were elements expected: "+expected)
        return listElements