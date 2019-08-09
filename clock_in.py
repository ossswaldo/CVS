# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

#from easygui import*


from datetime import datetime
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
        self.loginToCVS()
        self.cleanUpBrowser()

    def loginToCVS(self):
        
        print('\n')
        print(datetime.now(),'WorkBrain Script Initiated -')
        self.driver.get('https://mylife.cvshealth.com/webcenter/portal/mylife')
        print(datetime.now(),'Opening CVS My Life')

        self.workBrain()
        #self.timeCompare()
        time.sleep(5)

    def workBrain(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            try:
                dropDownMenu =  wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id = 'l1gTl4']")))
                ActionChains(self.driver).move_to_element(dropDownMenu).perform()
                print(datetime.now(),'Clicking Tools & Services')

                print(datetime.now(),'Searching For WorkBrain Drop Down')
                elementToSelect = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class = 'tools-flyout']/div/div/div/div/div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/a")))
                ActionChains(self.driver).move_to_element(elementToSelect).click().perform()
                print(datetime.now(),'Opening WorkBrain')
            except:
                print(datetime.now(),'Unable to Search For WorkBrain Drop Down, Looking Again')
                elementToSelect2 = self.driver.find_element_by_xpath("////*[text() = 'Workbrain - Employee Transaction Manager']/parent::div/parent::div/parent::div/parent::div/parent::div[@class = 'tools-flyout-content x1a']/div/div/div/div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/a")
                ActionChains(self.driver).move_to_element(elementToSelect2).click().perform()
                
                #elementToSelect2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text() = 'Workbrain - Employee Transaction Manager']/parent::div/parent::div/parent::div/parent::div/parent::div[@class = 'tools-flyout-content x1a']/div/div/div/div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/following-sibling::div/a")))
                #ActionChains(self.driver).move_to_element(elementToSelect2).click().perform()
                print(datetime.now(),'Opening WorkBrain')
        except:
                print(datetime.now(),'WorkBrain Not Found In Clicking Tools & Services ')
                inputElement = self.driver.find_element_by_xpath("//input[@id = 'globalSearchBox']")
                inputElement.send_keys('workbrain')
                print(datetime.now(),'Typing in Search bar')
                
                WorkBrain_dropDown =  wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text() = 'Workbrain - Employee Transaction Manager']")))
                ActionChains(self.driver).move_to_element(WorkBrain_dropDown).click().perform()
                print(datetime.now(),'Clicking Tools & Services')
        finally:
                print(datetime.now(),'WorkBrain Clicked - loading')





        
    def clockIN(self):
        wait = WebDriverWait(self.driver, 10)
        on = wait.until(EC.visibility_of_element_located((By.ID, "clock_on")))
        ActionChains(self.driver).move_to_element(on).click().perform()

        yes_b = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text() = 'Yes']")))# clicks the yes
        no_b = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text() = 'No']")))# clicks the no
        exit_b = wait.until(EC.visibility_of_element_located((By.XPATH, " //*[@class = 'ui-button-icon-primary ui-icon ui-icon-closethick']")))# Clicks the exit
        ActionChains(self.driver).move_to_element(yes_b).click().perform()
        print(datetime.now(),'Clocking In Successful')

    def clockOUT(self):
        wait = WebDriverWait(self.driver, 10)
        on = wait.until(EC.visibility_of_element_located((By.ID, "clock_off")))
        ActionChains(self.driver).move_to_element(on).click().perform()

        yes_b = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text() = 'Yes']")))# clicks the yes
        no_b = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text() = 'No']")))# clicks the no
        exit_b = wait.until(EC.visibility_of_element_located((By.XPATH, " //*[@class = 'ui-button-icon-primary ui-icon ui-icon-closethick']"))) # Clicks the exit
        ActionChains(self.driver).move_to_element(yes_b).click().perform()
        print(datetime.now(),'Clocking Out Successful')


    def timeCompare(self):
        wait = WebDriverWait(self.driver, 10)
        FMT = ('%H:%M:%S.%f')
        cTime = datetime.time(datetime.now())
        scTime = str(cTime)
        ten = '10:00:00.00000'
        four = '16:00:00.00000'
        fourThirty = '16:30:00.00000'

        self.driver.switch_to.window(self.driver.window_handles[1]) #swithces tab
        if (datetime.strptime(scTime, FMT) < datetime.strptime(ten, FMT) ):
            print(datetime.now(),'Clockig in')
            self.clockIN()
        elif(datetime.strptime(scTime, FMT) < datetime.strptime(four, FMT) ):
            print(datetime.now(),'Potential lunch time')
            time.sleep(2)
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class= 'on']")))
                print(datetime.now(), "Element ON Exists  - YOU WILL BE CLOCKED OUT")
                self.clockOUT()
            except:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class= 'off']")))
                print(datetime.now(), "Element OFF exists - YOU WILL BE CLOCKED IN")
                self.clockIN()
            finally:
                print(datetime.now(), "Mid Day Scenerio Complete - ACTION SUCCESSFUL")
            
           
        elif(datetime.strptime(scTime, FMT) > datetime.strptime(fourThirty, FMT) ):
            print(datetime.now(),'Time to leave')
            self.clockOUT()

    def cleanUpBrowser(self):
        print(datetime.now(),'Quitting Browser')
        self.driver.quit()


if __name__== "__main__":
    taskMaster =  multipleInstances()
    taskMaster.execute()
