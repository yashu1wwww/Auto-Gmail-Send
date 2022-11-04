import undetected_chromedriver as uc
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import random

subject = ["hey google how are you","hey google good morning","i think you are fine",] #add more if you want more text and replace the text in which you required

email = 'send123@gmail.com\n'  #replace with your gmail(use non 2 factor authentication mail) 
password = 'pass123\n'    #replace with your password

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
url = 'https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fmail.google.com&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'password'))).send_keys(password)
time.sleep(20)

driver.find_element_by_css_selector('.T-I.T-I-KE.L3').click()
time.sleep(16)
to = driver.find_element_by_name('to')
ActionChains(driver)\
.send_keys("toyou123@gmail.com")\
.perform()
#replace with your sender mail id

time.sleep(5)
driver.find_element_by_xpath('//input[@type="file"]').send_keys(r"C:\Users\Hp\Desktop\Bots\gmail\data.txt") #here the file or document will send (replace path with your where your file located if you don't want to use means add # in these line in starting of these code)
time.sleep(7)
driver.find_element_by_name("subjectbox").send_keys(random.choice(subject))
time.sleep(5)
driver.find_element_by_css_selector('.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3').click()
time.sleep(50)   
driver.close()
