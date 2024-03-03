from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Chrome web driver with the correct path to chromedriver executable
chrome_driver_path = r'D:\Git-Hub\carbuy-scraper\chromedriver-win64\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Navigate to the website
driver.get('https://www.pakwheels.com/used-cars/search/-/?q=civic')

# Locate all price elements using their class name
price_elements = driver.find_elements(By.CLASS_NAME, 'price-details')

# Extract the text of the price elements for the first 10 listings
for i in range(10):
    price = price_elements[i].text
    print(f"Price of listing {i+1}: {price}")

# Close the browser
driver.quit()