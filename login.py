# Used to import the webdriver from selenium
from selenium import webdriver
from LoginRandomizer import createPassword, createLogin
import os


# Get the path of chromedriver which you have install

def startBot(username, password, url):
    path = "C:\\Users\\Dusty\\Downloads\\chromedriver.exe"

    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(path)

    # opening the website  in chrome.
    driver.get(url)

    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element_by_name(
        "email").send_keys(username)

    # find the password by inspecting on password input
    driver.find_element_by_name(
        "password").send_keys(password)

    # click on submit
    # driver.find_element_by_css_selector(
    #   "next-btn").click()
    driver.close()
    driver.quit()


# Driver Code
# Enter below your login credentials
username = createLogin()
password = createPassword()

# URL of the login page of site
# which you want to automate login.
# PHISHING WEBSITE
url = "some phishing site"

# Call the function
startBot(username, password, url)
