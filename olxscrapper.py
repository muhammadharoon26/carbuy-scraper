from selenium import webdriver
from selenium.webdriver.common.by import By


class OLXScrapper:
    def __init__(self) -> None:
        self.user_input_car_model()

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

        self.elements_locater()
        self.data_extractor()

    def user_input_car_model(self) -> None:
        """This fuction would ask for the make model and the scrape the relevent data from the OLX"""

        self.make_model = input("Please enter make/model: ").replace(" ", "-")

    def elements_locater(self) -> None:
        """This function would located the relevent HTML tags"""

        self.driver.get("https://www.olx.com.pk/cars_c84/q-" + self.make_model)
        # Locate all price
        self.price_elements = self.driver.find_elements(By.CLASS_NAME, "_95eae7db")

        # Locate all name elements
        self.name_elements = self.driver.find_elements(By.CLASS_NAME, "a5112ca8")

        # Locate all link elements
        self.link_elements = self.driver.find_elements(By.CSS_SELECTOR, ".ee2b0479 a")

    def data_extractor(self) -> None:
        """Extract the text of the price elements, names, and links for all listings"""

        for i in range(len(self.price_elements)):
            self.name = self.name_elements[i].text
            self.price = self.price_elements[i].text

            # Get the href link from the anchor element within class 'ee2b0479'
            link = (
                self.link_elements[i].get_attribute("href")
                if i < len(self.link_elements)
                else "N/A"
            )

            print(f"Name: {self.name}")
            print(f"Price: {self.price}")
            print(f"Link: {link}")
            print()  # Add an empty line for spacing


olx = OLXScrapper()
