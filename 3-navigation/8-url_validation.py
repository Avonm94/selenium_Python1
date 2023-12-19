# open the browser, enter url and validate the website using website title.
###########################################################################################

# Importing the necessary modules
from selenium import webdriver
import time as t

# Creating a Chrome WebDriver instance
driver = webdriver.Chrome()
print("WebDriver instance created.")

# Maximizing the browser window for better visibility
driver.maximize_window()
print("Browser window maximized.")

# Directly navigating to a URL using the get() method
driver.get('https://www.facebook.com/')
print(f"Navigating to: {driver.current_url}")
t.sleep(5)  # Waiting for 5 seconds to observe the loaded page

# Validating the title
expected_title = 'Facebook – log in or sign up'
actual_title = driver.title

if expected_title == actual_title:
    print(f'Title validation successful! Actual Title: {actual_title}')
else:
    print(f'Title validation failed. Expected Title: {expected_title}, Actual Title: {actual_title}')

# Closing the browser window
driver.close()
print("Browser window closed.")

# -----------------------------------------------------------------------------------------

# Selenium WebDriver, driver.title refers to a property that allows you to retrieve the title of the current web page
# that the WebDriver is interacting with.
# The title is the text typically displayed in the title bar of the browser window or tab.

# In summary, driver.title is a property in Selenium WebDriver that allows you to extract and work with the title of
# the currently loaded web page.
# It is commonly used in test automation scripts to verify that the expected page has been successfully navigated to.

# -----------------------------------------------------------------------------------------

# example 2:

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://portal-uat.laboredge.com/')

title = 'Nexus'

if title == driver.title:
    print(f'Pass:', {title})
else:
    print('Fail')

driver.close()
# -----------------------------------------------------------------------------------------