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

#Minimum Product Price in specific supermarket
tableData15 = 'SELECT min(Product.price_in_pounds) as price,Product.product_name,Supermarket.supermarket_name, Category.category_name from Retail.Product Left Join Market.Supermarket on Product.supermarket_id = Supermarket.supermarket_id Left Join Retail.Category on Product.category_id = Category.category_id where product_name=\'Eggs\' GROUP BY Product.product_name,Supermarket.supermarket_name,Category.category_name'
cursor.execute(tableData15)
print("\n Minimum Product Price in specific supermarket")
with cursor.execute(tableData15):
    columns = [col[0] for col in cursor.description]
    print(" ".join(columns))
    for row in cursor.fetchall():
        print(" ".join(str(cell) for cell in row))

#Minimum Product Price
tableData35 = 'SELECT Top 1 Product.price_in_pounds as price,Product.product_name ,Supermarket.supermarket_name, Category.category_name from Retail.Product Left Join Market.Supermarket on Product.supermarket_id = Supermarket.supermarket_id Left Join Retail.Category on Product.category_id = Category.category_id where product_name=\'Eggs\' order by Product.price_in_pounds'
cursor.execute(tableData35)
print("\n Minimum Product Price")
with cursor.execute(tableData35):
    columns = [col[0] for col in cursor.description]
    print(" ".join(columns))
    for row in cursor.fetchall():
        print(" ".join(str(cell) for cell in row))

#Delivery date from date of order
tableData25 = 'SELECT Top 10 order_id, CONVERT(CHAR(10), order_date,103) AS order_date, CONVERT(CHAR(10), DATEADD(day,standard_delivery, CONVERT(DATE, order_date)),103) AS Standard_delivery_date, CONVERT(CHAR(10), DATEADD(day,fast_delivery, CONVERT(DATE, order_date)), 103) AS Fast_delivery_date FROM Sales.Orders;'
cursor.execute(tableData25)
print("\n Calculated Delivery date from date of order")
with cursor.execute(tableData25):
    columns = [col[0] for col in cursor.description]
    print(" ".join(columns))
    for row in cursor.fetchall():
        print(" ".join(str(cell) for cell in row))

#Creation of View for Cheapest Product Tomato with delivery date from date of order
tableData45 = 'CREATE VIEW Cheapest_Product_Tomato AS select Top 1 Product.price_in_pounds as price,Product.product_name , Orders.order_id,Supermarket.supermarket_name, CONVERT(CHAR(10), Orders.order_date,103) AS order_date, CONVERT(CHAR(10), DATEADD(day, Orders.standard_delivery, CONVERT(DATE, order_date)),103) AS Standard_delivery_date, CONVERT(CHAR(10), DATEADD(day, Orders.fast_delivery, CONVERT(DATE, order_date)), 103) AS Fast_delivery_date FROM Sales.Orders Left Join Retail.Product ON Product.order_id = Orders.order_id Left Join Market.Supermarket ON Product.supermarket_id = Supermarket.supermarket_id where Product.product_name = \'Tomatoes\' order by Product.price_in_pounds'
tableData78 = 'select * from dbo.Cheapest_Product_Tomato'
tableData23 = 'drop view Cheapest_Product_Tomato;'
cursor.execute(tableData23)
cursor.execute(tableData45)
cnxn.commit()
print("\n View for Cheapest Product Tomato with delivery date successfully created")
print("\n Fetching Data from View")
with cursor.execute(tableData78):
    columns = [col[0] for col in cursor.description]
    print(" ".join(columns))
    for row in cursor.fetchall():
        print(" ".join(str(cell) for cell in row))


# Insert Record into Table
tableData = 'INSERT INTO Retail.Product (product_id, product_name,supermarket_id,category_id, order_id, price_in_pounds, unit, available, brand, description, dietary_restrictions, nutritional_information,no_of_ingredients, country_of_origin, is_seasonal, promotions, stock_level, is_popular, is_new,best_before_date, disposal_instructions, allergens) VALUES (\'M12345\', \'Apple\', 4, 101, \'O73\', 20.3, \'kg\', \'Yes\', \'Brand D\', \'Fresh organic apples\', \'vegan\', \'{"Calories": 52}\', 1, \'UK\', \'True\', \'None\', 100, \'True\', \'True\', \'2024-03-15\', \'Dispose of in compost\', \'nuts\')'
cursor.execute(tableData)
cnxn.commit()
# Fetch and print row after insertion
print("\n Row Inserted:product_id=M12345")
tableData2 = 'select Product.product_id,Product.product_name,Product.promotions,Product.best_before_date from Retail.Product where Product.product_id = \'M12345\''
with cursor.execute(tableData2):
    columns = [col[0] for col in cursor.description]
    print(" ".join(columns))
    for row in cursor.fetchall():
        print(" ".join(str(cell) for cell in row))

# Fetch and print row after updating
tabledata3 = 'UPDATE Retail.Product SET promotions = \'Buy 1 Get 1 Free\' WHERE product_id = \'M12345\''
cursor.execute(tabledata3)
cnxn.commit()
print("\n Row Update:product_id=M12345 Updated Promotions")
with cursor.execute(tableData2):
    columns = [col[0] for col in cursor.description]
    print(" ".join(columns))
    for row in cursor.fetchall():
        print(" ".join(str(cell) for cell in row))

# Fetch and print row after deletion
tabledata4 = 'delete from Retail.Product WHERE Product.best_before_date < \'2024-03-16\';'
cursor.execute(tabledata4)
cnxn.commit()
print("\n Row Deleted:product_id=M12345 Not Found")
with cursor.execute(tableData2):
    columns = [col[0] for col in cursor.description]
    print(" ".join(columns))
    for row in cursor.fetchall():
        print(" ".join(str(cell) for cell in row))