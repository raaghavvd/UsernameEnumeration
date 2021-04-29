from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

driver = webdriver.Edge(executable_path='msedgedriver')


print("The usernames present in Twitch are:")

for i in ["BegForMercy", "BraiasjdnkjnAxe", "CrazyMind", "DeathWaasdaish", "DisasterMaster", "ElNaaaino", "EndlessFacepalms", "FreakingOblin", "GhostlyPresence", "GridlockAndKey", "HoofHearted666", "KungFuMonk", "NineTees", "PlzJustDie", "SeekNDestroy", "SinisterChill", "BegqwForMercy", "BasxasdxrainAxe", "Crazy1Mind", "DeatasdasdhWish", "Dis1asterMaster", "EaslNino", "EndlessFaaacepalms", "FrrreakingOblin", "GhossdtlyPreseasnce", "GrisadlockAndKey", "HoofaHearted666", "KsungFuMonk", "NinessTees", "sPlzJustDie", "sSeeksNDestroy", "SssinisddterChill"]:
#for i in ["superman"]:

    user = i


    driver.get("https://www.twitch.tv/")
    element = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button/div/div')
    element.click()
    sleep(1)
    elem = driver.find_element_by_xpath("//input[@type='text']")
    elem.send_keys(user)
    elem.send_keys(Keys.TAB)
    sleep(2)
    p1 = driver.page_source
    if "*This username is unavailable." in p1:
        print(user)
