CREATE PROCEDURE PlaceOrder
    @customer_id INT,
    @product_id VARCHAR(255)
AS
BEGIN
    -- Check product availability
    DECLARE @available VARCHAR(255);
    DECLARE @stock_level INT;
    
    SELECT @available = available,
           @stock_level = stock_level
    FROM Retail.Product
    WHERE product_id = @product_id;

    IF @available = 'Yes' AND @stock_level > 0
    BEGIN
        -- Calculate order total
        DECLARE @unit_price FLOAT;
        SELECT @unit_price = price_in_pounds
        FROM Retail.Product
        WHERE product_id = @product_id;

        DECLARE @order_total FLOAT;
        SET @order_total = @unit_price;

        -- Insert order into Orders table
        DECLARE @order_id VARCHAR(255);
        SET @order_id = 'ORD' + CAST(NEWID() AS VARCHAR(36));

        INSERT INTO Sales.Orders (order_id, order_date, standard_delivery, fast_delivery, delivery_options, customer_id)
        VALUES (@order_id, GETDATE(), 3, 1, 'Standard', @customer_id);

        -- Update stock level
        UPDATE Retail.Product
        SET stock_level = stock_level - 1
        WHERE product_id = @product_id;

        -- Return order ID and total
        SELECT @order_id AS order_id, @order_total AS order_total;
    END
    ELSE
    BEGIN
        -- Product not available
        RAISERROR ('Product is not available.', 16, 1);
    END
END;


SELECT 
    OBJECT_DEFINITION(OBJECT_ID('PlaceOrder')) AS ProcedureDefinition;


SELECT * from sys.procedures;