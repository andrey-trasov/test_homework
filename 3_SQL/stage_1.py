# Этап 1: Массовое наполнение базы
#
# INSERT INTO order_items (order_id, product_name, price, quantity)
# SELECT
#     (trunc(random() * 3) + 1)::INT,
#     'Товар ' || (random() * 500)::int + 1,
#     (random() * 99900 + 100)::DECIMAL(10, 2),
#     (random() * 9 + 1)::INT
# FROM generate_series(1, 1000000 - (SELECT COUNT(*) FROM order_items)) AS gs;
#
#
#
# Этап 2: Установка индексов
#
# CREATE INDEX idx_orders_customer_id
# ON orders (customer_id);
#
#
# CREATE INDEX idx_order_items_order_id_price
# ON order_items (order_id, price);
#
#
# CREATE INDEX idx_order_items_product_name
# ON order_items (product_name);
#
#
# Этап 3: Анализ использования индексов
#
# Все товары с price > 10000 из заказа с ID = 123.
#
# EXPLAIN ANALYZE
# SELECT product_name, price, quantity FROM order_items
# WHERE order_id = 1 AND price > 10000;
#
#
# Все заказы клиента с customer_id = 1.
#
# EXPLAIN ANALYZE
# SELECT customer_id FROM orders
# WHERE customer_id = 1
#
# Этап 4: Удаление неэффективных индексов
# удаляю индекс потому что у меня всего 3 заказа
#
# DROP INDEX public.idx_orders_customer_id;
#
#
# Этап 5: Бизнес-логика с использованием транзакций
#
# Создание новой записи в таблице orders с текущей датой.
# Добавление 3–5 случайных товаров в таблицу order_items для созданного заказа.
# В случае любой ошибки (например, попытка вставить NULL в product_name), вся транзакция откатывается.
#
# BEGIN;
#
# WITH new_order AS (
#   INSERT INTO orders (customer_id, order_date)
#   VALUES (1, '2025-06-19')
#   RETURNING id
# )
#
# INSERT INTO order_items (order_id, product_name, quantity, price)
# VALUES
#   ((SELECT id FROM new_order), 'Ноутбук', 1, 65000.00),
#   ((SELECT id FROM new_order), 'Монитор', 1, 85000.00),
#   ((SELECT id FROM new_order), 'Мышь', 1, 1500.00),
#   ((SELECT id FROM new_order), NULL, 1, 1500.00);
# COMMIT;

