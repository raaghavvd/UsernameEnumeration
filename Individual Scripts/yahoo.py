#  User Enum Yahoo
# TWO CHANGES: Find element by name AND USE TAB instead of RETURN

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

driver = webdriver.Edge(executable_path='msedgedriver')

print("The usernames present in Yahoo are:")

for i in ["BegForMercy", "superman", "BraiasjdnkjnAxe", "CrazyMind", "DeathWaasdaish", "DisasterMaster", "ElNaaaino", "EndlessFacepalms", "FreakingOblin", "GhostlyPresence", "GridlockAndKey", "HoofHearted666", "KungFuMonk", "NineTees", "PlzJustDie", "SeekNDestroy", "SinisterChill", "BegqwForMercy", "BasxasdxrainAxe", "Crazy1Mind", "DeatasdasdhWish", "Dis1asterMaster", "EaslNino", "EndlessFaaacepalms", "FrrreakingOblin", "GhossdtlyPreseasnce", "GrisadlockAndKey", "HoofaHearted666", "KsungFuMonk", "NinessTees", "sPlzJustDie", "sSeeksNDestroy", "SssinisddterChill"]:
#for i in ["supeasdarman"]:

    user = i

    driver.get("https://login.yahoo.com/account/create?.lang=en-US&src=homepage&activity=ybar-signin&pspid=2023538075&.done=https%3A%2F%2Fwww.yahoo.com%2F&specId=yidReg&done=https%3A%2F%2Fwww.yahoo.com%2F")
    p1 = driver.page_source
    #elem=driver.find_element_by_xpath("//*[@id='usernamereg-yid']")
    elem=driver.find_element_by_name("yid")
    elem.send_keys(user)
    elem.send_keys(Keys.TAB)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2,p1)
    if "A Yahoo account already exists with this email address." in p3:
        print(i)
