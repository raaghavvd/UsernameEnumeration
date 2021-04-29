#  User Enum Microsoft
# Filter on "Create a password". Other condition not working

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

driver = webdriver.Edge(executable_path='msedgedriver')

print("The usernames present in Microsoft are:")

for i in ["ccohen@aol.com", "keijser@aol.com", "ajohnson@hotmail.com", "rnewman@aol.com", "sfoskett@hotmail.com", "seurat@aol.com", "richard@gmail.com", "punkis@gmail.com", "jadavis@outlook.com", "staffelb@att.net", "pplinux@icloud.com", "lamky@optonline.net", "ccoerhen@aol.com", "keijserqer@aol.com", "ajohneesdson@hotmail.com", "rnewman@aol.com", "sfosksdett@hotmail.com", "seusdrat@aol.com", "richard@gmail.com", "pssunkis@gmail.com", "jadavssis@outlook.com", "stafssfelb@att.net", "pplinsdux@icloud.com", "laamky@optonline.net"]:


    user = i

    driver.get("https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&rver=7.3.6963.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.microsoft.com%2fen-us%2f&id=74335&aadredir=1&contextid=ACB533D65C56CD95&bk=1615526360&uiflavor=web&lic=1&mkt=EN-US&lc=1033&uaid=08c675e0e23847268b39b98014e3323d")
    p1 = driver.page_source
    #elem=driver.find_element_by_name("Mobile Number or Email")
    elem=driver.find_element_by_xpath("//input[@type='email']") #type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2,p1)


    if "Create a password" not in p3:
        print(i)

    sleep(3)
