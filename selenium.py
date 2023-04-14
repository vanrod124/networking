from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

# Set the URL of the Google Form
form_url = "YOUR_FORM_URL_HERE"

# Create a function to generate a random name
def generate_random_name():
    first_names = ["Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "James", "Isabella", "Oliver"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    random_name = random.choice(first_names) + ' ' + random.choice(last_names)
    return random_name

# Create a function to generate a random age between 18 and 100
def generate_random_age():
    return str(random.randint(18, 100))

# Set up the Selenium driver
driver = webdriver.Chrome()
driver.get(form_url)

# Find the form fields for name and age
name_field = driver.find_element_by_xpath("//input[@aria-label='Name']")
age_field = driver.find_element_by_xpath("//input[@aria-label='Age']")

# Fill in the form fields with random values
name_field.send_keys(generate_random_name())
age_field.send_keys(generate_random_age())

# Submit the form
submit_button = driver.find_element_by_xpath("//span[contains(text(), 'Submit')]")
submit_button.click()

# Close the Selenium driver
driver.close()
