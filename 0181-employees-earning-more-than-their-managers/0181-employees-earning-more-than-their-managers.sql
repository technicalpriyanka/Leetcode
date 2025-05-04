# Write your MySQL query statement below
select e1.name as Employee from Employee as e1 inner join Employee as e2 
on e2.id = e1.managerId where e1.salary > e2.salary