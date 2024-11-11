
CREATE VIEW IF NOT EXISTS vw_inventory AS 
SELECT 
    id_sku, 
    short_name,
    final_date
FROM 
    tb_sku_status
INNER JOIN
    tb_sku ON tb_sku_status.id_sku = tb_sku.id
WHERE 
    final_date IS NULL;

CREATE VIEW IF NOT EXISTS vw_stores_ranking AS 
SELECT 
    tb_store.id, 
    tb_store.name, 
    tb_store.region, 
    toStartOfMonth(tb_transactions.date) AS month, 
    SUM(tb_transactions.total_price) AS total_sales, 
    tb_target_store.target 
FROM 
    tb_store
INNER JOIN 
    tb_transactions ON tb_store.id = tb_transactions.id_store 
INNER JOIN 
    tb_target_store ON tb_store.id = tb_target_store.id_store AND toStartOfMonth(tb_transactions.date) = tb_target_store.month
GROUP BY 
    tb_store.region, tb_store.id, tb_store.name, tb_target_store.target, month
ORDER BY 
    tb_store.region, total_sales DESC;

CREATE VIEW IF NOT EXISTS vw_sellers_ranking AS 
SELECT 
    tb_employee.id, 
    tb_employee.name, 
    tb_employee.surname, 
    tb_employee.role, 
    tb_employee.id_store, 
    toStartOfMonth(tb_transactions.date) AS month, 
    SUM(tb_transactions.total_price) AS total_sales, 
    tb_target_salesperson.target 
FROM 
    tb_employee
INNER JOIN 
    tb_transactions ON tb_employee.id = tb_transactions.id_seller 
INNER JOIN 
    tb_target_salesperson ON tb_employee.id = tb_target_salesperson.id_seller AND toStartOfMonth(tb_transactions.date) = tb_target_salesperson.month
GROUP BY 
    tb_employee.id, tb_employee.name, tb_employee.surname, tb_employee.role, tb_employee.id_store, tb_target_salesperson.target, month
ORDER BY 
    tb_employee.id_store, total_sales DESC;

CREATE VIEW IF NOT EXISTS vw_seller_progress AS 
SELECT 
    tb_employee.id, 
    tb_transactions.date, 
    SUM(tb_transactions.total_price) AS seller_total_sales,
    tb_target_salesperson.target 
FROM 
    tb_employee
INNER JOIN 
    tb_transactions ON tb_employee.id = tb_transactions.id_seller 
INNER JOIN 
    tb_target_salesperson ON tb_employee.id = tb_target_salesperson.id_seller 
GROUP BY 
    tb_employee.id, tb_transactions.date, tb_target_salesperson.target;

CREATE VIEW IF NOT EXISTS vw_store_progress AS 
SELECT 
    tb_store.id, 
    tb_transactions.date, 
    SUM(tb_transactions.total_price) AS store_total_sales,
    tb_target_store.target 
FROM 
    tb_store
INNER JOIN 
    tb_transactions ON tb_store.id = tb_transactions.id_store 
INNER JOIN 
    tb_target_store ON tb_store.id = tb_target_store.id_store 
GROUP BY 
    tb_store.id, tb_transactions.date, tb_target_store.target;

CREATE VIEW IF NOT EXISTS vw_top_products AS 
SELECT 
    tb_sku_cost_price.initial_date, 
    tb_sku_cost_price.final_date, 
    tb_sku_cost_price.profit, 
    tb_sku.id, 
    tb_sku.short_name, 
    tb_sku.category, 
    tb_sku.brand 
FROM 
    tb_sku_cost_price
INNER JOIN 
    tb_sku ON tb_sku_cost_price.id_sku = tb_sku.id 
WHERE 
    toStartOfMonth(tb_sku_cost_price.initial_date) = addMonths(toStartOfMonth(now()), -1) 
ORDER BY 
    profit DESC 
LIMIT 10;