from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")
options.add_argument("--user-data-dir=/tmp/chrome-user-data")

# Lấy đường dẫn Chrome từ biến môi trường
chrome_bin_path = os.getenv("CHROME_BIN", "/usr/bin/chromium-browser")
options.binary_location = chrome_bin_path

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")

print(driver.title)
driver.quit()
