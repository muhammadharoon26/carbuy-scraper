# CarBuyer Scraper🚗🔍

## Overview
The CarBuy Scraper is a Python-based web scraping tool that extracts car listings from OLX and PakWheels. It gathers car names, prices, and links, converts prices to PKR, and sorts the listings by ascending price.

## Features
- Scrapes car listings from OLX and PakWheels.
- Converts prices to PKR for consistent comparison.
- Sorts listings by ascending price.
Outputs the sorted car listings with their details.

## Prerequisites
- Python 3.12 
- Selenium 
- Chrome WebDrivers
<br/>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=black&style=for-the-badge" height="40" alt="selenium logo"  />
  <img width="12" />
  <img src="https://img.shields.io/badge/Google Chrome-4285F4?logo=googlechrome&logoColor=white&style=for-the-badge" height="40" alt="chrome logo"  />
</div>
<br/>

## Installation
1. **Clone the Repository**:
```
git clone https://github.com/muhammadharoon26/carbuy-scraper.git
```

2. **Install required Python packages**:
```
pip install selenium
```
3. **Download Chrome WebDriver**:

4. **Update the Chrome WebDriver path**:
Update the chrome_driver_path in the script with the path to your downloaded Chrome WebDriver executable.

## Usage:
1. **Update the chrome_driver_path in the CarScraper class initialization:**
```
scraper = CarScraper(r'path_to_your_chromedriver')
```

2. **Run the script:**
```
python main.py
```

## Example Output:
```
Enter make/model:
Toyota Corolla
Name: Toyota Corolla 2015
Price: 1800000.0
Link: https://www.olx.com.pk/item/toyota-corolla-2015-iid-123456789

Name: Toyota Corolla 2016
Price: 2000000.0
Link: https://www.pakwheels.com/used-cars/toyota-corolla-2016-iid-987654321
```

## Script Explination:

### CarScraper Class

- __init__: Initializes the scraper with the Chrome WebDriver path.
- **setup_driver**: Sets up the Chrome driver.
- **format_make_model:** Formats the make/model input to be URL-friendly.
- **convert_to_pkr:** Converts different price formats to PKR.
- **scrape_olx:** Scrapes car listings from OLX.
- **scrape_pakwheels:** Scrapes car listings from PakWheels.
- **scrape_listings:** Combines OLX and PakWheels listings, sorts them by price, and returns the sorted list.

## Main Execution
- Creates an instance of **CarScraper**.
- Prompts the user for a make/model.
- Scrapes and sorts the listings.
- Outputs the sorted listings.

## Notes
- Ensure you have the correct version of ChromeDriver that matches your installed Chrome browser.
- Modify the chrome_driver_path to the location where you saved ChromeDriver.
- This script uses class names and element structures specific to OLX and PakWheels as of the creation date. If the websites update their structures, the script may need adjustments

## License
[MIT LICENSE](LICENSE)