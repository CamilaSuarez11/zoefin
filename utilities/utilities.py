import sys
from selenium import webdriver

print (sys.path[1])
ruth="/chromedriver"
system=sys.path[1]
path=system+ruth
print(path)
driver=None

def init():
    global driver
    driver=webdriver.Chrome(path)
    driver.maximize_window()
    driver.get("https://portal-test.zoefin.com/reschedule/ef6e2c60-9fec-11ec-9d51-4b9749daba94")
    driver.implicitly_wait(5)

def close():
    global driver
    driver.quit()

