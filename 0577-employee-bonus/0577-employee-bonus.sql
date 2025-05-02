# Write your MySQL query statement below
select employee.name, bonus.bonus from Employee left join bonus 
on employee.empId = bonus.empId where bonus < 1000 or bonus is null; 