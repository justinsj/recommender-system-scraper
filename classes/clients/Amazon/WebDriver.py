import sys
import os

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
print('all modules are loaded ')


class DriverOptions(object):

    def __init__(self):

        self.options = Options()
        self.options.add_argument('--no-sandbox')
        #self.options.add_argument('--start-maximized')
        #self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')
        #self.options.add_argument("--incognito")
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("detach", True)

        self.options.add_argument("disable-infobars")

        #self.helperSpoofer = Spoofer()

        #self.options.add_argument('user-agent={}'.format(self.helperSpoofer.userAgent))
        #self.options.add_argument('--proxy-server=%s' % self.helperSpoofer.ip)


class WebDriver(DriverOptions):

    def __init__(self, path=''):
        DriverOptions.__init__(self)
        self.driver_instance = self.get_driver()

    def get_driver(self):

        # print("""
        # IP:{}
        # UserAgent: {}
        # """.format(self.helperSpoofer.ip, self.helperSpoofer.userAgent))

        # PROXY = self.helperSpoofer.ip
        # webdriver.DesiredCapabilities.CHROME['proxy'] = {
        #     "httpProxy":PROXY,
        #     "ftpProxy":PROXY,
        #     "sslProxy":PROXY,
        #     "noProxy":None,
        #     "proxyType":"MANUAL",
        #     "autodetect":False
        # }
        webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True

        path = os.path.join(os.getcwd(), 'chrome','chromedriver.exe')


        # data_dir = os.path.join(os.getcwd(), 'chrome','User Data');
        user_agent = 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'

        username = os.getenv("USERNAME")
        #userProfile = "C:\\Users\\" + username + "\\AppData\\Local\\Google\\Chrome\\User Data"
        self.options.add_argument(f'user-agent={user_agent}')
        # self.options.add_argument("--user-data-dir="+data_dir);
        # self.options.add_argument("--profile-directory=Profile 5");
        self.options.add_argument("--disable-extensions");
        self.options.add_argument("window-size=412,915")


        self.options.add_argument("--enable-javascript")
        driver = webdriver.Chrome(executable_path=path, options=self.options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source":
                "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
        })

        return driver


