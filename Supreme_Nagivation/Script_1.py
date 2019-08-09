# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:24:24 2019

@author: C092320
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import easygui


options = Options()
#options.add_argument('start-minimized')
options.add_argument('disable-infobars')
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Automation_Enterprise\Selenium\Resources\Chrome\chromedriver.exe')
driver.get('https://www.google.com/')
print('\n')
print(datetime.datetime.now(),'Opening Google')



try:
    assert 'Google' in driver.title
    print (datetime.datetime.now(),'Assertion Pass')

except Exception as e:
    print (datetime.datetime.now(),'Assertion Fail', format(e))





elem = driver.find_element_by_name('q')  # Find the search box
elem.send_keys('Supreme New York' + Keys.RETURN)
print(datetime.datetime.now(),'Searching for Supreme')

driver.find_element_by_xpath("//*[@href = 'https://www.supremenewyork.com/' ]/parent::div[@class = 'r']/a").click()
print(datetime.datetime.now(),'Opening Supreme Website')

driver.find_element_by_xpath("//span[text()='shop']/parent::a/parent::li/parent::ul/parent::nav/parent::div[@id = 'wrap']/nav/ul/li/following-sibling::li/following-sibling::li/following-sibling::li/a[@class ='shop_link']").click()
print(datetime.datetime.now(),'Opening Supreme Shop')


#*****************
#   Methods that could be used to wait
#
#               time.sleep(1)    #import time
#    driver.implicitly_wait(1) # seconds


WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@href = 'http://www.supremenewyork.com/shop/all']/parent::li/a[text()= 'view all']"))).click()
print(datetime.datetime.now(),'Opening View All')


user_lookup = input('Item Searching For: ')
print(datetime.datetime.now(),'User Wants %s' % (user_lookup))



print('\n1.  ALL')
print('2.  NEW')
print('3.  JACKETS')
print('4.  SHIRTS')
print('5.  TOPS/SWEATERS')
print('6.  SWEATSHIRTS')
print('7.  PANTS')
print('8.  SHORTS')
print('9.  HATS')
print('10. BAGS')
print('11. ACCESSORIES')



s_catagorie = input('Item Is In: ')






#browser.quit()
