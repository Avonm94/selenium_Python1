###########################################################################################

# WebDriver is a module, and it will consist different classes, functions, constructors, method etc.
# to use this selenium package is installed.
# as per different browser, webdriver will have class.

# ex:
# chrome --> Chrome()
# edge -->  Edge()
# ff --> Firefox ()

# to perform further operations, we will use methods present in the particular classes.

# -----------------------------------------------------------------------------------------
# List of commands with syntax in web Driver: -

# Command -->  Description

# Element.sendKeys(“inputtext”) --> It will enter some text into an input box.
# driver.get(“URL”) --> Used to navigate an application.
# Element.clear() --> It clears the content from the input box.
# Select.deselectAll() --> It deselects OPTION from FIRST select on page.
# driver.selectByVisibleText(“some text”) --> It selects OPTION with the input which is specified by user.
# driver.switchTo().window(“windowName”) --> It moves and focuses from one window to another.
# driver.switchTo().alert() --> It will help in handling the alerts.
# driver.navigate().to(“URL”) --> It will navigate to URL
# driver.navigate().forward() --> It will navigate forward.
# driver.navigate().back() --> It will navigate back.
# driver.close() --> It will close the current browser associated with driver.
# driver.quit() --> It quits the driver and closes all windows of driver.
# driver.refresh() --> It quits will refresh the current page.

# -----------------------------------------------------------------------------------------

# The webdriver module in Selenium provides various methods for interacting with web browsers.
# Below are some common methods available in Selenium WebDriver:

# Navigation:
# get(url): Load a new web page in the current browser window.
# back(): Navigate back to the previous page.
# forward(): Navigate forward to the next page.
# refresh(): Refresh the current page.

# Window Management:
# maximize_window(): Maximize the current browser window.
# minimize_window(): Minimize the current browser window.
# fullscreen_window(): Make the current browser window full screen.
# set_window_size(width, height): Set the size of the current browser window.
# set_window_position(x, y): Set the position of the current browser window.

# Element Location:
# find_element(by, value): Find the first element using the given method and value.
# find_elements(by, value): Find all elements using the given method and value.

# Element Interaction:
# click(): Click on an element.
# send_keys(keys): Simulate typing into an element.
# clear(): Clear the contents of an input field.
# submit(): Submit a form.

# Browser Information:
# title: Get the title of the current page.
# current_url: Get the URL of the current page.
# page_source: Get the source code of the current page.

# Alert Handling:
# switch_to.alert: Switch to the currently active alert on the page.
# alert.accept(): Accept the alert.
# alert.dismiss(): Dismiss the alert.
# alert.text: Get the text of the alert.

# Frame Handling:
# switch_to.frame(frame_reference): Switch to the specified frame.
# switch_to.default_content(): Switch back to the default content.

# Timeouts:
# implicitly_wait(time): Set a default waiting time for the browser to wait for an element to be found.
# set_page_load_timeout(time): Set the maximum time to wait for a page to load.

# Cookies:
# add_cookie(cookie_dict): Add a cookie to the current session.
# get_cookies(): Get all cookies.

# These are just some of the commonly used methods in Selenium WebDriver.
# The Selenium WebDriver documentation provides a comprehensive list of methods,
# and their usage for different programming languages.


# -----------------------------------------------------------------------------------------

# summery :

# Web driver: -
# The selenium webdriver is the automation tool used to automate the test scripts written in selenium.

# Webdriver installation:-
# Chrome:https:\\sites.google.com/a/chromium.org/chromedriver/downloads

# Libraries need to import: -
# From selenium import webdriver
# Import time

# Selenium library: -
# It is used for the automation and control web driver also performs actions like goto website link, etc.

# Time library: -
# Used for sleep function because selenium works when all elements of pages are loaded.
# sleep function will pause (delays) the execution of the script for given time (in seconds)

# now we are good to go..

###########################################################################################