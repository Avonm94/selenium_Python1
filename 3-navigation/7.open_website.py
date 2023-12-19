# open the browser enter url.
# to enter url into browser we will use get() method. where we pass the url as a string.
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
driver.get('https://portal-uat.laboredge.com/')
print(f"Navigating to: {driver.current_url}")
t.sleep(5)  # Waiting for 5 seconds to observe the loaded page

# Storing a URL in a variable and navigating to it using the get() method
website_url = 'https://www.globalsqa.com/demo-site/'
driver.get(website_url)
print(f"Navigating to: {driver.current_url}")

# Closing the browser window
driver.close()
print("Browser window closed.")

# -----------------------------------------------------------------------------------------