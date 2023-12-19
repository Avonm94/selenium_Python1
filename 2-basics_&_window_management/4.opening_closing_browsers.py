# Opening & closing browser.
###########################################################################################

# Import the webdriver module from the selenium library
from selenium import webdriver

# Import a time library to use sleep function
import time as t

# -----------------------------------------------------------------------------------------

# Path configuration:

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# options = webdriver.ChromeOptions()
# service = ChromeService(executable_path=CHROMEDRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=options)


# Make sure you have the required browser drivers (chromedriver.exe, geckodriver.exe, and
# msedgedriver.exe) available in your system PATH or provide their paths explicitly in the webdriver
# instantiation if they are not in the PATH.

# Note: In Selenium4.0 and later versions, drivers are not required to download as it's already
# downloaded from server, even no need to specify the driver Path.

# In Selenium 4, you’ll need to set the driver’s executable_path from a Service object to prevent deprecation warnings.
# (Or don’t set the path and instead make sure that the driver you need is on the System PATH.)

# from selenium official website.


# -----------------------------------------------------------------------------------------
# Opening the browser,

# Create an object for the webdriver w.r.t. browser
chrome_driver = webdriver.Chrome()
edge_driver = webdriver.Edge()
ff_driver = webdriver.Firefox()

# Note: make sure that Browser name starts with a capital letter,
# or else you'll get type error: module not callable.

# Above code will open the respective browser with a blank tab.

# -----------------------------------------------------------------------------------------

# use sleep to delay/hold execution of the script in seconds.
t.sleep(5)

# -----------------------------------------------------------------------------------------

# Closing browser,
# In Selenium, there are two methods to close a browser window: close() and quit() .

# close():

# The close() method is used to close the current browser window or tab that the WebDriver
# is currently handling.
# It leaves other open browser windows or tabs unaffected.
# It is generally used when you want to close a specific browser window or tab, but keep the
# WebDriver session running.


# quit():

# The quit() method is used to exit the entire WebDriver session, closing all open browser
# windows or tabs associated with that WebDriver instance.
# It not only closes the browser windows but also releases the associated driver executable
# process and resources.
# It is recommended to use quit() at the end of your script to ensure all resources are
# properly released.


# closing the browsers.
chrome_driver.close()
# chrome_driver.quit()

edge_driver.close()
# edge_driver.quit()

ff_driver.close()
# ff_driver.quit()


# -----------------------------------------------------------------------------------------

# Why Close and Quit?
# Closing and quitting browser windows is essential for several reasons:
# 1. Resource Management:
# Browsers consume system resources. If you have multiple browser windows or tabs open,
# they can collectively use a significant amount of memory. Closing unnecessary windows helps
# manage resources efficiently.

# 2. Clean Test Environment:
# In automated testing, it's crucial to start with a clean and consistent state for each test. Closing
# or quitting browsers ensures that each test starts with a fresh browser instance.

# 3. Preventing Memory Leaks:
# Closing or quitting the browser helps prevent memory leaks. Not closing browser instances
# properly may lead to memory buildup over time, causing instability or unexpected behavior.

# 4. Driver Cleanup:
# The quit() method releases the WebDriver executable process and resources. This is
# important, especially if your script spawns multiple browser instances during its execution.
# Failing to quit the WebDriver could result in lingering processes.

# In summary, while close() is used to close a specific browser window, quit() is used to terminate
# the entire WebDriver session, closing all associated windows and releasing resources. Properly
# managing browser instances ensures efficient resource utilization and a clean testing environment. It's
# a good practice to use quit() at the end of your script to ensure proper cleanup.

###########################################################################################

# from here onwards, I'll write scripts for only one browser.
# to execute these scripts for other browsers just have to change the browser object.

###########################################################################################

# To make the script easy to remember, I will divide it into 3 sections.
# header: will consist all import statements.
# body: consist all the browser-related statement
# footer: will have closing/quitting statement

###########################################################################################
