# Write your MySQL query statement below
select Product.product_name , Sales.year, Sales.price from Sales join product on sales.product_id = product.product_id;