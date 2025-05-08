# Write your MySQL query statement below
select u.name, IFNULL(sum(t.distance), 0) as travelled_distance
from users as u 
left join rides t
on u.id = t.user_id 
group by user_id 
order by travelled_distance DESC, name;