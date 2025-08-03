CREATE TABLE IF NOT EXISTS individual (
    id INTEGER PRIMARY KEY AUTO INCREMENT,
    monthly_income REAL,
    age INTEGER,
    full_name TEXT,
    phone TEXT,
    email TEXT,
    category TEXT,
    balance REAL
);

CREATE TABLE IF NOT EXISTS company (
    id INTEGER PRIMARY KEY AUTO INCREMENT,
    monthly_income REAL,
    age INTEGER,
    trade_name TEXT,
    phone TEXT,
    corporate_email TEXT,
    category TEXT,
    balance REAL
);

INSERT INTO individual (monthly_income, age, full_name, phone, email, category, balance) VALUES
(5000.00, 35, 'John Silva', '9999-8888', 'john@example.com', 'Category A', 10000.00),
(4000.00, 45, 'Mary Oliveira', '7777-6666', 'mary@example.com', 'Category B', 15000.00),
(6000.00, 28, 'Peter Santos', '5555-4444', 'peter@example.com', 'Category C', 8000.00);

INSERT INTO company (monthly_income, age, trade_name, phone, corporate_email, category, balance) VALUES
(100000.00, 10, 'XYZ Corp', '1111-2222', 'contact@xyz.com', 'Category A', 50000.00),
(80000.00, 5, 'ABC Inc', '3333-4444', 'contact@abc.com', 'Category B', 70000.00),
(120000.00, 8, '123 LLC', '5555-6666', 'contact@123.com', 'Category C', 90000.00);
