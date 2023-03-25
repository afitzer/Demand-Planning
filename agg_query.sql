-- Get the aggregate of products with the product descriptions
SELECT p.description, SUM(g.gross_sales) AS total_sales
FROM fitzforecast_grosssales g
INNER JOIN fitzforecast_product p ON g.product_id = p.id
GROUP BY p.description;

-- Get the aggregate of the brands with the brand names
SELECT brand, SUM(g.gross_sales) AS total_sales
FROM fitzforecast_grosssales g
INNER JOIN fitzforecast_product p ON g.product_id = p.id
GROUP BY brand;



