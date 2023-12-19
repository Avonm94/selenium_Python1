# Webpage Navigation
###########################################################################################

# Importing the necessary modules
from selenium import webdriver
import time as t

# Creating a Chrome WebDriver instance
driver = webdriver.Chrome()

# Maximizing the browser window
driver.maximize_window()
print("Browser window maximized")

# Opening Facebook and waiting for 5 seconds
driver.get("https://www.facebook.com")
print("Opened Facebook")
print("Current URL:", driver.current_url)
print("Page Title:", driver.title)
t.sleep(5)

# Opening Instagram and waiting for 5 seconds
driver.get("https://www.instagram.com")
print("Opened Instagram")
print("Current URL:", driver.current_url)
print("Page Title:", driver.title)
t.sleep(5)

# Refreshing the current page and waiting for 5 seconds
driver.refresh()
print("Refreshed the page")
print("Current URL:", driver.current_url)
print("Page Title:", driver.title)
t.sleep(5)

# Navigating back to the previous page and waiting for 5 seconds
driver.back()
print("Navigated back to the previous page")
print("Current URL:", driver.current_url)
print("Page Title:", driver.title)
t.sleep(5)

# Navigating forward to the next page and waiting for 5 seconds
driver.forward()
print("Navigated forward to the next page")
print("Current URL:", driver.current_url)
print("Page Title:", driver.title)
t.sleep(5)

# Closing the browser window
driver.close()
print("Closed the browser")

# -----------------------------------------------------------------------------------------