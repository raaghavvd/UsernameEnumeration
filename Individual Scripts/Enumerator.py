from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep,time
from seleniumwire import webdriver
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


# r=req.get('https://jasonrigden.com')
# r = session.get('https://jasonrigden.com')

# 'an adobe account with this email address already exists'


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
    sleep(3)

    file1=browser.page_source

    passwordV='aaaaaaaaa'

    try:
        elem = browser.find_element_by_name("username")
    except:
        # print("username doesnt exist")
        try:
            elem=browser.find_element_by_name("usernameOrEmail")
        except:
            # print("usernameOrEmail doesnt exist")
            try:
                elem=browser.find_element_by_name("email")
            except:
                # print("email doesnt exist")
                try:
                    elem=browser.find_element_by_name("ap_email")
                except:
                    # print("email doesnt exist")
                    try:
                        elem=browser.find_element_by_name("userid")
                    except:
                        # print("email doesnt exist")
                        try:
                            elem=browser.find_element_by_xpath("//*[@id='forgot-password-email']")
                        except:
                            # print("email doesnt exist")
                            try:
                                elem=browser.find_element_by_xpath("//*[@id='/html/body/div[2]/div/form/input[2]']")
                            except:
                                # print("email doesnt exist")
                                try:
                                    elem=browser.find_element_by_xpath("//input[@type='email']")
                                except:
                                    print("can't enumerate")






    elem.send_keys(user)
    sleep(2)

    # try:
    #     pass_=browser.find_element_by_name("passwd")
    #
    #
    # except:
    #     try:
    #         pass_=browser.find_element_by_name("password")
    #
    #     except:
    #         print("email doesnt exist")
    #         flag_pass=True
    # if(flag_pass):
    #     print("no password field")
    # else:
    #     pass_.send_keys(passwordV)


    # print(pass_.is_displayed())





    # print(flag_pass)
    # if('box.com' in link):
    #     print("BOX")
    #
    #     elem.send_keys(Keys.TAB)
    #
    # else:

    elem.send_keys(Keys.RETURN)
    sleep(10)
    file2=browser.page_source


    soup = BeautifulSoup(file2)
    for script in soup(["script", "style"]):
        script.decompose()
    # delete out tags

    content = list(soup.stripped_strings)
    #Cleaning the html text and converting the text in lower case.
    content=[re.sub('[^A-Za-z0-9]+', '', data.lower()) for data in content]

    print(content)





    for x in content:
        # print(x)
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
    options = Options()
    options.add_argument("--headless") # Runs Chrome in headless mode.
    print(user)
    print("HI")
    # firefoxOptions=webdriver.ChromeOptions()
    # firefoxOptions.set_headless()
    # browser=webdriver.Chrome(options=firefoxOptions)
    # startTime=time.time()
    # doLogin(user)
    flag_pass=False


    browser.get(str(link))
    sleep(3)
    file1=browser.page_source
    # try:
    #     elem = browser.find_element_by_name("email")
    # except:
    #     pass
    # try:
    #     elem=driver.find_element_by_name("email-localpart")
    # except:
    #     print("sadsadas")
    try:
        elem=browser.find_element_by_xpath("//*[@id='user_email']")
    except:
        try:
            elem=browser.find_element_by_xpath("//input[@type='email']")
        except:
            # print("email doesnt exist")
            try:
                elem=browser.find_element_by_name("email")
            except:
                # print("text doesnt exist")
                try:
                    elem=browser.find_element_by_xpath("//input[@type='text']")
                except:
                    # print("text doesnt exist")
                    try:
                        elem=driver.find_element_by_name("yid")
                    except:
                        print("can't enumerate")
                        exit(0)







    # elem = browser.find_element_by_name("usernameOrEmail")
    # except:
    #     pass
    elem.send_keys(user)
    time.sleep(2)
    try:
        pass_=browser.find_element_by_name("passwd")


    except:
        try:
            pass_=browser.find_element_by_name("password")

        except:
            print("password doesnt exist")
            flag_pass=True
    # print(pass_.is_displayed())
    # if(pass_.is_displayed()):
    #     pass_.send_keys('aaaaaaaa')

        # print("no password field")
    # else:
        # pass_.send_keys('aaaaaaaa')
    # if(flag_pass):
    #     print("sdasd")
    # else:
    #     if(pass_.is_displayed):
    #         pass_.send_keys('QWErty!@#123shd7')




    # elem = browser.find_element_by_name("password")
    # elem.send_keys(password)
    # print(flag_pass)
    if('box.com' in link ):
        print("BOX")

        elem.send_keys(Keys.TAB)
    elif('engadget.com' in link):
        elem.send_keys(Keys.TAB)
    elif('fastmail.com' in link):
        elem.send_keys(Keys.TAB)
    elif('ibm.com' in link):
        elem.send_keys(Keys.TAB)
    elif('imgur .com' in link):
        elem.send_keys(Keys.TAB)
    elif('independent.co.uk' in link):
        elem.send_keys(Keys.TAB)
    elif('techcrunch.com' in link):
        elem.send_keys(Keys.TAB)
    elif('indeed.com' in link):
        print('indeed')
        elem.send_keys(Keys.TAB)
    elif('zippyshare.com' in link):
        elem.send_keys(Keys.TAB)
    elif('samsung.com' in link):
        elem.send_keys(Keys.TAB)
    elif('wondershare.com' in link):
        elem.send_keys(Keys.TAB)
    elif('redtube.com' in link):
        elem.send_keys(Keys.TAB)








    else:

        elem.send_keys(Keys.RETURN)
    sleep(8)
    file2=browser.page_source


    soup = BeautifulSoup(file2)
    for script in soup(["script", "style"]):
        script.decompose()
    # delete out tags

    content = list(soup.stripped_strings)
    #Cleaning the html text and converting the text in lower case.
    content=[re.sub('[^A-Za-z0-9]+', '', data.lower()) for data in content]






    print(content)
    for x in content:
        # print("Enumerating")
        if x in msg_database:
            print("Match found")
            accounts.append(i);




    browser.close()

if __name__ == "__main__":

    if sys.argv[2]=='-username':
        with open('usernames.txt') as f:
            emailID= [line.rstrip() for line in f]
    elif sys.argv[2]=='-email':
        print("FETCHING EMAILS...")
        with open('emailID.txt') as f:
            emailID= [line.rstrip() for line in f]




    # usernameList=["superman", "batman", "asdjhbasbdajd"]



    with open('newlinks.txt') as f:
        links= [line.rstrip() for line in f]



    f=0
    for l in links:
        accounts=[]


        for i in emailID:
            # if(f/2==0):
            if sys.argv[3]=='t':
                print('tor')

                renew_tor_ip()
            # else:
                # continue
            #print(get_current_ip())


            # if(f/4==0):
            if sys.argv[1]=='-P':
                runProgram(i,l)
                print("Checking if username exists..")
            elif sys.argv[1]=='-NP' :
                print("Checking if username doesnt exists..")


                accountNotPresentLogin(i,l)
            else:
                print("enter valid argument.")
                sys.exit(0)
            f+=1
        print("The current Link crawled: ",l);
        print("The accounts", set(accounts));

#check if there is extra tag after request, check with the og page html. (inner html, ,login div box)


#TryCatch more websites:
#gather more website error messages
# test this on more websites.