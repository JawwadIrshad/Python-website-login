#main.py
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def close_flash_message(driver):
    try:
        close_btn = driver.find_element(By.CSS_SELECTOR, "#flash a.close")
        close_btn.click()
    except:
        pass
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(
    options=options,
    use_subprocess=True,
    version_main=143  
)

wait = WebDriverWait(driver, 10)

try:
    driver.get("https://the-internet.herokuapp.com")
    time.sleep(5)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    )).click()
    time.sleep(5)

    # Enter the username nd password and login
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(EC.presence_of_element_located((By.ID, "flash")))
    success_message = driver.find_element(By.ID, "flash").text
    logout_button = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "a.button.secondary.radius")
    ))

    if "You logged into a secure area!" in success_message and logout_button.is_displayed():
        print("✅ Login successful & Logout button visible")
    else:
        print("❌ Login validation failed")

    
    close_flash_message(driver)

    logout_button.click()

 
    wait.until(EC.presence_of_element_located((By.ID, "flash")))
    logout_message = driver.find_element(By.ID, "flash").text

    wait.until(EC.presence_of_element_located((By.ID, "username")))
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    if "You logged out of the secure area!" in logout_message and \
       username_field.is_displayed() and password_field.is_displayed():
        print("✅ Logout successful & Login page displayed again")
    else:
        print("❌ Logout validation failed")

    close_flash_message(driver)

    time.sleep(5)

finally:
    driver.quit()
