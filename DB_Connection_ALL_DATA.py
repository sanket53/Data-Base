import pyodbc
import pandas as pd

server = 'tcp:mcruebs04.isad.isadroot.ex.ac.uk'
database = 'BEMM459_GroupB'
username = 'GroupB'
password = 'XyaX882+Mk'

# Driver for own machine.  Comment out when on windows machine.
#serverstring = 'DRIVER={/opt/homebrew/cellar/msodbcsql18/18.1.2.1/lib/libmsodbcsql.18.dylib};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';TrustServerCertificate=yes;Encrypt=no;'

# print(serverstring)

#cnxn = pyodbc.connect(serverstring)

cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';TrustServerCertificate=yes;Encrypt=no;')

cursor = cnxn.cursor()

# This part you should only run once.  The reason being that the first time you run it, 
# the table is created because it does not exist.  If you run it again, the table DOES
# exist and so it will cause an error.  You can check to see if the table is there 
# using the panel for the SQL server and clicking refresh.
csv_file = 'C:\\Users\hp\Desktop\database\grocery_random_data.csv'
table_name = 'ALL_DATA'


tsql = '''CREATE TABLE ALL_DATA (
  product_name VARCHAR(255),
  category_id VARCHAR(255),
  category_name VARCHAR(255),
  supermarket_name VARCHAR(255),
  price_in_pounds  VARCHAR(255),
  unit VARCHAR(255),
  available VARCHAR(255),
  brand VARCHAR(255),
  product_id VARCHAR(255),
  supermarket_id VARCHAR(255),
  image_url VARCHAR(255),
  description VARCHAR(255),
  dietary_restrictions VARCHAR(255),
  nutritional_information VARCHAR(255),
  no_of_ingredients VARCHAR(255),
  country_of_origin VARCHAR(255),
  is_seasonal VARCHAR(255),
  promotions VARCHAR(255),
  stock_level VARCHAR(255),
  delivery_options VARCHAR(255),
  delivery_lead_time VARCHAR(255),
  minimum_order_quantity VARCHAR(255),
  is_click_and_collect_available VARCHAR(255),
  Rating VARCHAR(255),
  number_of_reviews VARCHAR(255),
  is_popular VARCHAR(255),
  is_new VARCHAR(255),
  customer_tags VARCHAR(255),
  best_before_date VARCHAR(255),
  disposal_instructions VARCHAR(255),
  awards_won VARCHAR(255),
  allergens VARCHAR(255),
  is_organic VARCHAR(255),
  is_vegan VARCHAR(255),
  standard_delivery VARCHAR(255),
  fast_delivery VARCHAR(255),
  order_date VARCHAR(255),
  customer_id VARCHAR(255),
  customer_name VARCHAR(255),
  customer_email VARCHAR(255),
  customer_number VARCHAR(255),
  customer_address VARCHAR(255),
  order_id VARCHAR(255)
)'''
print('Creating ALL_DATA table \n')
# Make the SQL run on the server.
cursor.execute(tsql)
try:
  df = pd.read_csv(csv_file , encoding="latin-1")
except FileNotFoundError:
  print(255)(f"Error: CSV file '{csv_file}' not found.")
  exit()

# Get column names from DataFrame
column_names = ', '.join(df.columns.tolist())

# Prepare insert statement with placeholders for values
insert_stmt = f"INSERT INTO {table_name} ({column_names}) VALUES ({','.join(['?'] * len(df.columns))})"

# Iterate through DataFrame rows and insert data
for row in df.itertuples():
  # Convert row values to a list and escape single quotes
  values = [str(v).replace("'", "''") for v in row[1:]]
  cursor.execute(insert_stmt, values)

print(f"Data from '{csv_file}' inserted into table '{table_name}' successfully.")


# Use commit to get it to finish 
cnxn.commit()

# Now call all the data from the new table

tableData = 'SELECT * FROM ALL_DATA;'

print('printing first row \n')

with cursor.execute(tableData):
    row = cursor.fetchone()
    while row:
        print(str(row[0]) + ' '+str(row[1]))
        row = cursor.fetchone()