DROP TRIGGER IF EXISTS Retail.check_best_before_date;
DROP TRIGGER IF EXISTS Sales.enforce_min_order_price;


CREATE TRIGGER check_best_before_date
ON Retail.Product
INSTEAD OF INSERT, UPDATE
AS
BEGIN
    IF EXISTS (SELECT 1 FROM inserted WHERE best_before_date < GETDATE())
    BEGIN
        PRINT 'Error: Product has expired and cannot be inserted or updated.';
    END
    ELSE
    BEGIN
        -- Perform the insert or update operation
        INSERT INTO Retail.Product (product_id, product_name, supermarket_id, category_id, order_id, price_in_pounds, unit, available, brand, description, dietary_restrictions, nutritional_information, no_of_ingredients, country_of_origin, is_seasonal, promotions, stock_level, is_popular, is_new, best_before_date, disposal_instructions, allergens)
        SELECT product_id, product_name, supermarket_id, category_id, order_id, price_in_pounds, unit, available, brand, description, dietary_restrictions, nutritional_information, no_of_ingredients, country_of_origin, is_seasonal, promotions, stock_level, is_popular, is_new, best_before_date, disposal_instructions, allergens
        FROM inserted;
    END
END;


CREATE TRIGGER enforce_min_order_price
ON Sales.Orders
INSTEAD OF INSERT, UPDATE
AS
BEGIN
    DECLARE @min_order_price DECIMAL(10, 2);
    SET @min_order_price = 40.00; -- Minimum order price threshold
    
    IF EXISTS (
        SELECT * 
        FROM inserted i
        INNER JOIN (
            SELECT order_id, SUM(p.price_in_pounds) AS total_order_price
            FROM Orders o
            JOIN Product p ON o.product_id = p.product_id
            GROUP BY order_id
        ) o ON i.order_id = o.order_id
        WHERE o.total_order_price < @min_order_price
    )
    BEGIN
        RAISERROR('Order cannot be placed. Minimum order price must be at least £40.', 16, 1);
        RETURN;
    END;
    
    -- If all orders meet the minimum order price requirement, proceed with the insert or update
    INSERT INTO Sales.Orders (order_id, order_date, standard_delivery, fast_delivery, delivery_options, customer_id)
    SELECT order_id, order_date, standard_delivery, fast_delivery, delivery_options, customer_id FROM inserted;
END;


SELECT * FROM sys.triggers;



ALTER TABLE Sales.Customer
ADD CONSTRAINT UC_Email UNIQUE (customer_email);

ALTER TABLE Sales.Customer
ADD CONSTRAINT UC_PhoneNumber UNIQUE (customer_number);

SELECT
    name AS constraint_name,
    is_disabled
FROM 
    sys.indexes
WHERE 
    object_id = OBJECT_ID('Sales.Customer');


SELECT * FROM sys.key_constraints;
SELECT * FROM sys.foreign_keys;

SELECT * FROM sys.views;
