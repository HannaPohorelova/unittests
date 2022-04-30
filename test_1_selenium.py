import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service
import tracemalloc

tracemalloc.start()

class TestMePlease(unittest.TestCase):

    def setUp(self) -> None:        # открывает браузер
        #service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome() #"(service=service)"
        self.driver.set_window_size(1024, 768)


    def test_1(self):
        self.driver.get("http://www.google.com/")

    def test_2(self):
        self.driver.get("http://www.wiki.com/")
        #time.sleep(5)

    def test_3(self):
        self.driver.maximize_window()
        self.driver.get("https://www.selenium.dev/about/")
        doc_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/documentation']").click()
        self.assertEqual(self.driver.title, "The Selenium Browser Automation Project | Selenium")
        self.assertEqual(self.driver.current_url, "https://www.selenium.dev/documentation/")



    def tearDown(self) -> None:   #закрывает браузер
        self.driver.close()

if __name__ == '__main__':
    unittest.main()