# Write your MySQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee e
INNER JOIN Department as d on d.id = e.departmentId
WHERE e.salary = (select max(salary) from Employee as e1 
                    inner join department as d2 on d2.id = e1.departmentId 
                    where d.name = d2.name);