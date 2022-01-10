# Used to import the webdriver from selenium
from selenium import webdriver

# Get the path of chromedriver which you have install
from selenium.webdriver.chrome.options import Options

path = "C:\\Users\\Dusty\\Downloads\\chromedriver.exe"
# giving the path of chromedriver to selenium webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")
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
