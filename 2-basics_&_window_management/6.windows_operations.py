# Perform browser-windows related operations.
###########################################################################################
# Selenium always launches the browser in windowed mode.
# -----------------------------------------------------------------------------------------
# Import the necessary module from Selenium
from selenium import webdriver
# Import the 'time' module and alias it as 't' for brevity
import time as t

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()
print('Step 1: Open the Browser')

# Maximize the browser window
driver.maximize_window()
print('Step 2: Maximize the Window')
t.sleep(5)

# Minimize the browser window
driver.minimize_window()
print('Step 3: Minimize the Window')
t.sleep(5)

# Switch to full-screen mode
driver.fullscreen_window()
print('Step 4: Enter Full screen Mode')
t.sleep(5)

# Set the window size to 500x500 pixels
driver.set_window_size(500, 500)
print('Step 5: Set Window Size to 500x500 pixels')
t.sleep(5)

# Set the window position to (300, 300) on the screen
driver.set_window_rect(300, 300)
print('Step 6: Set Window Position to (300, 300)')
t.sleep(5)

# Set the window position to (400, 400) on the screen
driver.set_window_position(400, 400)
print('Step 7: Set Window Position to (400, 400)')
t.sleep(5)

# Close the browser window
driver.close()
print('Step 8: Close the Browser')

# -----------------------------------------------------------------------------------------
