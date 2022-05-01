# Used to import the webdriver from selenium
from selenium import webdriver
import os

# Get the path of chromedriver which you have install

def startBot(username, first_name, email, password, url):
	path = "C:\\Users\\Asus  Eb167TS\\Downloads\\chromedriver"
	
	# giving the path of chromedriver to selenium webdriver
	driver = webdriver.Chrome(path)
	
	# opening the website in chrome.
	driver.get(url)
	
	# find the id or name or class of
	# username by inspecting on username input
	driver.find_element_by_name(
		"username").send_keys(username)
	
	# find the password by inspecting on password input
	driver.find_element_by_name(
		"password").send_keys(password)

	driver.find_element_by_name(
		"fname").send_keys(first_name)

	driver.find_element_by_name(
		"email").send_keys(email)
	
	# click on submit
	driver.find_element_by_css_selector(
		"btn-success").click()


# Driver Code
# Enter below your login credentials
username = "bot1"
first_name = "Bot Python"
email = "python@Python.com"
password = "12345678"

# URL of the login page of site
# which you want to automate login.
url = "http://127.0.0.1:8000/register/"

# Call the function
startBot(username, first_name,email, password, url)
