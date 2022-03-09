#1) Get the names and the quantities in stock for each product.
SELECT product_id,product_name,units_in_stock FROM products
GROUP BY product_id
ORDER BY product_id ASC;

#2) Get a list of current products (Product ID and name).

SELECT product_id,product_name FROM products
WHERE discontinued=0

#3) Get a list of the most and least expensive products (name and unit price).


SELECT product_name, unit_price 
FROM products 
ORDER BY unit_price DESC;


#4) Get products that cost less than $20.

SELECT product_id,product_name,unit_price FROM products
WHERE  unit_price<20
ORDER BY unit_price DESC;


#5) Get products that cost between $15 and $25.

SELECT product_id,product_name,unit_price FROM products
WHERE  unit_price>=15 AND unit_price<=25
ORDER BY unit_price DESC;

#6) Get products above average price.

SELECT product_id,product_name,unit_price FROM products
WHERE  unit_price>(SELECT avg(unit_price)FROM products)
ORDER BY unit_price DESC;

#7) Find the ten most expensive products.

SELECT product_id,product_name,unit_price FROM products
ORDER BY unit_price DESC
LIMIT 10;


#8) Get a list of discontinued products (Product ID and name).

SELECT product_id,product_name FROM products
WHERE discontinued=1

#9) Count current and discontinued products.

SELECT discontinued ,count(product_id)FROM products
GROUP BY discontinued;

#10)Find products with less units in stock than the quantity on order.

#10) 

SELECT a.category_name FROM categories a,products b 
WHERE a.category_id=b.category_id;

/*Total orders per week by Category*/
SELECT SUM(o.order_id), c.category_name, EXTRACT(WEEK FROM o.order_date) AS week,
 EXTRACT(YEAR FROM o.order_date) AS year
    FROM orders AS o
	JOIN order_details AS od
	ON o.order_id = od.order_id
	JOIN products AS p
	ON od.product_ID = p.product_id
	JOIN categories as c
	ON p.category_id = c.category_id
    GROUP BY c.category_name, week, year;




SELECT category_name ,x.prod_revenue from (
    SELECT p.category_id, SUM(od.unit_price * od.quantity * (1 - od.discount)) as prod_revenue
    FROM products AS p
    JOIN  order_details AS od
    ON p.product_id = od.product_id
    GROUP BY p.category_id
    ORDER BY prod_revenue DESC
    LIMIT 5)x ,categories c 
    WHERE x.category_id=c.category_id
    GROUP BY;


    SELECT o.ship_country,c.countries_iso_code,SUM(od.unit_price * od.quantity * (1 - od.discount)) as prod_revenue
    FROM orders AS o,order_details AS od,countries c
    WHERE o.order_id = od.order_id AND c.countries_name=o.ship_country
    GROUP BY o.ship_country,c.countries_iso_code
    ORDER BY prod_revenue DESC;




    SELECT * FROM orders_detail;


    SELECT o.ship_country,c.countries_name,c.countries_id,c.countries_iso_code,
	EXTRACT(DAY FROM MAX(o.shipped_date - o.order_date))
	FROM orders o, countries c
    WHERE c.countries_name=o.ship_country
		
	GROUP BY o.ship_country,c.countries_name,c.countries_id;


    SELECT s.country,c.countries_iso_code 
    FROM suppliers s,countries c
    WHERE s.country=c.countries_name
    GROUP BY s.country,c.countries_iso_code;


SELECT o.ship_country,od.order_id, SUM(od.unit_price * od.quantity * (1 - od.discount)) 
as prod_revenue FROM order_details od, orders o
WHERE o.order_id=od.order_id
GROUP BY  od.order_id,o.ship_country,od.order_id
ORDER BY prod_revenue DESC
LIMIT 5;


SELECT employee_id,AGE(hiredate,birth_date),title,title_of_courtesy FROM employees;


SELECT employee_id, age(hiredate, birth_date) AS "hiring_age"
FROM employees;


Select employee_id,last_name ,first_name ,title , 
birth_date, hiredate,AGE(current_date,hiredate) 
from employees;

to_timestamp('05 Dec 2000', 'DD Mon YYYY');

Select count(employee_id),title 
from employees
Group by title;



select e.employee_id,count(o.customer_id)
from orders o , employees e
WHERE e.employee_id =o.employee_id
GROUP BY e.employee_id
ORDER BY  o.customer_id DESC ;

select e.employee_id,concat(e.first_name,' ',e.last_name),
count(o.order_id)
from customers c,orders o,employees e
WHERE e.employee_id=o.employee_id and c.customer_id=o.customer_id
GROUP BY e.employee_id
ORDER BY count DESC 

concat(e.first_name,' ',e.last_name);


select concat(e.first_name,' ',e.last_name),sum(DISTINCT (o.customer_id))
from orders o,employees e
WHERE e.employee_id=o.employee_id and e.employee_id=4
ORDER BY o.customer_id DESC ;

first_name,last_name,
sum(DISTINCT (o.customer_id))


concat(e.first_name,' ',e.last_name);

select  e.employee_id,concat(e.first_name,' ',e.last_name),count(distinct(o.customer_id))
from orders o, employees e
where e.employee_id=o.employee_id 
GROUP BY e.employee_id
ORDER BY count(distinct(o.customer_id)) DESC 
LIMIT 3;

Select k.order_date,sum((o.unit_price)*(o.quantity)) from order_details o, orders k
Where k.order_id=o.order_id
GROUP BY  k.order_date;
Select TO_CHAR(k.order_date,'YYYY'),sum((o.unit_price)*(o.quantity)) 

from order_details o, orders k
Where k.order_id=o.order_id
GROUP BY TO_CHAR(k.order_date,'YYYY');



 TO_CHAR(
        payment_date,
        'HH12:MI:SS');


Select TO_CHAR((k.order_date),'YYYY'),count(k.order_id),c.category_id,c.category_name from order_details o, categories c, products p,orders k
Where c.category_id=p.category_id and o.product_id=p.product_id
and k.order_id=o.order_id
GROUP BY c.category_id,c.category_name,TO_CHAR((k.order_date),'YYYY');
;
  SELECT SUM(od.unit_price * od.quantity * (1 - od.discount)) as prod_revenue
    FROM orders AS o,order_details AS od,countries c
    WHERE o.order_id = od.order_id AND c.countries_name=o.ship_country

    ORDER BY prod_revenue DESC;


    SELECT o.ship_country, SUM(od.unit_price * od.quantity * (1 - od.discount)) 
as prod_revenue FROM order_details od, orders o
WHERE o.order_id=od.order_id
GROUP BY  o.ship_country
ORDER BY prod_revenue DESC
LIMIT 5;
