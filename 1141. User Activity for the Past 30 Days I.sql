# Write your MySQL query statement below
with temp as 
(
    select user_id, activity_date from Activity
    where activity_date between "2019-06-28" AND "2019-07-27"
)

select activity_date as 'day' , count(distinct user_id) as active_users
from temp
group by activity_date;