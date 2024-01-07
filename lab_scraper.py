import requests
from bs4 import BeautifulSoup
import pandas as pd

def lab_scraper(url):
    # Send an HTTP request to the specified URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the relevant data elements
    lab_name_element = soup.find('span', {'class': 'lb-name'})
    mrp_element = soup.find('span', {'class': 'price'})
    discounted_price_element = soup.find('span', {'class': 'discounted-price'})
    tests_included_element = soup.find('span', {'class': 'tests-included'})
    address_element = soup.find('span', {'class': 'address'})

    # Extract the lab name, MRP, discounted price, tests included, and address
    lab_name = lab_name_element.text.strip() if lab_name_element else ""
    mrp = mrp_element.text.strip() if mrp_element else ""
    discounted_price = discounted_price_element.text.strip() if discounted_price_element else ""
    tests_included = tests_included_element.text.strip() if tests_included_element else ""
    address = address_element.text.strip() if address_element else ""

    # Create a pandas DataFrame with the extracted data
    data = {'Lab Name': [lab_name],
            'MRP': [mrp],
            'Discounted Price': [discounted_price],
            'Tests Included': [tests_included],
            'Address': [address]}

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)

    # Write the DataFrame to a CSV file
    df.to_csv('lab_data.csv', index=False)

    return lab_name, mrp, discounted_price, tests_included, address

url="https://www.labuncle.com/packages/health-champion-radiology-package-1677"
output = lab_scraper(url)
print(output)