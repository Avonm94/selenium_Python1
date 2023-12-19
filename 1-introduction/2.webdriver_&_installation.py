# Selenium WebDriver Architecture
###########################################################################################

# WebDriver:
# WebDriver is a component of selenium / it is a module.
# It is an API and protocol that supports the automation of all the major browsers in the market.
# Its aim is to emulate a real user’s interaction with the browser as closely as possible.
# The selenium webdriver is the automation tool used to automate the test scripts written in selenium.

# -----------------------------------------------------------------------------------------

# API: Application Program Interface
# in software:
# Presentation Layer --> Application Layer --> Backend Layer,
# GUI/UI             -->  Business / Logic -->  Data Base,
# GUI Testing        -->   API Testing     -->   Database Testing,

# -----------------------------------------------------------------------------------------

# How WebDriver is an API:
# Application will run on browsers (Chrome, Edge, Firefox).(AUT: Application Under Test)
# To automate the testing, we will write automation code/scripts in the IDE. (PyCharm)
# to execute the script, we need one mediator i.e., Selenium-WebDriver API.
# IDE (Code) --> WebDriver (API) --> Application (UAT)

###########################################################################################

# Selenium Client Library

# Selenium Client Library or language bindings is a programming library that consists of commands in the
# form of an external jar file that are compatible with Selenium protocol/W3C Selenium protocol.

# The selenium client library can be divided into two groups:

# Web Driver protocol clients – They are thin wrappers around WebDriver protocol HTTP calls.
# Based on the user’s preferred programming language, the library can be downloaded from Selenium’s official repository.
# The library can later be added while creating a new project or a new Maven project in Eclipse or IntelliJ.

# WebDriver-based tools – These are higher-level libraries that allow us to work with WebDriver automation.
# Testing frameworks like Selenide, webdriver.io, or AI-powered Selenium extensions like Healenium come under
# this group. These tools rely on lower-level webdriver protocols to function efficiently.

# -----------------------------------------------------------------------------------------

# JSON Wire protocol:
# JSON is used in web services in REST and is a widely accepted method for communication between heterogeneous systems.
# The Selenium WebDriver uses JSON to communicate between client libraries and drivers.
# The JSON requests sent by the client are converted into HTTP requests for the server’s understanding and again
# converted back to JSON format while sending it to the client again. This data transfer process is serialization.
# By this method, the internal logic of the browser is not revealed, and the server can communicate with the client
# libraries, even if it is not aware of any programming language.

# -----------------------------------------------------------------------------------------

# Browser Drivers:
# Browser drivers act as a bridge between the Selenium libraries and the browsers.
# They help to run Selenium commands on the browser. Each of the browsers has separate drivers,
# which can be downloaded from Selenium’s official repository.

# -----------------------------------------------------------------------------------------

# Selenium API:
# Selenium API is a set of rules and regulations that the programs use to communicate with each other.
# APIs work as an interface between the program and aid in their interaction without any user knowledge.

# -----------------------------------------------------------------------------------------
# Selenium 3 Architecture:

# Selenium Client Library --> JSON Wire Protocol --> [Browser Drivers <-(W3C)-> Browsers]
# python,java,ruby        -->  over HTTP         -->   HTTP over HTTP Server

# W3C -> World Wide Web Consortium

# -----------------------------------------------------------------------------------------

# Selenium 4 Architecture:

# Selenium Client Library --> W3C --> [Browser Drivers <-(W3C)-> Browsers]
# python,java,ruby        --> W3C -->   HTTP over HTTP Server

# W3C -> World Wide Web Consortium

###########################################################################################

# Selenium Client Library:
# Supports various programming languages for Selenium WebDriver.
# Allows writing automation scripts in Java, Python, C#, Ruby, Javascript, etc.

# Browser Drivers:
# Separate drivers for each supported browser.
# Facilitate communication between Selenium scripts and browsers.
# Drivers include FirefoxDriver, ChromeDriver, etc.

# JSON Wire Protocol over HTTP:
# Lightweight JSON format used for data transfer.
# Facilitates communication between Selenium scripts and Browser Drivers in WebDriver architecture.

# Browsers:
# Receive commands and execute automation tasks in different browsers.
# Supported browsers include Chrome, Firefox, IE, Edge, Safari, Opera, etc.

###########################################################################################

# Installation

# Prerequisite:
# python latest version
# pycharm

# 1.download browser-specific drivers (check browser versions first):
# Chrome: https://chromedriver.chromium.org/downloads
# Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Firefox: https://github.com/mozilla/geckodriver/releases

# 2.once downloaded, extract them and keep then in one folder.

# 3.to set up selenium package (webdriver).
# in pycharm --> project setting: file--> project --> python interpreter --> search selenium. (I will go with this.)
# or using selenium command:pip install selenium

###########################################################################################
# for more information
# https://toolsqa.com/selenium-webdriver/selenium-webdriver-architecture/
# https://www.interviewbit.com/blog/selenium-architecture/
# https://artoftesting.com/selenium-webdriver-architecture
# https://www.simplilearn.com/tutorials/python-tutorial/selenium-with-python
# https://www.selenium.dev/documentation/webdriver/
###########################################################################################