CREATE TABLE IF NOT EXISTS working_data (
    date_ingestion DateTime,
    data_row String,
    tag String
) ENGINE = MergeTree()
ORDER BY date_ingestion;


CREATE TABLE tb_employee 
( 
    id UInt32,  
    name String,  
    surname String,  
    role String,  
    id_store UInt32  
) 
ENGINE = MergeTree()
ORDER BY id;

CREATE TABLE tb_store 
( 
    id UInt32,  
    name String,  
    region String,  
    management String
) 
ENGINE = MergeTree()
ORDER BY id;

CREATE TABLE tb_transactions 
( 
    id UInt32,  
    date Date,  
    id_seller UInt32,  
    id_store UInt32,  
    quantity UInt32,  
    total_price Float64,  
    unit_price Float64
) 
ENGINE = MergeTree()
ORDER BY id;

CREATE TABLE tb_target_salesperson 
( 
    target UInt32,  
    month Date,  
    id_seller UInt32
) 
ENGINE = MergeTree()
ORDER BY (month, id_seller);

CREATE TABLE tb_sku_cost_price 
( 
    id_sku UInt32,  
    initial_date Date,  
    final_date Date,  
    cost Float64,  
    price Float64,  
    profit Float64
) 
ENGINE = MergeTree()
ORDER BY id_sku;

CREATE TABLE tb_sku 
( 
    id UInt32,  
    short_name String,  
    complete_name String,  
    description String,  
    category String,  
    sub_category String,  
    brand String,  
    contents Float64,  
    contents_measurement String
) 
ENGINE = MergeTree()
ORDER BY id;

CREATE TABLE tb_sku_status 
( 
    id_sku UInt32,  
    initial_date Date,  
    final_date Date
) 
ENGINE = MergeTree()
ORDER BY id_sku;

CREATE TABLE tb_target_store 
( 
    target UInt32,  
    month Date,  
    id_store UInt32
) 
ENGINE = MergeTree()
ORDER BY (month, id_store);

----------------- Creating Views -------------------------------------

CREATE VIEW vw_inventory AS 
SELECT 
    id_sku, 
    short_name
    final_date,
FROM 
    tb_sku_status
INNER JOIN
    tb_sku ON tb_sku_status.id_sku = tb_sku.id
WHERE 
    final_date IS NULL;

CREATE VIEW vw_stores_ranking AS 
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

CREATE VIEW vw_sellers_ranking AS 
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

CREATE VIEW vw_seller_progress AS 
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

CREATE VIEW vw_store_progress AS 
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

CREATE VIEW vw_top_products AS 
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