from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os
from stem import Signal
from stem.control import Controller
import subprocess
from time import sleep


def get_current_ip():
    # myProxy = "127.0.0.1:9150"
    # ip, port = myProxy.split(":")
    # driver = webdriver.FirefoxProfile()
    # driver.set_preference('network.proxy.type', 1)
    # driver.set_preference('network.proxy.socks', ip)
    # driver.set_preference('network.proxy.socks_port', int(port))
    # options = Options()
    # options.headless = True
    # #driver = webdriver.Firefox(options=options)
    # driver = webdriver.Firefox(driver)
    driver.get("http://httpbin.org/ip")
    # # try:
    #     driver.get('http://httpbin.org/ip')
    #
    # except Exception as e:
    #     print(str(e))
    # else:
    #     print("Done")



def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="mypassword")  #this will be different!
        controller.signal(Signal.NEWNYM)


if __name__ == "__main__":
    sub = subprocess.Popen(r'C:\Users\User\Desktop\Tor Browser\Browser\firefox')
    profile = FirefoxProfile(r'C:\Users\User\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')

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


    for i in range(5):
        print(i)
        if i%2==0:
            renew_tor_ip()
        get_current_ip()
        sleep(3)
