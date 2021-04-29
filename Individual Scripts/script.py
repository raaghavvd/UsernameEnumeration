from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff
import requests
import time
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
driver = webdriver.Edge(executable_path='msedgedriver')
##maybe remove special characters from the inner html diff.
##convert everything to lower case.
msg_database=['That username is taken. Try another.','The password you’ve entered is incorrect.','is already a Microsoft account. Please try a different email address.',
'An Adobe account with this email address already exists','This email address is not available. Choose a different address.','This email is already connected to an account','This email address is already in use.']
accounts=[]

def get_current_ip():

    session=requests.session()
    session.proxies={}
    session.proxies['http']='socks5h://localhost:9050'
    session.proxies['https']='socks5h://localhost:9050'
    try:
        r=session.get('http://httpbin.org/ip')
    except Exception as e:
        print(str(e))
    else:
        return r.text
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="HkB3IDWD#143")  ##this will be different!
        controller.signal(Signal.NEWNYM)

# r=req.get('https://jasonrigden.com')
# r = session.get('https://jasonrigden.com')





def runProgram(user,link):
    # renew_tor_ip()
    print(user);
    firefoxOptions=webdriver.FirefoxOptions()
    firefoxOptions.set_headless()
    browser=webdriver.Firefox(options=firefoxOptions)
    browser.get(link)
    file1=browser.page_source
    # try:
    #     elem = browser.find_element_by_name("email")
    # except:
    #     pass
    try:
        elem=browser.find_element_by_xpath("//input[@type='email']")
    except:
        print("email doesnt exist")
        try:
            elem=browser.find_element_by_xpath("//input[@type='text']")
        except:
            print("text doesnt exist")


    # elem = browser.find_element_by_name("usernameOrEmail")
    # except:
    #     pass


    elem.send_keys(user)
    # elem = browser.find_element_by_name("password")
    # elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    sleep(10)
    file2=browser.page_source
    # print(file2)
    diffVal=extract_html_diff.as_string(file2,file1)
    # soup = BeautifulSoup(diffVal, 'html.parser')
    # print(soup.get_text())


    # print(len(diffVal))
    # diffLen=len(diffVal)
    # print(diffLen)
    # print(diffVal)
    if "An Adobe account with this email address already exists" in diffVal:
       accounts.append(i);

    browser.close()

if __name__ == "__main__":
    emailID=["ccohen@aol.com", "superman@gmail.com", "keijser@aol.com", "superman@gmail.com", "ajohnson@hotmail.com", "rnewman@aol.com", "sfoskett@hotmail.com", "seurat@aol.com", "richard@gmail.com", "punkis@gmail.com", "jadavis@outlook.com", "staffelb@att.net", "pplinux@icloud.com", "lamky@optonline.net", "ccoerhen@aol.com", "keijserqer@aol.com", "ajohneesdson@hotmail.com", "rnewman@aol.com", "sfosksdett@hotmail.com", "seusdrat@aol.com", "richard@gmail.com", "pssunkis@gmail.com", "jadavssis@outlook.com", "stafssfelb@att.net", "pplinsdux@icloud.com", "laamky@optonline.net","raaghavvd@gmail.com"];

    # usernames=["BegForMercy", "raaghavvd", "raghav1sep", "devgon.raaghavv", "raaghavvdevgon110", "ElNino", "EndlessFacepalms", "FreakingOblin", "GhostlyPresence", "GridlockAndKey", "HoofHearted666", "KungFuMonk", "NineTees", "PlzJustDie", "SeekNDestroy", "SinisterChill", "BegqwForMercy", "BasxasdxrainAxe", "Crazy1Mind", "DeatasdasdhWish", "Dis1asterMaster", "EaslNino", "EndlessFaaacepalms", "FrrreakingOblin", "GhossdtlyPreseasnce", "GrisadlockAndKey", "HoofaHearted666", "KsungFuMonk", "NinessTees", "sPlzJustDie", "sSeeksNDestroy", "SssinisddterChill"]
    linkName="https://auth.services.adobe.com/en_US/index.html?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2Fadobedotcom2%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%26state%3D%257B%2522ac%2522%253A%2522%2522%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=adobedotcom2&scope=creative_cloud%2CAdobeID%2Copenid%2Cgnav%2Cread_organizations%2Cadditional_info.projectedProductContext%2Csao.ACOM_CLOUD_STORAGE%2Csao.stock%2Csao.cce_private%2Cadditional_info.roles&denied_callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fdenied%2Fadobedotcom2%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%26response_type%3Dtoken%26state%3D%257B%2522ac%2522%253A%2522%2522%257D&state=%7B%22ac%22%3A%22%22%7D&relay=4827a8d2-b951-46ac-ae3a-4a2de4a089f2&locale=en_US&flow_type=token&idp_flow_type=login#/signup"

    x=0
    for i in emailID:
        if(x/4==0):
            renew_tor_ip();
        runProgram(i,linkName)
        x+=1

    print(accounts);

#check if there is extra tag after request, check with the og page html. (inner html, ,login div box)


#TryCatch more websites:
#gather more website error messages
# test this on more websites.
