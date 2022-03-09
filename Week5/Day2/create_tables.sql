-- Create the Customer Table
CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT primary key, 
    company_name TEXT not null, 
    contact_name TEXT, 
    contact_title TEXT, 
    address TEXT, 
    city TEXT, 
    region TEXT, 
    postal_code TEXT, 
    country TEXT, 
    phone TEXT, 
    fax TEXT);

-- Copy the Customer Table
\copy customers FROM '/Users/marija/WORK/SPICED/DS-Course/_prep/05-Dashboard/northwind-data/customers.csv' DELIMITER ',' CSV HEADER NULL 'NULL';


-- Create Employee Table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT primary key,
    last_name TEXT not null,
    first_name TEXT not null,
    title TEXT,
    title_of_courtesy TEXT,
    birth_date TIMESTAMP,
    hireDate TIMESTAMP,
    address TEXT,
    city TEXT,
    region TEXT,
    postalCode TEXT,
    country TEXT,
    homePhone TEXT,
    extension TEXT,
    photo TEXT,
    notes TEXT,
    reportsTo INT,
    photoPath TEXT);

-- \copy the Employees Table
\copy employees FROM '/Users/marija/WORK/SPICED/DS-Course/_prep/05-Dashboard/northwind-data/employees.csv' DELIMITER ',' CSV HEADER NULL 'NULL';


-- Create the Orders Table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT primary key,
    customer_id TEXT references customers (customer_id),
    employee_id INT references employees (employee_id),
    order_date TIMESTAMP,
    required_date TIMESTAMP,
    shipped_date TIMESTAMP,
    ship_via INT,
    freight REAL,
    ship_name TEXT,
    ship_address TEXT,
    ship_city TEXT,
    ship_region TEXT,
    ship_postal_code TEXT,
    ship_country TEXT);

-- Copy the orders table
\copy orders FROM '/Users/marija/WORK/SPICED/DS-Course/_prep/05-Dashboard/northwind-data/orders.csv' CSV HEADER NULL 'NULL';


-- Create the suppliers table
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INT PRIMARY KEY,
	company_name TEXT,
	contact_name TEXT,
	contact_title TEXT,
	address TEXT,
	city TEXT,
	region TEXT,
	postal_code TEXT,
	country TEXT,
	phone TEXT,
	fax TEXT,
	home_page TEXT
);

-- Copy the suppliers table
\copy suppliers FROM '/Users/marija/WORK/SPICED/DS-Course/_prep/05-Dashboard/northwind-data/suppliers.csv' CSV HEADER NULL 'NULL';


-- Create the categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INT PRIMARY KEY,
    category_name TEXT,
    description TEXT
);

-- Copy the categories table
\copy categories FROM PROGRAM 'cut -f 1-3 -d "," /Users/marija/WORK/SPICED/DS-Course/_prep/05-Dashboard/northwind-data/categories.csv' CSV HEADER NULL 'NULL';


-- Create the products table
CREATE TABLE IF NOT EXISTS products (
    product_id INT primary key,
    product_name TEXT not null,
    supplier_id INT references suppliers (supplier_id),
    category_id INT references categories (category_id),
    quantity_per_unit TEXT,
    unit_price FLOAT,
    units_in_stock INT,
    reorder_level INT,
    units_on_order INT,
    discontinued INT
);

-- Copy the products table
\copy products FROM '/Users/marija/WORK/SPICED/DS-Course/_prep/05-Dashboard/northwind-data/products.csv' CSV HEADER NULL 'NULL';


-- Create regions table
CREATE TABLE IF NOT EXISTS regions (
    region_id INT PRIMARY KEY,	
    region_description TEXT NOT NULL
);

-- Copy the regions table
\copy regions FROM '/Users/marija/WORK/SPICED/DS-Course/_prep/05-Dashboard/northwind-data/regions.csv' CSV HEADER NULL 'NULL';


-- Create order_details table
CREATE TABLE IF NOT EXISTS order_details (
    order_id INT references orders (order_id),
    product_id INT references products (product_id),
    unit_price FLOAT,
    quantity INT,
    discount REAL
);

-- Copy the order_details table
\copy order_details FROM '/Users/marija/WORK/SPICED/DS-Course/_prep/05-Dashboard/northwind-data/order_details.csv' CSV HEADER NULL 'NULL';


-- Create shippers table
CREATE TABLE IF NOT EXISTS shippers (
    shipper_id INT PRIMARY KEY,
    company_name TEXT,
    phone TEXT
);

-- Copy the shippers table
\copy shippers FROM '/Users/marija/WORK/SPICED/DS-Course/_prep/05-Dashboard/northwind-data/shippers.csv' CSV HEADER NULL 'NULL';


-- Create territories table
CREATE TABLE IF NOT EXISTS territories (
    territory_id INT PRIMARY KEY,
    territory_description TEXT,
    region_id int references regions (region_id)
);

-- Copy the territories table
\copy territories FROM '/Users/marija/WORK/SPICED/DS-Course/_prep/05-Dashboard/northwind-data/territories.csv' CSV HEADER NULL 'NULL';


-- Create employee_territories
CREATE TABLE IF NOT EXISTS employee_territories (
    employee_id INT references employees (employee_id),
    territory_id INT references territories (territory_id)
);

-- Copy the employee_territories table
\copy employee_territories FROM '/Users/marija/WORK/SPICED/DS-Course/_prep/05-Dashboard/northwind-data/employee_territories.csv' CSV HEADER NULL 'NULL';
