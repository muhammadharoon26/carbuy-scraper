from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class CarScraper:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def setup_driver(self):
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service)

    @staticmethod
    def format_make_model(make_model):
        return make_model.replace(" ", "-")

    @staticmethod
    def convert_to_pkr(price_text):
        if 'Rs' in price_text:
            numerical_part = price_text.split()[1].replace(',', '')
            return float(numerical_part)
        elif 'lacs' in price_text:
            return float(price_text.split()[1]) * 100000
        elif 'crores' in price_text:
            return float(price_text.split()[1]) * 10000000
        else:
            parts = price_text.split()
            if 'PKR' in parts:
                amount_index = parts.index('PKR') + 1
                amount = parts[amount_index]
                if 'lacs' in parts:
                    return float(amount) * 100000
                elif 'crores' in parts:
                    return float(amount) * 10000000
        return None

    def scrape_olx(self, formatted_make_model):
        self.driver.get(f'https://www.olx.com.pk/cars_c84/q-{formatted_make_model}')
        price_elements = self.driver.find_elements(By.CLASS_NAME, '_95eae7db')
        name_elements = self.driver.find_elements(By.CLASS_NAME, 'a5112ca8')
        link_elements = self.driver.find_elements(By.CSS_SELECTOR, '.ee2b0479 a')
        
        listings = []
        for i in range(len(price_elements)):
            name = name_elements[i].text
            price_text = price_elements[i].text
            price = self.convert_to_pkr(price_text)
            link = link_elements[i].get_attribute('href') if i < len(link_elements) else 'N/A'
            listings.append({'name': name, 'price': price, 'link': link})
        
        return listings

    def scrape_pakwheels(self, make_model):
        self.driver.get(f'https://www.pakwheels.com/used-cars/search/-/?q={make_model}')
        price_elements = self.driver.find_elements(By.CLASS_NAME, 'price-details')
        name_elements = self.driver.find_elements(By.CLASS_NAME, 'car-name')
        
        listings = []
        for i in range(len(price_elements)):
            name = name_elements[i].find_element(By.TAG_NAME, 'h3').text
            price_text = price_elements[i].text
            price = self.convert_to_pkr(price_text)
            link = name_elements[i].get_attribute('href')
            listings.append({'name': name, 'price': price, 'link': link})
        
        return listings

    def scrape_listings(self, make_model):
        self.setup_driver()
        formatted_make_model = self.format_make_model(make_model)
        
        olx_listings = self.scrape_olx(formatted_make_model)
        pakwheels_listings = self.scrape_pakwheels(make_model)
        
        all_listings = olx_listings + pakwheels_listings
        sorted_listings = sorted(all_listings, key=lambda x: x['price'])
        
        self.driver.quit()
        return sorted_listings

if __name__ == '__main__':
    scraper = CarScraper(r'D:\Git-Hub\carbuy-scraper\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    make_model = input("Enter make/model:\n")
    sorted_listings = scraper.scrape_listings(make_model)
    
    for listing in sorted_listings:
        print(f"Name: {listing['name']}")
        print(f"Price: {listing['price']}")
        print(f"Link: {listing['link']}\n")