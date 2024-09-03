from selenium import webdriver
from selenium.webdriver.common.by import By


class PakWheelScraper:
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

        self.elements_locater()
        self.extract_text()

    def elements_locater(self):
        """This funcion will take input and then locate the relevent HTML element from the pakwheel website"""
        # variables
        self.make_model = input("Please enter make/model: ")

        # Navigate to the website
        self.driver.get(
            "https://www.pakwheels.com/used-cars/search/-/?q=" + self.make_model
        )

        # Locate all price
        self.price_elements = self.driver.find_elements(By.CLASS_NAME, "price-details")

        # Locate all name
        self.name_elements = self.driver.find_elements(By.CLASS_NAME, "car-name")

        # Locate all links
        self.links = self.driver.find_elements(By.CLASS_NAME, "car-name")

    def extract_text(self):
        """This funcion Extract the text of the price elements, names, and links for all listings"""

        for i in range(len(self.price_elements)):
            name = self.name_elements[i].find_element(By.TAG_NAME, "h3").text
            price = self.price_elements[i].text
            link = self.links[i].get_attribute("href")
            print(f"Name: {name}, ")
            print(f"Price: {price}, ")
            print(f"Link: {link}")
            print()  # Add an empty line for spacing


pakwheel = PakWheelScraper()
