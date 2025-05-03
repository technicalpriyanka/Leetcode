# Write your MySQL query statement below
select m.name from Employee as e 
inner join employee as m 
on e.managerId=m.id 
group by e.managerId 
having count(e.id)>=5