# Write your MySQL query statement below
with temp as
(
    select p.product_id, p.price * u.units as price, u.units as unit
    from Prices p
    left join UnitsSold u on p.product_id = u.product_id
    where u.purchase_date between p.start_date and p.end_date
)

select product_id, 
    case 
        when unit is not null then round(sum(price) / sum(unit), 2)
        else 0
    end  as average_price
from temp
group by product_id;