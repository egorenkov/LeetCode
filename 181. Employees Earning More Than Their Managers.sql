# Write your MySQL query statement below
SELECT e1.name as Employee
FROM  Employee as e1
where e1.salary >   (SELECT e2.salary 
                FROM Employee as e2
                WHERE e2.id = e1.managerId);