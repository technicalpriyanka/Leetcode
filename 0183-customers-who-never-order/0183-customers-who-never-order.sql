# Write your MySQL query statement below
select Customers.name as Customers from Customers 
where Customers.id not in (select Orders.customerId from orders);