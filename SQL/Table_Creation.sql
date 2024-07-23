drop table Retail.Awards;
drop table Retail.Product;
drop table Sales.Orders;
drop table Sales.Customer;
drop table Market.Supermarket;
drop table Retail.Category;

CREATE SCHEMA Sales;
CREATE SCHEMA Market;
CREATE SCHEMA Retail;

CREATE TABLE Sales.Customer
    (customer_id INT NOT NULL, 
    customer_name VARCHAR(255) NOT NULL, 
    customer_email VARCHAR(255),
    customer_number BIGINT,
    customer_address VARCHAR(255),
    CONSTRAINT pk_customer PRIMARY KEY (customer_id)
)

INSERT INTO Sales.Customer select CAST(customer_id AS INT) as customer_id,customer_name,customer_email,CAST(customer_number AS BIGINT) as customer_number,customer_address from dbo.ALL_DATA ;


CREATE TABLE Market.Supermarket
    (supermarket_id VARCHAR(255) NOT NULL, 
    supermarket_name VARCHAR(255) NOT NULL, 
    is_click_and_collect_available VARCHAR(255),
    rating FLOAT,
    CONSTRAINT pk_supermarket PRIMARY KEY (supermarket_id)
)
INSERT INTO Market.Supermarket select distinct supermarket_id,supermarket_name,is_click_and_collect_available,CAST(rating AS FLOAT) as rating from dbo.ALL_DATA;


CREATE TABLE Retail.Category
    (category_id INT NOT NULL, 
    category_name VARCHAR(255) NOT NULL, 
    CONSTRAINT pk_category PRIMARY KEY (category_id)
)
INSERT INTO Retail.Category select distinct CAST(category_id AS INT) category_id,category_name from dbo.ALL_DATA;

ALTER TABLE Retail.Category ADD category_available VARCHAR(255) NOT NULL DEFAULT 'YES';
select * from Retail.Category;

CREATE TABLE Sales.Orders
    (order_id VARCHAR(255) NOT NULL,
    order_date DATE,
    standard_delivery INT,
    fast_delivery INT,
    delivery_options VARCHAR(255),
    customer_id INT,
    CONSTRAINT pk_orders PRIMARY KEY (order_id),FOREIGN KEY (customer_id) REFERENCES Sales.Customer(customer_id)
)
INSERT INTO Sales.Orders select order_id,CONVERT(DATE, order_date,103) AS order_date, CAST(standard_delivery AS INT) standard_delivery,CAST(fast_delivery AS INT) fast_delivery, delivery_options,CAST(customer_id AS INT) customer_id from dbo.ALL_DATA;

CREATE TABLE Retail.Product
    (product_id VARCHAR(255) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    supermarket_id VARCHAR(255),
    category_id INT,
    order_id VARCHAR(255),
    price_in_pounds FLOAT,
    unit VARCHAR(255),
    available VARCHAR(255),
    brand VARCHAR(255),
    description VARCHAR(255),
    dietary_restrictions VARCHAR(255),
    nutritional_information VARCHAR(255),
    no_of_ingredients INT,
    country_of_origin VARCHAR(255),
    is_seasonal VARCHAR(255),
    promotions VARCHAR(255),
    stock_level INT,
    is_popular VARCHAR(255),
    is_new VARCHAR(255),
    best_before_date DATE,
    disposal_instructions VARCHAR(255),
    allergens VARCHAR(255),
    CONSTRAINT pk_product PRIMARY KEY (product_id),FOREIGN KEY (supermarket_id) REFERENCES Market.Supermarket(supermarket_id),
    FOREIGN KEY (category_id) REFERENCES Retail.Category(category_id),
    FOREIGN KEY (order_id) REFERENCES Sales.Orders(order_id)
)
INSERT INTO Retail.Product select product_id,product_name, supermarket_id, CAST(category_id AS INT) category_id,order_id, CAST(price_in_pounds AS FLOAT) price_in_pounds, unit,available,brand,description,dietary_restrictions,nutritional_information,CAST(no_of_ingredients AS INT) no_of_ingredients, country_of_origin, is_seasonal,promotions,CAST(stock_level AS INT) stock_level,is_popular,is_new, CONVERT(DATE, best_before_date,103) AS best_before_date,disposal_instructions,allergens from dbo.ALL_DATA;


CREATE TABLE Retail.Awards
    (product_id VARCHAR(255) NOT NULL,
    product_name VARCHAR(255),
    awards_won VARCHAR(255),
    number_of_reviews INT,
    CONSTRAINT fk_awards FOREIGN KEY (product_id) REFERENCES Retail.Product(product_id)
)
INSERT INTO Retail.Awards select product_id,product_name,awards_won, CAST(number_of_reviews AS INT) number_of_reviews from dbo.ALL_DATA;

