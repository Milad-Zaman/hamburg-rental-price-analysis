import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to extract data from a single ad URL
def extract_ad_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (e.g., 404)

        soup = BeautifulSoup(response.content, 'html.parser')

        # Initialize variables
        price = None
        size = None
        availability = None
        location = None
        apartment_size = None
        rooms = None

        # Extract price and size
        for fact in soup.find_all('div', class_='col-xs-6 text-center'):
            detail_label = fact.find('span', class_='key_fact_detail')
            if detail_label:
                detail_label_text = detail_label.text.strip()
                detail_value = fact.find('b', class_='key_fact_value').text.strip()

                if detail_label_text == "Gesamtmiete":
                    price = detail_value
                elif detail_label_text == "Größe" or detail_label_text == "Zimmergröße":
                    size = detail_value

        # Extract availability
        availability = soup.select_one('div.col-xs-6 > b.noprint').get_text(strip=True) if soup.select_one('div.col-xs-6 > b.noprint') else None

        # Extract location
        location = soup.select_one('div.col-xs-12 > a > span.section_panel_detail').get_text(strip=True) if soup.select_one('div.col-xs-12 > a > span.section_panel_detail') else None

        # Extract apartment size and rooms
        for detail in soup.select('div.col-xs-12 > ul.pl15.mb15 > li > span.section_panel_detail'):
            detail_text = detail.get_text(strip=True)
            if "Wohnungsgröße" in detail_text:
                apartment_size = detail_text.split(":")[1].strip()
            elif "er WG" in detail_text:
                rooms = detail_text

        return {
            "Price (Gesamtmiete)": price,
            "Size (Zimmergröße/Größe)": size,
            "Availability": availability,
            "Location": location,
            "Apartment Size (Wohnungsgröße)": apartment_size,
            "Rooms": rooms,
            "URL": url
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Base URL for Hamburg ads page
base_url = 'https://www.wg-gesucht.de/wg-zimmer-und-1-zimmer-wohnungen-und-wohnungen-in-Hamburg.55.0+1+2.1.22.html?offer_filter=1&city_id=55&sort_order=0&noDeact=1&categories%5B%5D=0&categories%5B%5D=1&categories%5B%5D=2&pagination=1&pu=#page-24'

try:
    # Send a GET request to the base URL
    response = requests.get(base_url)
    response.raise_for_status()  # Raise an exception for bad responses (e.g., 404)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all ad links and filter out commercial ads
    ad_links = []
    for ad in soup.find_all('a', class_='detailansicht'):
        if not ad.find('img', class_='lazy-advert'):
            ad_url = "https://www.wg-gesucht.de" + ad['href']
            ad_links.append(ad_url)

    # Extract data from each ad
    results = []
    for link in ad_links:
        ad_data = extract_ad_data(link)
        if ad_data:
            results.append(ad_data)

    # Convert data to DataFrame
    df = pd.DataFrame(results)

    # Save DataFrame to Excel
    excel_file = 'wg_gesucht_ads.xlsx'
    df.to_excel(excel_file, index=False, engine='xlsxwriter')

    print(f"Data saved to {excel_file}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching base URL {base_url}: {e}")