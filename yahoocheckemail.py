# MIT License
#
# Copyright (c) 2017 Denzil Sequeira
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait


class YahooScraper(object):
    def __init__(self):
        display = Display(visible=0, size=(1120, 600))
        display.start()
        self.driver = webdriver.Chrome()
        self.url = 'https://edit.yahoo.com/forgot?stage=fe100'

    def scrape(self, email):
        self.driver.get(self.url)
        self.driver.find_element_by_id('username').send_keys(email)
        self.driver.find_element_by_name('verifyYid').click()

        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState;") == "complete")
        bs = BeautifulSoup(self.driver.page_source, "lxml")
        if bs.findAll("div", class_="error-msg"):
            print ("Invalid Email")
        else:
            print ("Valid Email")


if __name__ == '__main__':
    wbkname = input("E-mail to be checked?? ")
    scraper = YahooScraper()

    scraper.scrape(str(wbkname))
