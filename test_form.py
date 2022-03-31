import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture
def setUp():
    global name,release,director_name,distributor,producer,language,driver
    name=input("Enter name")
    release = input("Enter name")
    director_name = input("Enter name")
    distributor = input("Enter name")
    producer = input("Enter name")
    language = input("Enter name")
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()
def test_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/")
    driver.find_element_by_name("name").send_keys(name)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys(release)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/input").send_keys(director_name)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[4]/td[2]/input").send_keys(distributor)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[5]/td[2]/input").send_keys(producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select").send_keys(language)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[7]/td[2]/button").click()
    driver.close()
    print("test case has successfully completed")



