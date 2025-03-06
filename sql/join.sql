-- Query 1: Display the first name, last name, department number, and department name for each employee
SELECT employee.first_name, employee.last_name, employee.department_id, department.department_name
FROM employees employee
JOIN departments department ON employee.department_id = department.department_id;

-- Query 2: Display the first and last name, department, city, and state province for each employee
SELECT employee.first_name, employee.last_name, department.department_name, location.city, location.state_province
FROM employees employee
JOIN departments department ON employee.department_id = department.department_id
JOIN locations location ON department.location_id = location.location_id;

-- Query 3: Display the first name, last name, department number, and department name for all employees in departments 80 or 40
SELECT employee.first_name, employee.last_name, employee.department_id, department.department_name
FROM employees employee
JOIN departments department ON employee.department_id = department.department_id
WHERE employee.department_id IN (40, 80);

-- Query 4: Display all departments including those where there are no employees
SELECT department.department_name, employee.first_name, employee.last_name
FROM departments department
LEFT JOIN employees employee ON department.department_id = employee.department_id;

-- Query 5: Display the first name of all employees including the first name of their manager
SELECT employee.first_name AS "Employee First Name", manager.first_name AS "Manager First Name"
FROM employees employee
LEFT JOIN employees manager ON employee.manager_id = manager.employee_id;

-- Query 6: Display the job title, full name (first and last name) of the employee, and the difference between the maximum salary for the job and the salary of the employee
SELECT job.job_title, employee.first_name || ' ' || employee.last_name AS "Full Name", (job.max_salary - employee.salary) AS "Salary Difference"
FROM employees employee
JOIN jobs job ON employee.job_id = job.job_id;

-- Query 7: Display the job title and the average salary of employees
SELECT job.job_title, AVG(employee.salary) AS "Average Salary"
FROM employees employee
JOIN jobs job ON employee.job_id = job.job_id
GROUP BY job.job_title;

-- Query 8: Display the full name (first and last name) and salary of employees who work in any department located in London
SELECT employee.first_name || ' ' || employee.last_name AS "Full Name", employee.salary
FROM employees employee
JOIN departments department ON employee.department_id = department.department_id
JOIN locations location ON department.location_id = location.location_id
WHERE location.city = 'London';

-- Query 9: Display the department name and the number of employees in each department
SELECT department.department_name, COUNT(employee.employee_id) AS "Number of Employees"
FROM departments department
LEFT JOIN employees employee ON department.department_id = employee.department_id
GROUP BY department.department_name;