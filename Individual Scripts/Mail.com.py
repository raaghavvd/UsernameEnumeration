# User Enum Mail.com
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

# Using edge browser
driver = webdriver.Edge(executable_path='msedgedriver')

# Using Firefox browser
#driver = webdriver.FirefoxProfile()
#driver = webdriver.Firefox(driver)

print("The usernames present in Mail.com are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["BegForMercy", "BraiasjdnkjnAxe", "CrazyMind", "DeathWaasdaish", "DisasterMaster", "ElNaaaino", "EndlessFacepalms" ]:
    user = i

    driver.get("https://signup.mail.com/#.1272-header-signup2-1")
    sleep(3)
    p1=driver.page_source
    elem=driver.find_element_by_xpath('//input[@type="text"]') #type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)
    if "This choice of email address has already been assigned" in p3:
       print(i)
driver.close()