# open browser, open application, and identify an element and perform action.
###########################################################################################

# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

# Create a Chrome WebDriver instance and maximize the window
driver = webdriver.Chrome()
driver.maximize_window()

# Open the login page
driver.get("https://practicetestautomation.com/practice-test-login/")
t.sleep(5)

# Find the username field, enter 'student', and wait
username = driver.find_element(By.ID, 'username')
username.send_keys('student')
t.sleep(5)

# Find the password field, enter 'Password123', and wait
password = driver.find_element(By.NAME, 'password')
password.send_keys('Password123')
t.sleep(5)

# Find and click the submit button and wait
submit_btn = driver.find_element(By.CLASS_NAME, 'btn')
submit_btn.click()
t.sleep(5)

# Define expected URL and title after successful login
exp_url = 'https://practicetestautomation.com/logged-in-successfully/'
exp_title = 'Logged In Successfully | Practice Test Automation'

# Print current page title and URL
print("Current Page Title:", driver.title)
print("Current Page URL:", driver.current_url)

# Check if the actual URL and title match the expected ones
if exp_url == driver.current_url and exp_title == driver.title:
    print('Test Pass')
else:
    print('Test Fail')

# Find and click the logout button and wait
logout_btn = driver.find_element(By.LINK_TEXT, 'Log out')
logout_btn.click()
t.sleep(5)

# Close the browser
driver.close()

# -----------------------------------------------------------------------------------------
