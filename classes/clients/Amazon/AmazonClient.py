

import pandas as pd
import re
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .WebDriver import WebDriver

def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
        driver.get("chrome://downloads/");
    return driver.execute_script("""
        var items = document.querySelector('downloads-manager')
            .shadowRoot.getElementById('downloadsList').items;
        if (items.every(e => e.state === "COMPLETE"))
            return items.map(e => e.fileUrl || e.file_url);
        """)



wait_for_element = 2  # wait timeout in seconds
class AmazonWebsite:
    def __init__(self, driver):
        self.driver = driver
    def go_to(self, url):
        driver = self.driver;
        driver.get(url)
    def get_store_text(self):
        driver = self.driver;
        return driver.find_element_by_css_selector('#bylineInfo').get_attribute('innerText')
    def get_image_src(self):
        driver = self.driver;
        return driver.find_element_by_css_selector('.image-size-wrapper.fp-image-wrapper.image-block-display-flex img').get_attribute('innerText')
    def get_details(self):
        driver = self.driver;

        elem = WebDriverWait(driver, wait_for_element).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".a-expander-prompt")
            )
        )
        if (elem): 
            driver.execute_script(" document.querySelector('.a-expander-prompt').click();")
        rows = driver.find_elements_by_css_selector('#productOverview_feature_div .a-row:not(#poExpander)');
        details = {}
        for row in rows:
            splitArr = row.get_attribute('innerText').split('\n');
            if (len(splitArr) == 2):
                [k, v] = splitArr
                details[k] = v;
        
        return details;
    def get_product_id(self):
        driver = self.driver;
        currentURL = driver.current_url;
        match = re.search('\/[A-Z0-9]{10}', currentURL)
        return match[0][1:]
    def get_node_data(self):
        storeText = self.get_store_text()
        imageSrc = self.get_image_src()
        details = self.get_details()
        productId = self.get_product_id()
        return {
            "storeText": storeText,
            "imageSrc": imageSrc,
            "details": details,
            "productId": productId,
        }

    def close(self):
        self.driver.close()
        
class AmazonClient:
    def __init__(self):
        driverBase = WebDriver()
        driver = driverBase.driver_instance
        self.website = AmazonWebsite(driver)
        
    def GetNodeData(self, url):
        self.website.go_to(url)
        return self.website.get_node_data()
        
    def Close(self):
        self.website.close()