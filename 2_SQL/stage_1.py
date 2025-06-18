# CREATE TABLE customers
# (
# 	id SERIAL PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     email VARCHAR(255) UNIQUE NOT NULL
# );
#
# CREATE TABLE orders
# (
# 	id SERIAL PRIMARY KEY,
# 	customer_id int REFERENCES customers(id),
# 	order_date DATE
# );
#
# CREATE TABLE order_items
# (
# 	id SERIAL PRIMARY KEY,
# 	order_id int REFERENCES orders(id),
# 	product_name VARCHAR(255) NOT NULL,
# 	quantity int NOT NULL,
# 	price FLOAT
# );