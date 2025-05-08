# Write your MySQL query statement below
select name from SalesPerson 
where sales_id not in (select sales_id from Company 
join Orders on company.com_id = Orders.com_id 
where name = 'Red' );