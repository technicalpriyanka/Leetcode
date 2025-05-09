# Write your MySQL query statement below
-- select user_id,
--     MAX(time_stamp) AS last_stamp from Logins WHERE year(time_stamp) = 2020
-- group by user_id;

select user_id,
    MAX(time_stamp) AS last_stamp from Logins WHERE time_stamp like '2020%'
group by user_id;