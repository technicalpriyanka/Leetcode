# Write your MySQL query statement below
select person_name
from(
    select person_name,
    sum(weight) over (order by turn ) as t_weight
    from queue
) as sub
where t_weight <= 1000 order by t_weight desc limit 1;