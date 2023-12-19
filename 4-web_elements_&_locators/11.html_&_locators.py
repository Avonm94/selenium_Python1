# HTML & Locators
###########################################################################################

# HTML:
# As we know, all web-application's UIs are designed using HTML (hyper text markup language).
# this html has element 3:

# Tag name:
# any word/letter that is started or written with/in angular brackets is a tag name.
# Ex: <a, <a> or <span , <span>

# Attribute:
# anything that is a combination of key and value pair.
# Ex: (attribute name = attribute value)
# id = 'user'
# Here, attribute name = id , attribute value = 'Name'

# Text:
# anything that is written outside, of the angular brackets.
# Ex: <a> this is text </a>

# -----------------------------------------------------------------------------------------

# Ex:
# <input type="text" name="username" value="" id="username" class="textField" placeholder="Username">
# input = Tag name
# attributes = type="text", name="username", value=""....etc.

# <div>Login </div>
# div = tag name
# Login = text

#  these are called as locators, which will help us find elements.

###########################################################################################

# Locators:

# Locators refer to unique identifiers or attributes used to locate and interact with elements on a web page,
# enabling automation tools like Selenium to manipulate and retrieve information from specific elements.
# or
# locators are html address that identifies a web elements uniquely within a webpage.
# in the context of Selenium WebDriver, locators refer to the methods.
# to find elements using locators, we are using find_element and find_elements method.

# to use find_element and find_elements, we need to import By class from selenium webdriver.
# just mouse hover it will suggest from where to import.

# Note: The locators can be used with both find_element() and find_elements() methods, and you
# need to import By class from selenium.webdriver.common.by to use these locators.

# to find an element need to open web page and right-click and inspect.

# -----------------------------------------------------------------------------------------

# Locators can be divided into 2,
# Built-in locators: id, name, tag name, class name, link text, partial link text.
# Customized locator: css selector, xpath.

# -----------------------------------------------------------------------------------------

# Built-in locators

# 1.By ID:
# Locate an element using its unique id attribute.
# element = driver.find_element(By.ID, "element_id")

# 2. By Name:
# Locate an element using its name attribute.
# element = driver.find_element(By.NAME, "element_name")

# 3. By Class Name:
# Locate an element using its class name.
# element = driver.find_element(By.CLASS_NAME, "element_class")

# 4. By Tag Name:
# Locate an element using its HTML tag name.
# element = driver.find_element(By.TAG_NAME, "input")

# 5. By Link Text:
# Locate a link element by its visible text.
# element = driver.find_element(By.LINK_TEXT, "Click me")

# 6. By Partial Link Text:
# Locate a link element by a portion of its visible text.
# element = driver.find_element(By.PARTIAL_LINK_TEXT, "Click")

# -----------------------------------------------------------------------------------------

# Customized locator

# 7. By XPath:
# Locate an element using XPath expressions.
# element = driver.find_element(By.XPATH, "//input[@id='username']")

# 8. By CSS Selector:
# Locate an element using a CSS selector.
# element = driver.find_element(By.CSS_SELECTOR, "input#username")

# Remember to import By from selenium.webdriver.common.by in your code.

# -----------------------------------------------------------------------------------------

# After finding an element, you can perform various actions on it, such as sending keys, clicking,
# retrieving attributes, or checking its visibility.
# For example,

# Typing into an input field
# element.send_keys("Hello, Selenium!")

# Clicking a button
# element.click()

# Getting the text of an element
# text = element.text



###########################################################################################

