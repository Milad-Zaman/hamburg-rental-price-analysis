import pandas as pd
import re
from datetime import datetime

# Define the function to convert the availability to hours
def convert_to_hours(value):
    fixed_date = datetime.strptime('24.06.2024', "%d.%m.%Y")
    value = str(value)  # Ensure value is always treated as a string
    
    try:
        if 'Minuten' in value:
            # Extract the number of minutes and convert to hours
            minutes = int(re.search(r'\d+', value).group())
            return minutes / 60
        elif 'Stunde' in value or 'Stunden' in value:
            # Extract the number of hours
            hours = int(re.search(r'\d+', value).group())
            return hours
        elif 'Tag' in value or 'Tage' in value:
            # Extract the number of days and convert to hours
            days = int(re.search(r'\d+', value).group())
            return days * 24
        else:
            # Handle dates by calculating difference from the fixed date
            try:
                date_format = "%d.%m.%Y"
                date = datetime.strptime(value, date_format)
                delta = fixed_date - date
                return delta.days * 24
            except ValueError:
                return None
    except Exception as e:
        print(f"Error processing value {value}: {e}")
        return None

# Load the original data
file_path = 'data_with_dummies.xlsx'
df = pd.read_excel(file_path)

# Apply the conversion to the 'Availability' column
df['Availability_in_hours'] = df['Availability'].apply(convert_to_hours)

# Save the results back to a new Excel file
output_file_path = 'final_data.xlsx'
df.to_excel(output_file_path, index=False)