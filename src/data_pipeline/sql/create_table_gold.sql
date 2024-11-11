CREATE TABLE IF NOT EXISTS tb_employee 
( 
    id UInt32,  
    name String,  
    surname String,  
    role String,  
    id_store UInt32  
) ENGINE = MergeTree() ORDER BY id;

CREATE TABLE IF NOT EXISTS tb_store 
( 
    id UInt32,  
    name String,  
    region String,  
    management String,
    initial_date DateTime
) ENGINE = MergeTree() ORDER BY id;

CREATE TABLE IF NOT EXISTS tb_transactions 
( 
    id UInt32,  
    date DateTime,  
    id_seller UInt32,  
    id_store UInt32,  
    quantity UInt32,  
    id_sku UInt32,
    total_price Float64,  
    unit_price Float64
) ENGINE = MergeTree() ORDER BY id;

CREATE TABLE IF NOT EXISTS tb_target_salesperson 
( 
    target UInt32,  
    month DateTime, 
    id_seller UInt32
) ENGINE = MergeTree() ORDER BY (month, id_seller);

CREATE TABLE IF NOT EXISTS tb_sku_cost_price 
( 
    id_sku UInt32,  
    initial_date DateTime, 
    final_date DateTime, 
    cost Float64,  
    price Float64,  
    profit Float64
) ENGINE = MergeTree() ORDER BY id_sku;

CREATE TABLE IF NOT EXISTS tb_sku 
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
) ENGINE = MergeTree() ORDER BY id;

CREATE TABLE IF NOT EXISTS tb_sku_status 
( 
    id_sku UInt32,  
    initial_date DateTime, 
    final_date Date
) ENGINE = MergeTree() ORDER BY id_sku;

CREATE TABLE IF NOT EXISTS tb_target_store 
( 
    target UInt32,  
    month DateTime, 
    id_store UInt32
) ENGINE = MergeTree() ORDER BY (month, id_store);

CREATE TABLE IF NOT EXISTS tb_substitute_sku 
( 
    id_sku UInt32,  
    name_complete_recommendations Array(String)
) ENGINE = MergeTree() ORDER BY (id_sku);

CREATE TABLE IF NOT EXISTS tb_crossell
( 
    antecedents String,
    consequents String,
    support Float64,
    confidence Float64,
    lift Float64
) ENGINE = MergeTree();

CREATE TABLE IF NOT EXISTS tb_projection
( 
    id_seller UInt32,
    monthly_income Array(Float64),
    forecast Array(Float64)
) ENGINE = MergeTree();
