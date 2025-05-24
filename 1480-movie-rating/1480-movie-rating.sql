# Write your MySQL query statement below
select name as results from(
    select u.name, count(u.name) as count
    from users u
    join MovieRating m
    on u.user_id = m.user_id
    group by u.user_id
    order by count desc, u.name asc limit 1
) as temp

union all

select title as results from (
    select mo.title, avg(m.rating) as avg_rating
    from movies mo
    join movierating m
    on m.movie_id = mo.movie_id
    where m.created_at between '2020-02-01' and '2020-02-28'
    group by m.movie_id
    order by avg_rating desc, mo.title asc limit 1
) as temp1 