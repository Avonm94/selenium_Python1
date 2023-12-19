# opening & closing chrome
###########################################################################################
print("Script execution started.")
# importing selenium and webdriver
from selenium import webdriver
import time
print("All required library imported successfully.")

# -----------------------------------------------------------------------------------------

driver = webdriver.Chrome()  # launching browser
print("Chrome browser launched successfully.")
time.sleep(5)  # waiting for 5 sec.
print("Waited for 5 seconds successfully.")

# -----------------------------------------------------------------------------------------

driver.close()  # closing browser.
print("Chrome browser closed successfully")
print("Script execution ended.")
# -----------------------------------------------------------------------------------------