from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--lang=en-US")

# to remove the banner
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

file_path = "puzzles.txt"  

base_url = "https://lichess.org/training/"
urls = []

with open(file_path, "r") as file:
    for line in file:
        line = line.strip() 
        url = base_url + line
        urls.append(url)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver = webdriver.Chrome(service=Service("chrome"), options=options)
wait = WebDriverWait(driver, 100)

def open_new_tab(url):
    driver.execute_script(f"window.open('{url}', '_blank');") 

def switch_to_new_tab():
    driver.switch_to.window(driver.window_handles[-1]) 

def close_current_tab():
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])

for url in urls:
    open_new_tab(url)  
    close_current_tab()
    switch_to_new_tab() 
    element = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'complete'), 'Success!'))
    if element:
        continue

driver.quit()