#  User Enum Chaturbate
# Need usernames instead of email IDs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

print("The usernames present in theguadian are:")

#for i in ["ccohen@aol.com", "superman@gmail.com", "batman@gmail.com", "keijser@aol.com", "superman@gmail.com", "ajohnson@hotmail.com", "rnewman@aol.com", "sfoskett@hotmail.com", "seurat@aol.com", "richard@gmail.com", "punkis@gmail.com", "jadavis@outlook.com", "staffelb@att.net", "pplinux@icloud.com", "lamky@optonline.net", "ccoerhen@aol.com", "keijserqer@aol.com", "ajohneesdson@hotmail.com", "rnewman@aol.com", "sfosksdett@hotmail.com", "seusdrat@aol.com", "richard@gmail.com", "pssunkis@gmail.com", "jadavssis@outlook.com", "stafssfelb@att.net", "pplinsdux@icloud.com", "laamky@optonline.net"]:
#for i in ["ccohen@aol.com", "superman@gmail.com", "batman@gmail.com"]:
for i in ["superman", "batman", "asdjhbasbdajd"]:

    user = i
    driver = webdriver.Edge(executable_path='msedgedriver')
    driver.get("https://chaturbate.com/accounts/register/?src=header&auipsrc=navbar")
    sleep(2)
    p1 = driver.page_source
    elem=driver.find_element_by_xpath("//input[@type='text']") #type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2,p1)
    if "Username is already taken" in p3:
        print(i)
    sleep(3)
    driver.close()