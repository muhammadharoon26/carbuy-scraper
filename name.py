from bs4 import BeautifulSoup

html_snippet = '<a href="/used-cars/honda-civic-2018-for-sale-in-karachi-8436125" class="car-name ad-detail-path" title="Honda Civic  2018 Oriel 1.8 i-VTEC CVT" current-index="0" target="_blank">' \
               '<h3 style="white-space: normal;">Honda Civic  2018 Oriel 1.8 i-VTEC CVT for Sale</h3>' \
               '<span class="auction-rating">9.2/10</span>' \
               '</a>'

# Parse the HTML snippet
soup = BeautifulSoup(html_snippet, 'html.parser')

# Extract the name and link
name = soup.h3.text.strip()
link = soup.a['href']

print("Name:", name)
print("Link:", link)
