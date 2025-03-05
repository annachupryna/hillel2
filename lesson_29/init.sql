CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    department VARCHAR(100)
);

INSERT INTO employees (name, age, department) VALUES
    ('Alice', 30, 'development'),
    ('Bob', 45, 'hr'),
    ('Charlie', 28, 'marketing');
