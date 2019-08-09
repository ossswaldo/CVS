from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import time 


class multipleInstances():
    
    def __init__(self):
        self.driver = None
        
    def setupselenium(self):
        options = Options()
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        #options.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Automation_Enterprise\Selenium\Resources\Chrome\chromedriver.exe')
     
    def execute(self):
        self.setupselenium()
        self.loginToGMail()
        self.cleanUpBrowser()
        
    def loginToGMail(self):
         self.driver.get('https://www.gmail.com/')
         print(datetime.datetime.now(),'\nOpening Google')
         time.sleep(1)
         self.driver.find_elements_by_id('Email').send_keys('arguetaoswaldo0976@gmail.com')
         self.driver.find_elements_by_id('Email').submit()
         time.sleep(1)
         self.driver.find_elements_by_id('Passwd').send_keys('123')
         self.driver.find_elements_by_id('Passwd').submit()

        
        
    def cleanUpBrowser(self):
        self.driver.quit()
        
        
if __name__== "__main__":
    taskMaster =  multipleInstances()
    taskMaster.execute()
    
    
   
    
    
 #  try:
 #       assert 'Google' in driver.title
 #       print (datetime.datetime.now(),'Assertion Pass')
 #   
  #  except Exception as e:
 #       print (datetime.datetime.now(),'Assertion Fail', format(e))
 #       
 #       
 #   counter = 0
 #   while counter<10000000000000000:
 #   
 #       elem = driver.find_element_by_name('q')  # Find the search box
 #       elem.send_keys('CVS')
 #       print(datetime.datetime.now(),'Searching for CVS', counter)
 #       
 #       driver.refresh()
 #       print(datetime.datetime.now(),'Refeshing Google')
 #       time.sleep(2)

