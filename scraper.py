import requests
from bs4 import BeautifulSoup
import csv

url = "http://quotes.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    scraped_data = []

    for quote_div in quotes:
        text = quote_div.find('span', class_='text').get_text(strip=True)
        author = quote_div.find('small', class_='author').get_text(strip=True)
        scraped_data.append({'text': text, 'author': author})

    with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['text', 'author']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(scraped_data)

    print("Success! Data has been scraped and saved to quotes.csv.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
except Exception as e:
    print(f"An error occurred: {e}")