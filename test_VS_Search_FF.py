__author__ = 'Sergey'

import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestSummaryVSSearch(unittest.TestCase):
    driver = None


    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
        #self.driver.implicitly_wait(10)
        #self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()


    def test_search_1(self):
        """
             This test looks on the second element of the ad
             and verify whether the searched keyword is present
             in the title.
        """

        self.driver.get("http://www.vivastreet.com/")

        self.driver.find_element_by_css_selector(r"[title=Nord-Pas-de-Calais]").click()

        #action_chains_action = ActionChains(self.driver)
        #action_chains_action.move_to_element(element_on_the_map).click().perform()


        def ajax_complete(driver):
            try:
                return 0 == driver.execute_script("return jQuery.active")
            except WebDriverException:
                pass


        #vs_detail_link = WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id("vs-detail-link-2"))
        #self.assertIn('a', vs_detail_link.text)

        ##self.driver.implicitly_wait(10)
        #Here is the text that is commented out
        self.driver.find_element_by_xpath(r'//input[@id="vs_search_keywords"]').send_keys("Ceci test")
        category_dropdown = Select(self.driver.find_element_by_id("vs-cat-dropdown-1"))
        category_dropdown.select_by_value('74')
        self.driver.find_element_by_css_selector(r'.kiwii-btn.kiwii-btn-primary.kiwii-btn-large.'
                                                 r'ui-button.ui-search-button1.ui-corner-all.'
                                                 r'kiwii-span-2').send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 10).until(ajax_complete, "Timeout waiting for page to load")
        vs_detail_link = self.driver.find_element_by_id("vs-detail-link-1")
        self.assertIn('TEST', vs_detail_link.text)


if __name__ == "__main__":
    unittest.main()