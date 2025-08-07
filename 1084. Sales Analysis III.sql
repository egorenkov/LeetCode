# Write your MySQL query statement below

SELECT DISTINCT p.product_id, p.product_name FROM Product p
join Sales s On p.product_id = s.product_id
WHERE s.sale_date >= "2019-01-01" AND s.sale_date <= "2019-03-31"
AND p.product_id NOT IN (
    SELECT DISTINCT p.product_id FROM Product p
    join Sales s On p.product_id = s.product_id
    WHERE s.sale_date < "2019-01-01" OR s.sale_date > "2019-03-31" 
);
