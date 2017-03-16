import selenium.webdriver
import time

#signin_button = '.HomePageActionButton'

class WebdriverHandler(object):
    def __init__(self, url):
        self._webdriver = selenium.webdriver.Firefox(firefox_binary= r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
        self._url = url

    def openURL(self):
        self._webdriver.get(self._url)


    def click(self, selector):
        element = self._webdriver.find_element_by_css_selector(selector)
        element.click()

    def enterText(self, selector, text):
        element = self._webdriver.find_element_by_css_selector(selector)
        element.send_keys(text)

    def readSource(self):
        source = self._webdriver.page_source
        print source

class Tenbis(object):
    def __init__(self, url):
        self.wd = WebdriverHandler(url)
        self.wd.openURL()

    def login(self, username, password):
        self.wd.click(".HomePageActionButton")
        self.wd.enterText("[tabindex='1']", username)
        self.wd.enterText("[tabindex='2']", password + '\n')

    def expensesReport(self):
        time.sleep(8)
        self.wd.click(".glyphicon-cog")
        self.wd.click("[href='/Account/UserReport']")
        self.wd.readSource()



def main():
    tenbis = Tenbis("https://10bis.co.il")
    tenbis.login(username, password)



if __name__ == '__main__':
    main()
