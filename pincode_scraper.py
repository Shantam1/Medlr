import requests
from bs4 import BeautifulSoup

def scrape_medicine_availability(pincode, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Locate the medicine availability and delivery date elements
    medicine_availability = soup.select_one('span.availability-status')
    delivery_date = soup.select_one('span.delivery-date')

    # Extract the medicine availability and delivery date
    if medicine_availability:
        medicine_availability = medicine_availability.text.strip()
    else:
        medicine_availability = "Not available"

    if delivery_date:
        delivery_date = delivery_date.text.strip()
    else:
        delivery_date = "Not available"

    return medicine_availability, delivery_date, url
# Example usage
pincode = "225001"
url="https://www.kauverymeds.com/product/atrox-50mg-tablet-dt-127064"
availability, delivery_date, url = scrape_medicine_availability(pincode, url)
print(f"Medicine availability: {availability}")
print(f"Delivery date: {delivery_date}")