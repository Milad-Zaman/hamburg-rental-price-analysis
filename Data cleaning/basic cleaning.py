import pandas as pd
import re

def clean_data(input_file, output_file):
    # Load the file and remove duplicate rows
    df = pd.read_excel(input_file)
    df = df.drop_duplicates()

    # Remove 'm²' from specified columns
    df['Size (Zimmergröße/Größe)'] = df['Size (Zimmergröße/Größe)'].str.replace('m²', '').astype(str).str.strip()
    df['Apartment Size (Wohnungsgröße)'] = df['Apartment Size (Wohnungsgröße)'].str.replace('m²', '').astype(str).str.strip()

    # Function to extract the last 5 digits from any number found in the string
    def extract_region(location):
        numbers = re.findall(r'\d+', location)
        for number in numbers:
            if len(number) == 5:
                return number
            elif len(number) > 5:
                return number[-5:]
        return None

    # Apply the function to the 'Location' column to create the 'Region' column
    df['Region'] = df['Location'].apply(extract_region)

    # Extract the number at the beginning of each cell in the 'Rooms' column
    df['Rooms_Number'] = df['Rooms'].str.extract(r'(\d+)')

    # Remove '€' from the 'Price (Gesamtmiete)' column
    df['Price (Gesamtmiete)'] = df['Price (Gesamtmiete)'].str.replace('€', '').astype(str).str.strip()

    # Save the cleaned DataFrame to a new Excel file
    df.to_excel(output_file, index=False)

# Specify the input and output file paths
input_file = 'wg_gesucht_ads.xlsx'
output_file = 'cleaned_data.xlsx'

# Run the data cleaning function
clean_data(input_file, output_file)