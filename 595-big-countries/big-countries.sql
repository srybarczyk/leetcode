/* Write your T-SQL query statement below */
select name, population, area
from World
where population>=25000000 or area >=3000000;