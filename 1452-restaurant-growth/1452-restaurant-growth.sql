# Write your MySQL query statement below
select a.visited_on, 
        sum(b.amount) as amount, 
        round(sum(b.amount)/7 , 2) as average_amount

from (select distinct visited_on from customer) a

join customer b 
on b.visited_on between date_sub(a.visited_on, interval 6 day) and a.visited_on
group by a.visited_on
having count(distinct b.visited_on) = 7
order by a.visited_on;
