select r.contest_id, 
round(count( distinct r.user_id)*100.0 / (select count(*) from users), 2) as percentage 
from users as u
join register as r
on u.user_id = r.user_id
group by r.contest_id
order by percentage desc,
r.contest_id asc;