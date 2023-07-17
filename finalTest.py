import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # chromedriver_path = "C:\Webdriver\chromedriver.exe"
    # service = Service(executable_path=chromedriver_path)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://app.jubelio.com/login')
    # driver.maximize_window()
    yield driver

def test_login(driver):
    username_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")

    username = "qa.rakamin.jubelio@gmail.com"
    password = "Jubelio123!"

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_menu")))

    time.sleep(5)
    driver.quit()

def test_inventory(driver):
    # step login 
    username_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")

    username = "qa.rakamin.jubelio@gmail.com"
    password = "Jubelio123!"

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_menu")))

    # step inventory
    driver.get('https://app.jubelio.com/home/inventory')

    # click button Penyusaian Persediaan
    penyesuaian_stock = driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]")
    penyesuaian_stock.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Penyesuaian Persediaan')]")))

    # Input product
    scan_barang = driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]")
    product = "AFG-001"
    scan_barang.send_keys(product, Keys.ENTER)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'AFG-001 - Action Figure - Gundam Evo')]")))

    # Click button Simpan
    save_button = driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]")
    save_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'AFG-001')]")))

    time.sleep(5)
    driver.quit()