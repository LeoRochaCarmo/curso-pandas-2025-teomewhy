SELECT
    seller_id,
    sum(t1.price) as totalRevenue,
    count(DISTINCT t1.order_id) as qtSalles
FROM tb_order_items as t1

LEFT JOIN tb_orders as t2
ON t1.order_id = t2.order_id

GROUP BY seller_id

