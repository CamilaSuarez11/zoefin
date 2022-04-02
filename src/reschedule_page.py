import time

from selenium.webdriver.common.by import By

from zoefin.utilities import utilities

utilities.init()


def click_date_reschedule():
    utilities.driver.find_element(By.XPATH, "//*[@id='calendar_container']/div[1]/div[1]/div[1]/div[3]/div[11]").click()


def validation_day():
    return utilities.driver.find_element(By.XPATH, "//*[@id='calendar_container']/div[1]/div/div[2]/div[1]").text


def select_time():
    utilities.driver.find_element(By.XPATH, "//*[@id='calendar_container']/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[4]").click()


def validation_time():
    return utilities.driver.find_element(By.XPATH, "//*[@id='calendar_container']/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[3]").text


def click_type_of_call():
    utilities.driver.find_element(By.XPATH, "//*[@id='calendar_container']/div[1]/div[2]/div/label[1]/div").click()


def validation_type_of_call():
    return utilities.driver.find_element(By.XPATH, "//*[@id='calendar_container']/div[1]/div[2]/div/label[1]/div").text


def click_reschedule():
    utilities.driver.find_element(By.XPATH, "//*[@id='calendar_container']/div[2]/button[1]").click()


def validation_pop_up_window():
    return utilities.driver.find_element(By.XPATH, "//*[@id='ZUIModal-children-container']/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/ul/li[1]/span").text


def validation_hour():
    return utilities.driver.find_element(By.XPATH, "//*[@id='ZUIModal-children-container']/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/ul/li[2]/span").text


def validation_duration():
    return utilities.driver.find_element(By.XPATH, "//*[@id='ZUIModal-children-container']/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/ul/li[3]/span").text


def validation_type():
    return utilities.driver.find_element(By.XPATH, "//*[@id='ZUIModal-children-container']/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/ul/li[4]/div/span").text


def click_confirm():
    utilities.driver.find_element(By.XPATH,  "//*[@id='ZUIModal-children-container']/div/div/div[1]/div[2]/div/div/div/div/div/div[3]/div/button[2]").click()


def validation_reschedule_successfully():
    return utilities.driver.find_element(By.XPATH, "//*[@id='ZUIModal-children-container']/div/div/div[1]/div[2]/div/div/div/div/div/p[1]/span[2]").text
