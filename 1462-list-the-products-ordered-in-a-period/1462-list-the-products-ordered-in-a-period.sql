# Write your MySQL query statement below
select products.product_name, sum(orders.unit) as unit
from products 
inner join orders
using (product_id)
where DATE_FORMAT(orders.order_date, '%Y-%m') = '2020-02'
group by product_id
having sum(orders.unit) >= 100;