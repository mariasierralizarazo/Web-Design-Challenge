import pandas as pd 
import os
# Defining file path 
file_path = os.path.join('Resources', 'cities.csv')
# Reading CSV file with Pandas for DataFrame generation
cities_df = pd.read_csv(file_path,delimiter=',')
# Generate HTML table code with Pandas for posting in the data.html file  
html_table = cities_df.to_html(header = True , index = False)
