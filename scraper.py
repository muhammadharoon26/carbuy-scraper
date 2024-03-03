from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Chrome web driver with the correct path to chromedriver executable
chrome_driver_path = r'D:\Git-Hub\carbuy-scraper\chromedriver-win64\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Navigate to the website
driver.get('https://www.pakwheels.com/used-cars/search/-/?q=accord')

# Locate all price elements using their class name
price_elements = driver.find_elements(By.CLASS_NAME, 'price-details')

# Locate all name elements using their class name
name_elements = driver.find_elements(By.CLASS_NAME, 'car-name')

# Locate all links
links = driver.find_elements(By.CLASS_NAME, 'car-name')

# Extract the text of the price elements, names, and links for the first 10 listings
for i in range(20):
    name = name_elements[i].find_element(By.TAG_NAME, 'h3').text
    price = price_elements[i].text
    link = links[i].get_attribute('href')
    print(f"Name: {name}, ")
    print(f"Price: {price}, ")
    print(f"Link: {link}")
    print()  # Add an empty line for spacing

# Close the browser
driver.quit()