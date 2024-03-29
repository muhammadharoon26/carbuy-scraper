from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up the Chrome web driver with the correct path to chromedriver executable
chrome_driver_path = r'D:\Git-Hub\carbuy-scraper\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# Set up the service
service = Service(chrome_driver_path)

# Initialize the Chrome driver with the service
driver = webdriver.Chrome(service=service)

# Function to format make/model to be URL-friendly
def format_make_model(make_model):
    return make_model.replace(" ", "-")

# Get user input and format it
make_model = input('Please enter make/model: ')
formatted_make_model = format_make_model(make_model)

# Navigate to the website
driver.get('https://www.olx.com.pk/cars_c84/q-' + formatted_make_model)

# Locate all price elements using their class name
price_elements = driver.find_elements(By.CLASS_NAME, '_95eae7db')

# Locate all name elements using their class name
name_elements = driver.find_elements(By.CLASS_NAME, 'a5112ca8')

# Locate all link elements within class 'ee2b0479'
link_elements = driver.find_elements(By.CSS_SELECTOR, '.ee2b0479 a')

# Extract the text of the price elements, names, and links for all listings
for i in range(len(price_elements)):
    name = name_elements[i].text
    price = price_elements[i].text
    
    # Get the href link from the anchor element within class 'ee2b0479'
    link = link_elements[i].get_attribute('href') if i < len(link_elements) else 'N/A'
    
    print(f"Name: {name}")
    print(f"Price: {price}")
    print(f"Link: {link}")
    print()  # Add an empty line for spacing

# Close the browser
driver.quit()