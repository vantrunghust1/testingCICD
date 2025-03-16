from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")  # Tránh vấn đề quyền hạn trong môi trường CI
options.add_argument("--disable-dev-shm-usage")  # Khắc phục lỗi bộ nhớ chia sẻ
options.add_argument("--headless")  # Chạy không giao diện (bắt buộc trên CI/CD)
options.add_argument("--user-data-dir=/tmp/chrome-user-data")  # Đặt thư mục user-data riêng

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")

print(driver.title)
driver.quit()
