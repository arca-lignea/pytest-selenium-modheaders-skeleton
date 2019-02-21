import time
import unittest
import zipfile
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
 
class PyUnitSeleniumTestCase(unittest.TestCase):
    def setUp(self):
        user_data_dir = 'C:/Users/blah/AppData/Local/Google/Chrome/'
        extension_path = 'Extensions/idgpnmonknjnojddfkpgkljpfnnfcklj/2.2.5_0'
        #new firefox session
        self.options = Options()
        self.options.add_argument('--load-extension=' + user_data_dir + extension_path)
        self.driver = webdriver.Chrome(executable_path='C:/temp/chromedriver.exe', options=self.options)
        self.driver.get('chrome-extension://idgpnmonknjnojddfkpgkljpfnnfcklj/settings.tmpl.html')
        self.driver.execute_script('''localStorage.setItem('profiles', JSON.stringify([{
                                      title: 'Selenium', hideComment: true, appendMode: '',
                                      headers: [
                                       {enabled: true, name: 'a', value: 'foo', comment: ''},
                                       {enabled: true, name: 'b', value: 'bar', comment: ''}
                                      ],
                                      respHeaders: [],
                                      filters: []
                               }]));''')
        time.sleep(1)
                               
                               
    def tearDown(self):
        self.driver.quit()
                               
    def testFlow(self):
        self.driver.get("http://localhost:4200/")
        time.sleep(5)
                               
                               
if __name__ == '__main__':
    unittest.main()
 
