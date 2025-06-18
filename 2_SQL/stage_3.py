# Задание 1: Простая фильтрация
#
# SELECT c.id, order_date FROM customers as c
# INNER JOIN orders as o ON c.id = o.customer_id
# WHERE c.name = 'Иван Иванов'
#
#
# Задание 2: Фильтрация + сортировка
#
# SELECT product_name, quantity, price FROM order_items
# WHERE order_id = 1
# ORDER BY price DESC
#
# Задание 3: Группировка + фильтрация
#
# SELECT c.name, SUM(quantity * price) as total_spent FROM customers as c
# INNER JOIN orders as o ON c.id = o.customer_id
# INNER JOIN order_items as oi ON o.id = oi.order_id
# GROUP BY name
# HAVING SUM(quantity * price) > 5000
