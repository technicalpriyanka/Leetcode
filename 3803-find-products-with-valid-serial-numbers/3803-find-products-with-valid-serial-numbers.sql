-- # Write your MySQL query statement below
select * from products where description regexp '[^a-zA-Z0-9]SN[0-9]{4}-[0-9]{4}[^0-9]' or description regexp '[^a-zA-Z0-9]SN[0-9]{4}-[0-9]{4}$' order by 1;
-- ^|[^a-zA-Z0-9])


