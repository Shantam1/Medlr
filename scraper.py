import requests
from bs4 import BeautifulSoup
import csv

# Function to extract data from Pharmeasy
def extract_data_from_pharmeasy(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    medicines = soup.find_all('td', class_='product-name')
    data = []
    for medicine in medicines:
        name = medicine.find('span', class_='product-name-text').text.strip()
        mrp = medicine.find('span', class_='product-price').text.strip()
        discounted_price = medicine.find('span', class_='product-discount-price').text.strip()
        quantity = medicine.find('span', class_='product-stock').text.strip()
        salts = medicine.find('span', class_='product-ingredients').text.strip()
        manufacturer = medicine.find('span', class_='product-info').text.strip()
        url = medicine.get('href')
        data.append([name, mrp, discounted_price, quantity, salts, manufacturer, url])
    return data

# Function to extract data from Netmeds
def extract_data_from_netmeds(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    medicines = soup.find_all('td', class_='product-name')
    data = []
    for medicine in medicines:
        name = medicine.find('h2').text.strip()
        mrp = medicine.find('span', class_='price-strike').text.strip()
        discounted_price = medicine.find('span', class_='price-actual').text.strip()
        quantity = medicine.find('span', class_='product-stock').text.strip()
        salts = medicine.find('span', class_='product-composition').text.strip()
        manufacturer = medicine.find('span', class_='product-info').text.strip()
        url = medicine.get('href')
        data.append([name, mrp, discounted_price, quantity, salts, manufacturer, url])
    return data

# List of URLs
pharmeasy_urls = ['https://pharmeasy.in/online-medicine-order/ferimuna-xt-susp-200ml-166294']  # Replace with your Pharmeasy URLs
netmeds_urls = ['https://www.netmeds.com/prescriptions/mednocal-tablet-10s']  # Replace with your Netmeds URLs

# Extract data and save it to a CSV file
def save_data_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'MRP', 'Discounted Price', 'Quantity', 'Salts', 'Manufacturer', 'URL'])
        for row in data:
            writer.writerow(row)

# Run the code for Pharmeasy and Netmeds
data_pharmeasy = extract_data_from_pharmeasy('https://pharmeasy.in/online-medicine-order/ferimuna-xt-susp-200ml-166294')
data_netmeds = extract_data_from_netmeds('https://www.netmeds.com/prescriptions/mednocal-tablet-10s')

# Save data to CSV files
save_data_to_csv(data_pharmeasy, 'C:\\Users\\Lenovo\\Downloads\\pharmeasy_data.csv')
save_data_to_csv(data_netmeds, 'C:\\Users\\Lenovo\\Downloads\\netmeds_data.csv')
