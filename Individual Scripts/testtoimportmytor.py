from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import subprocess
import os
from selenium.webdriver.common.keys import Keys
from time import sleep,time
#from seleniumwire import webdriver
import requests
import time
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
import re

with open('error_msgs.txt') as f:
    msg_database= [line.rstrip() for line in f]

#Cleaning the msg_database and converting the text in lower case.
msg_database=[re.sub('[^A-Za-z0-9]+', '', mystring.lower()) for mystring in msg_database]
print(msg_database)


with open('msg2.txt') as f:
    account_not_exist_msg= [line.rstrip() for line in f]

account_not_exist_msg=[re.sub('[^A-Za-z0-9]+', '', mystring.lower()) for mystring in account_not_exist_msg]
print(account_not_exist_msg)

def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="mypassword")  #this will be different!
        controller.signal(Signal.NEWNYM)

def accountNotPresentLogin(user,link):

    myProxy = "127.0.0.1:9150"
    ip, port = myProxy.split(":")
    driver = webdriver.FirefoxProfile()
    driver.set_preference('network.proxy.type', 1)
    driver.set_preference('network.proxy.socks', ip)
    driver.set_preference('network.proxy.socks_port', int(port))
    options = Options()
    options.headless = True
    # browser = webdriver.Firefox(options=options)
    browser = webdriver.Firefox(driver)

    print(user);
    flag=False
    flag_pass=False


    browser.get(str(link))
    file1=browser.page_source
    sleep(2)                                # Very IMP
    passwordV='A3847HUSHebhbdke$$'

    try:
        elem = browser.find_element_by_name("username")
    except:
        print("username doesnt exist")
        try:
            elem=browser.find_element_by_name("usernameOrEmail")
        except:
            print("usernameOrEmail doesnt exist")
            try:
                elem=browser.find_element_by_name("email")
            except:
                print("email doesnt exist")
                try:
                    elem=browser.find_element_by_name("ap_email")
                except:
                    print("email doesnt exist")
                    try:
                        elem=browser.find_element_by_name("userid")
                    except:
                        print("email doesnt exist")
                        try:
                            elem=browser.find_element_by_xpath("//*[@id='forgot-password-email']")
                        except:
                            print("email doesnt exist")
                            try:
                                elem=browser.find_element_by_xpath("//*[@id='/html/body/div[2]/div/form/input[2]']")
                            except:
                                print("email doesnt exist")






    elem.send_keys(user)
    sleep(2)

    try:
        pass_=browser.find_element_by_name("passwd")


    except:
        try:
            pass_=browser.find_element_by_name("password")

        except:
            print("email doesnt exist")
            flag_pass=True
    if(flag_pass):
        print("no password field")
    else:
        pass_.send_keys(passwordV)


    # print(pass_.is_displayed())





    # print(flag_pass)

    elem.send_keys(Keys.RETURN)
    sleep(10)
    file2=browser.page_source


    soup = BeautifulSoup(file2, "html.parser")
    for script in soup(["script", "style"]):
        script.decompose()
    # delete out tags

    content = list(soup.stripped_strings)
    #Cleaning the html text and converting the text in lower case.
    content=[re.sub('[^A-Za-z0-9]+', '', data.lower()) for data in content]

    # print(content)





    for x in content:
        print(x)
        if x in account_not_exist_msg:

            flag=True
        # else:
        #
        #     # print(x)
        #     accounts.append(i)

    if(flag):
        print("doesnt exist")
    else:

        accounts.append(i)



    browser.close()

def runProgram(user,link):


    myProxy = "127.0.0.1:9150"
    ip, port = myProxy.split(":")
    driver = webdriver.FirefoxProfile()
    driver.set_preference('network.proxy.type', 1)
    driver.set_preference('network.proxy.socks', ip)
    driver.set_preference('network.proxy.socks_port', int(port))
    options = Options()
    options.headless = True
    # browser = webdriver.Firefox(options=options)
    browser = webdriver.Firefox(driver)

    # renew_tor_ip()
    print(user)
    print("HI")
    # firefoxOptions=webdriver.ChromeOptions()
    # firefoxOptions.set_headless()
    # browser=webdriver.Chrome(options=firefoxOptions)
    # startTime=time.time()
    # doLogin(user)
    flag_pass=False


    browser.get(str(link))
    # sleep(2)                                         #Modified
    file1=browser.page_source
    sleep(2)                                          # WITHOUT this Economist, FOXNEWS gives an error
    # try:
    #     elem = browser.find_element_by_name("email")
    # except:
    #     pass
    try:
        elem=browser.find_element_by_xpath("//*[@id='user_email']")
    except:
        try:
            elem=browser.find_element_by_xpath("//input[@type='email']")
        except:
            print("email doesnt exist")
            try:
                elem=browser.find_element_by_name("email")
            except:
                print("text doesnt exist")
                try:
                    elem=browser.find_element_by_name("yid")
                except:
                    try:
                        elem=browser.find_element_by_xpath("//input[@type='text']")
                    except:
                        print("text doesnt exist")



    # elem = browser.find_element_by_name("usernameOrEmail")
    # except:
    #     pass
    # sleep(10)                                                #MODIFIED
    elem.send_keys(user)
    # time.sleep(2)                                             #MODIFIED
    try:
        pass_=browser.find_element_by_name("passwd")


    except:
        try:
            pass_=browser.find_element_by_name("password")

        except:
            print("email doesnt exist")
            flag_pass=True
    # print(pass_.is_displayed())
    # if(pass_.is_displayed()):
    #     pass_.send_keys('aaaaaaaa')

        # print("no password field")
    # else:
        # pass_.send_keys('aaaaaaaa')


    # elem = browser.find_element_by_name("password")
    # elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    sleep(5)                                #modified from 10 to 5
    # endTime=time.end()
    file2=browser.page_source

    # print(file2)
    # for request in browser.requests:
    #     if request.response:
    #         print(
    #             request.url,
    #             request.response.status_code,
    #             request.response.headers['Content-Type']
    #         )
    # diffVal=extract_html_diff.as_string(file2,file1)
    # soup = BeautifulSoup(diffVal, 'html.parser')
    # print(soup.get_text())
    soup = BeautifulSoup(file2, "html.parser")
    for script in soup(["script", "style"]):
        script.decompose()
    # delete out tags

    content = list(soup.stripped_strings)
    #Cleaning the html text and converting the text in lower case.
    content=[re.sub('[^A-Za-z0-9]+', '', data.lower()) for data in content]

    print(content)



    # print(len(diffVal))
    # diffLen=len(diffVal)
    # print(diffLen)
    # print(diffVal)
    # if diffVal in msg_database:
    # print(endTime-startTime)
    # print(diffVal)
    # re.sub('[^A-Za-z0-9]+', '', mystring)

    #print(content)
    # print(msg_database)
    for x in content:                                             # commented from 276 to 281
        #print("Enumerating")
        if x in msg_database:
            #print("!!1!!!!!!!!!!!!!!!!!! Matched wit")
            #print(x)
            accounts.append(i);




    browser.close()

if __name__ == "__main__":


    driwer = subprocess.Popen(r'C:\Users\User\Desktop\Tor Browser\Browser\firefox', close_fds=True)
    profile = FirefoxProfile(r'C:\Users\User\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')

    # emailID=["ccohen@aol.com" , "keijser@aol.com", "superman@gmail.com", "ajohnson@hotmail.com", "rnewman@aol.com", "sfoskett@hotmail.com", "seurat@aol.com", "richard@gmail.com", "punkis@gmail.com", "jadavis@outlook.com", "staffelb@att.net", "pplinux@icloud.com", "lamky@optonline.net", "ccoerhen@aol.com", "stafssfelb@att.net", "pplinsdux@icloud.com", "laamky@optonline.net","raaghavvd@gmail.com"];
    # emailID=set(emailID)

    with open('emailid.txt') as f:
        emailID= [line.rstrip() for line in f]
    # emailID=["raaghavvdevgon110@gmail.com","raaghavvd@gmail.com"]

    # usernames=["BegForMercy", "raaghavvd", "raghav1sep", "devgon.raaghavv", "raaghavvdevgon110", "ElNino", "EndlessFacepalms", "FreakingOblin", "GhostlyPresence", "GridlockAndKey", "HoofHearted666", "KungFuMonk", "NineTees", "PlzJustDie", "SeekNDestroy", "SinisterChill", "BegqwForMercy", "BasxasdxrainAxe", "Crazy1Mind", "DeatasdasdhWish", "Dis1asterMaster", "EaslNino", "EndlessFaaacepalms", "FrrreakingOblin", "GhossdtlyPreseasnce", "GrisadlockAndKey", "HoofaHearted666", "KsungFuMonk", "NinessTees", "sPlzJustDie", "sSeeksNDestroy", "SssinisddterChill"]
    with open('newlinks.txt') as f:
        links= [line.rstrip() for line in f]
    # with open('newlinks.txt') as f:
    #     links= [line.rstrip() for line in f]



    # linkName="https://auth.services.adobe.com/en_US/index.html?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2Fadobedotcom2%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%26state%3D%257B%2522ac%2522%253A%2522%2522%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=adobedotcom2&scope=creative_cloud%2CAdobeID%2Copenid%2Cgnav%2Cread_organizations%2Cadditional_info.projectedProductContext%2Csao.ACOM_CLOUD_STORAGE%2Csao.stock%2Csao.cce_private%2Cadditional_info.roles&denied_callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fdenied%2Fadobedotcom2%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%26response_type%3Dtoken%26state%3D%257B%2522ac%2522%253A%2522%2522%257D&state=%7B%22ac%22%3A%22%22%7D&relay=4827a8d2-b951-46ac-ae3a-4a2de4a089f2&locale=en_US&flow_type=token&idp_flow_type=login#/signup"

    f=0
    for l in links:
        accounts=[]
        # print(type(l))


        for i in emailID:
            if(f/2==0):
                renew_tor_ip()

            # accountNotPresentLogin(i,l)
            runProgram(i,l)
            f+=1

        print("The current Link crawled: ",l);
        print("The accounts", set(accounts));

