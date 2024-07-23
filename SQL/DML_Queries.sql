"Business Scenario"
"Minimum Product Price in specific supermarket"
SELECT min(Product.price_in_pounds) as price,Product.product_name,Supermarket.supermarket_name, Category.category_name from Retail.Product Left Join Market.Supermarket on Product.supermarket_id = Supermarket.supermarket_id Left Join Retail.Category on Product.category_id = Category.category_id where product_name='Eggs' GROUP BY Product.product_name,Supermarket.supermarket_name,Category.category_name;

"Minimum Product Price"
SELECT Top 1 Product.price_in_pounds as price,Product.product_name ,Supermarket.supermarket_name, Category.category_name from Retail.Product Left Join Market.Supermarket on Product.supermarket_id = Supermarket.supermarket_id Left Join Retail.Category on Product.category_id = Category.category_id where product_name='Eggs' order by Product.price_in_pounds;

SELECT Product.price_in_pounds as price, Product.product_name,Supermarket.supermarket_name FROM Retail.Product LEFT JOIN Market.Supermarket ON Product.supermarket_id = Supermarket.supermarket_id WHERE Product.product_name='Eggs' ORDER BY Product.price_in_pounds ASC LIMIT 1;

"Supermarket with great rating"
select supermarket_name,rating from Market.Supermarket where rating between 4.5 and 5;

"delivery date from date of order"
SELECT order_id,
  CONVERT(CHAR(10), order_date,103) AS order_date,
  CONVERT(CHAR(10), DATEADD(day, standard_delivery, CONVERT(DATE, order_date)),103) AS Standard_delivery_date,
  CONVERT(CHAR(10), DATEADD(day, fast_delivery, CONVERT(DATE, order_date)), 103) AS Fast_delivery_date
FROM Sales.Orders;


"View for Cheapest Product Tomato with delivery date from date of order"
CREATE VIEW Cheapest_Product_Tomato AS
select Top 1 Product.price_in_pounds as price,Product.product_name , Orders.order_id,Supermarket.supermarket_name,
  CONVERT(CHAR(10), Orders.order_date,103) AS order_date,
  CONVERT(CHAR(10), DATEADD(day, Orders.standard_delivery, CONVERT(DATE, order_date)),103) AS Standard_delivery_date,
  CONVERT(CHAR(10), DATEADD(day, Orders.fast_delivery, CONVERT(DATE, order_date)), 103) AS Fast_delivery_date FROM Sales.Orders Left Join Retail.Product ON Product.order_id = Orders.order_id Left Join Market.Supermarket ON Product.supermarket_id = Supermarket.supermarket_id where Product.product_name = 'Tomatoes' order by Product.price_in_pounds;


"Insert/Update/Delete of a Product based on Best Before Date"
select product_id,product_name,promotions,best_before_date from Retail.Product where product_id = 'M12345'

INSERT INTO Retail.Product (product_id, product_name,supermarket_id,category_id, order_id, price_in_pounds, unit, available, brand, description, dietary_restrictions, nutritional_information, no_of_ingredients, country_of_origin, is_seasonal, promotions, stock_level, is_popular, is_new, best_before_date, disposal_instructions, allergens) 
VALUES ('M12345', 'Apple', 4, 101, 'O73', 20.3, 'kg', 'Yes', 'Brand D', 'Fresh organic apples', 'vegan', '{"Calories": 52}', 1, 'UK', 'True', 'None', 100, 'True', 'True', '2024-03-15', 'Dispose of in compost', 'nuts');

UPDATE Retail.Product SET promotions = 'Buy 1 Get 1 Free' WHERE product_id = 'M12345';

delete from Retail.Product WHERE Product.best_before_date < '2024-03-16';

drop view Cheapest_Product_Tomato;
delete from Retail.Product WHERE product_id='M12345'