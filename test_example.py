from selenium import webdriver
from selenium.webdriver.common.by import By

# Khởi tạo WebDriver (Sử dụng Chrome)
driver = webdriver.Chrome()

# Mở trang web
driver.get("https://www.google.com")

# Kiểm tra tiêu đề trang
assert "Google" in driver.title

# Tìm ô tìm kiếm và nhập nội dung
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.submit()

# Đóng trình duyệt
driver.quit()
