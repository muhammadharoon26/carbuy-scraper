from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Chrome web driver (make sure you have chromedriver installed)
chrome_driver_path = 'D:\Git-Hub\carbuy-scraper\chromedriver_win32'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Navigate to the website
driver.get('https://www.pakwheels.com/used-cars/search/-/?q=cultus')

# Locate the price element using its class name
price_element = driver.find_element(By.CLASS_NAME, 'price-details')

# Extract the text of the price element
price = price_element.text

# Print the extracted price
print("The price is:", price)

# Close the browser
driver.quit()
