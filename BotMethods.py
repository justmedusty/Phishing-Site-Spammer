# Used to import the webdriver from selenium
from selenium import webdriver

# Get the path of chromedriver which you have install
path = "C:\\Users\\Dusty\\Downloads\\chromedriver.exe"
# giving the path of chromedriver to selenium webdriver
driver = webdriver.Chrome(path)


def startBot(url):
    # opening the website  in chrome.
    driver.get(url)


def inputData(username, password):
    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element_by_name(
        "email").send_keys(username)

    # find the password by inspecting on password input
    driver.find_element_by_name(
        "password").send_keys(password)
    driver.refresh()

    # click on submit
    # driver.find_element_by_css_selector(
    #   "next-btn").click()
