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

# Function to convert price to PKR
def convert_to_pkr(price_text):
    # print("Price Text:", price_text)
    # Check if 'Rs' is present in the price text
    if 'Rs' in price_text:
        # Split the price text and extract the numerical part
        numerical_part = price_text.split()[1]
        # Remove commas from the numerical part and convert it to float
        numerical_part = numerical_part.replace(',', '')
        return float(numerical_part)  # No conversion needed
    elif 'lacs' in price_text:
        return float(price_text.split()[1]) * 100000  # Convert lacs to PKR
    elif 'crores' in price_text:
        return float(price_text.split()[1]) * 10000000  # Convert crores to PKR
    else:
        # Handle other representations, like 'PKR 25.25 lacs'
        parts = price_text.split()
        if 'PKR' in parts:
            amount_index = parts.index('PKR') + 1
            amount = parts[amount_index]
            if 'lacs' in parts:
                return float(amount) * 100000  # Convert lacs to PKR
            elif 'crores' in parts:
                return float(amount) * 10000000  # Convert crores to PKR
    return None




# Get user input and format it
make_model = input('Please enter make/model: ')
formatted_make_model = format_make_model(make_model)

# Navigate to the OLX website
driver.get('https://www.olx.com.pk/cars_c84/q-' + formatted_make_model)

# Locate all price elements using their class name
price_elements_olx = driver.find_elements(By.CLASS_NAME, '_95eae7db')

# Locate all name elements using their class name
name_elements_olx = driver.find_elements(By.CLASS_NAME, 'a5112ca8')

# Locate all link elements within class 'ee2b0479'
link_elements_olx = driver.find_elements(By.CSS_SELECTOR, '.ee2b0479 a')

# Extract the text of the price elements, names, and links for all OLX listings
olx_listings = []
for i in range(len(price_elements_olx)):
    name = name_elements_olx[i].text
    price_text = price_elements_olx[i].text
    # Convert price to PKR
    price = convert_to_pkr(price_text)
    
    # Get the href link from the anchor element within class 'ee2b0479'
    link = link_elements_olx[i].get_attribute('href') if i < len(link_elements_olx) else 'N/A'
    
    olx_listings.append({'name': name, 'price': price, 'link': link})

# Navigate to the PakWheels website
driver.get('https://www.pakwheels.com/used-cars/search/-/?q='+ make_model)

# Locate all price elements using their class name
price_elements_pw = driver.find_elements(By.CLASS_NAME, 'price-details')

# Locate all name elements using their class name
name_elements_pw = driver.find_elements(By.CLASS_NAME, 'car-name')

# Locate all links
links_pw = driver.find_elements(By.CLASS_NAME, 'car-name')

# Extract the text of the price elements, names, and links for all PakWheels listings
pw_listings = []
for i in range(len(price_elements_pw)):
    name = name_elements_pw[i].find_element(By.TAG_NAME, 'h3').text
    price_text = price_elements_pw[i].text
    # Convert price to PKR
    price = convert_to_pkr(price_text)
    link = links_pw[i].get_attribute('href')
    pw_listings.append({'name': name, 'price': price, 'link': link})

# Close the browser
driver.quit()

# Combine listings from both websites
all_listings = olx_listings + pw_listings

# Sort the listings by ascending price
sorted_listings = sorted(all_listings, key=lambda x: x['price'])

# Print the sorted listings
for listing in sorted_listings:
    print(f"Name: {listing['name']}")
    print(f"Price: {listing['price']}")
    print(f"Link: {listing['link']}")
    print()  # Add an empty line for spacing
