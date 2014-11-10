__author__ = 'Sergey'

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class TestSummaryVSSearch(unittest.TestCase):

    driver = None

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()


    def test_search(self):
        """


        """

        self.driver.get("http://www.vivastreet.com/")

        self.driver.find_element_by_css_selector(r"[title=Nord-Pas-de-Calais]").click()

        #action_chains_action = ActionChains(self.driver)
        #action_chains_action.move_to_element(element_on_the_map).click().perform()


        #vs_detail_link = WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id("vs-detail-link-2"))
        #self.assertIn('a', vs_detail_link.text)

        ##self.driver.implicitly_wait(10)
        #self.driver.get("http://ordinateur-occasion.vivastreet.com/informatique-pda")
        self.driver.find_element_by_xpath(r'//input[@id="vs_search_keywords"]').send_keys("Test")
        category_dropdown = Select(self.driver.find_element_by_id("vs-cat-dropdown-1"))
        category_dropdown.select_by_value('74')
        self.driver.find_element_by_css_selector(r'.kiwii-btn.kiwii-btn-primary.kiwii-btn-large.'
                                                 r'ui-button.ui-search-button1.ui-corner-all.'
                                                 r'kiwii-span-2').send_keys(Keys.ENTER)

        vs_detail_link = WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id("vs-detail-link-2"))
        #vs_detail_link = self.driver.find_element_by_id("vs-detail-link-2")
        self.assertIn('moto,', vs_detail_link.text)
if __name__ == "__main__":
     unittest.main()