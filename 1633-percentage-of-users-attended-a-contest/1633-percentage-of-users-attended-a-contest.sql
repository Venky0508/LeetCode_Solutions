# Write your MySQL query statement below
select r.contest_id, round(count(r.user_id)/(select count(user_id) as total from Users), 4)*100 as percentage
from Register as r
join Users as u
on r.user_id = u.user_id
group by r.contest_id
order by percentage desc, r.contest_id asc; 
