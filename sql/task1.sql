CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL,
    department TEXT NOT NULL
);

ALTER TABLE employees RENAME TO staff;

ALTER TABLE staff ADD COLUMN department TEXT;

INSERT INTO staff (name, position, salary, department)
VALUES ('John Doe', 'Software Engineer', 75000.0, 'Engineering');

INSERT INTO staff (name, position, salary, department)
VALUES ('Jane Smith', 'Product Manager', 90000.0, 'Product Management');

INSERT INTO staff (name, position, salary, department)
VALUES ('Alice Johnson', 'Data Scientist', 80000.0, 'Data Science');

UPDATE staff
SET salary = 80000.0
WHERE name = 'John Doe';

DELETE FROM staff
WHERE name = 'Alice Johnson';

SELECT * FROM staff;