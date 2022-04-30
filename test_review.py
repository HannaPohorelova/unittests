import tracemalloc
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


tracemalloc.start()

class TestRocks(unittest.TestCase):

    def setUp(self) -> None:        # открывает браузер
        #service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome() #"(service=service)"
        self.driver.set_window_size(1024, 768)


    def test_stones(self):
        self.driver.get("https://techstepacademy.com/trial-of-the-stones")
        input_1 = self.driver.find_element(By.ID, "r1Input")
        input_2 = self.driver.find_element(By.ID, "r2Input")

        btn_answer_1 = self.driver.find_element(By.ID, "r1Btn")
        btn_answer_2 = self.driver.find_element(By.ID, "r2Butn")

        answer_1 = self.driver.find_element(By.CSS_SELECTOR, "#passwordBanner h4")
        answer_2 = self.driver.find_element(By.CSS_SELECTOR, "#successBanner1 h4")


        self.driver.execute_script("arguments[0].scrollIntoView();", input_1)
        input_1.send_keys('rock')
        btn_answer_1.click()
        text_answer_1 = answer_1.text

        input_2.send_keys(text_answer_1)
        btn_answer_2.click()
        text_answer_2 = answer_2.text

        expected_answer = 'Success!'
        self.assertEqual(text_answer_2, expected_answer)

        merchant_1 = self.driver.find_element(By.XPATH, '(//div/span/b)[1]').text
        merchant_2 = self.driver.find_element(By.XPATH, '(//div/span/b)[2]').text
        merchant_wealth_1 = self.driver.find_element(By.XPATH, '(//div/span/b)[1]/../../p')
        merchant_wealth_2 = self.driver.find_element(By.XPATH, '(//div/span/b)[2]/../../p')

        merch_1 = int(merchant_wealth_1.text)
        merch_2 = int(merchant_wealth_2.text)
        richest = ""
        if (merch_1>merch_2):
            richest = merchant_1
        else:
            richest = merchant_2
        input_3 = self.driver.find_element(By.ID, "r3Input")
        input_3.send_keys(richest)

        btn_answer_3 = self.driver.find_element(By.ID, "r3Butn")
        btn_answer_3.click()

        answer_3 = self.driver.find_element(By.CSS_SELECTOR, "#successBanner2 h4")
        text_answer_3 = answer_3.text

        self.assertEqual(text_answer_3, expected_answer)
        time.sleep(5)

        btn_check_answers = self.driver.find_element(By.ID, "checkButn")
        btn_check_answers.click()

        text_check_answers = self.driver.find_element(By.CSS_SELECTOR, "#trialCompleteBanner h4").text
        expected_answer = "Trial Complete"
        self.assertTrue(text_check_answers == expected_answer)
        time.sleep(5)

    def tearDown(self) -> None:   #закрывает браузер
        self.driver.close()

if __name__ == '__main__':
    unittest.main()