# Write your MySQL query statement below
select employee_id from salaries 
where employee_id not in (select employee_id from employees)

union

select employee_id from employees
where employee_id not in (select employee_id from salaries)

order by employee_id;

