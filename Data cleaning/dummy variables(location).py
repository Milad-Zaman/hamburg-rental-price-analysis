import pandas as pd

# Load the original Excel file
file_path = 'cleaned_data.xlsx'
df = pd.read_excel(file_path)

# Define lists of postal codes
near_to_uni = [20148, 20146, 20149, 20144, 20354, 20355, 22301, 20357, 22085]
near_to_airport = [22415, 22339, 22335, 22453, 22459, 22455, 22297, 22419, 22337, 22309]
near_to_hbf = [20099, 20095, 22087, 20354, 20097, 20537, 20535, 20355]
near_to_city_center = [20095, 20355, 20459, 20099, 20097, 20359, 20357, 20457, 20354]

# Create dummy variables
df['near_to_uni'] = df['Region'].apply(lambda x: 1 if x in near_to_uni else 0)
df['near_to_airport'] = df['Region'].apply(lambda x: 1 if x in near_to_airport else 0)
df['near_to_hbf'] = df['Region'].apply(lambda x: 1 if x in near_to_hbf else 0)
df['near_to_city_center'] = df['Region'].apply(lambda x: 1 if x in near_to_city_center else 0)

# Save the updated DataFrame to a new Excel file
output_file_path = 'data_with_dummies.xlsx'
df.to_excel(output_file_path, index=False)