# ---- ClicHouse Connection

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col

spark = SparkSession.builder \
    .appName("ClickHouse to PySpark") \
    .config("spark.jars", "/path/to/clickhouse-jdbc-driver.jar") \
    .getOrCreate()

jdbc_url = "jdbc:clickhouse://localhost:8123/your_database"
jdbc_properties = {
    "user": "usuario",
    "password": "senha",
    "driver": "com.clickhouse.jdbc.ClickHouseDriver"
}

query = "(SELECT * FROM working_data WHERE date >= now() - INTERVAL 1 DAY) AS working_data"
df_spark = spark.read.jdbc(url=jdbc_url, table=query, properties=jdbc_properties)

# ---- Create schemas

employee_schema = StructType([
    StructField("id_empoyee", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("surname", StringType(), True),
    StructField("cpf", StringType(), True),
    StructField("status", StringType(), True),
    StructField("role", StringType(), True),
    StructField("inital_date", DateType(), True),
    StructField("end_date", DateType(), True),
    StructField("store_id", StringType(), True)
])

inventory_schema = StructType([
    StructField("nome_loja", StringType(), True),
    StructField("cod_prod", IntegerType(), True),
    StructField("data", DateType(), True),
    StructField("estoque", IntegerType(), True)
])

sku_cost_schema = StructType([
    StructField("cod_prod", IntegerType(), True),
    StructField("data_inicio", DateType(), True),
    StructField("data_fim", DateType(), True),
    StructField("custo", FloatType(), True)
])

sku_dataset_schema = StructType([
    StructField("cod_prd", IntegerType(), True),
    StructField("nome_abrev", StringType(), True),
    StructField("nome_completo", StringType(), True),
    StructField("descricao", StringType(), True),
    StructField("categoria", StringType(), True),
    StructField("sub_categoria", StringType(), True),
    StructField("marca", StringType(), True),
    StructField("conteudo_valor", IntegerType(), True),
    StructField("conteudo_medida", StringType(), True)
])

sku_price_schema = StructType([
    StructField("cod_prod", IntegerType(), True),
    StructField("data_incio", DateType(), True),
    StructField("data_fim", DateType(), True),
    StructField("preco", FloatType(), True)
])

sku_status_schema = StructType([
    StructField("cod_prod", IntegrType(), True),
    StructField("data_inicio", DateType(), True),
    StructField("data_fim", DateType(), True)
])

store_schema = StructType([
    StructField("nome_loja", StringType(), True),
    StructField("regiao", StringType(), True),
    StructField("diretoria", StringType(), True),
    StructField("data_inauguracao", DateType(), True)
])

target_store_schema = StructType([
    StructField("month", StringType(), True),
    StructField("store_id", IntegerType(), True),
    StructField("sales_target", IntegerType(), True)
])

target_sales_schema = StructType([
    StructField("id_employee", IntegerType(), True),
    StructField("sales_target", IntegerType(), True),
    StructField("month", StringType(), True)
])

transactions_schema = StructType([
    StructField("data", DateType(), True),
    StructField("cod_vendedor", IntegerType(), True),
    StructField("cod_loja", StringType(), True),
    StructField("cod_transacao", StringType(), True),
    StructField("quantidade", StringType(), True),
    StructField("cod_prod", IntegerType(), True),
    StructField("preco", FloatType(), True)
])


# ---- Config functions

def remove_nan(tag, schema):
    df_spark = df_csv.filter(df_csv["tag"] == tag)
    df_json = df_spark.withColumn("df_spark", from_json(col("data_rows")), schema)
    df_new = df_json.na.drop()
    return df_new

def filter_only(tag, schema):
    df_spark = df_csv.filter(df_csv["tag"] == tag)
    df_json = df_spark.withColumn("df_spark", from_json(col("data_rows")), schema)
    return df_new


# ---- Employee

try:
    df_employee = filter_only("employee", employe_schema)
    df_employee = df_employee.filter(df_employee['end_date'].isNull())
except Exception as e:
    print("Error in Employee ", e, "\n Essa tabela não tem atualizações")
    pass

# ---- Inventory

try:
    df_inventory = remove_nan("inventory", inventory_schema)
    df_inventory = df_inventory.withColumn("data", col("data").cast("timestamp"))
    window_spec = Window.partitionBy("cod_prod", "nome_loja").orderBy(col("data").desc())
    df_last = df_inventory.withColumn("row_num", row_number().over(window_spec)).filter(col("row_num") == 1)
    df_last = df_last.drop("row_num")
    df_inventory = df_last
except Exception as e:
    print("Error in Inventory ", e, "\n Essa tabela não tem atualizações")
    pass

# ---- SKU Cost

try:
    df_cost = filter_only("sku_cost", sku_cost_schema)
    df_cost = df_cost.filter(df_cost['data_fim'].isNull())
except Exception as e:
    print("Error in SKU Cost ", e, "\n Essa tabela não tem atualizações.")
    pass

# ---- SKU Price

try:
    df_price = filter_only("sku_price", sku_price_schema)
    df_price = df_price.filter(df_price['data_fim'].isNull())
except Exception as e:
    print("Error in SKU Price ", e, "\n Essa tabela não tem atualizações.")
    pass

# ---- SKU Status

try:
    df_status = filter_only("sku_status", sku_status_schema)
    df_status = df_status.filter(df_status['data_fim'].isNull())
except Exception as e:
    print("Error in SKU Status ", e, "\n Essa tabela não tem atualizações.")
    pass

# ---- New SKU Price and Cost
try:
    df_cost = df_cost.drop("data_incio")
    df_price = df_price.drop("data_incio")
    df_cost = df_cost.drop("data_fim")
    df_price = df_price.drop("data_fim")
    df_join = df_price.join(df_cost, on="cod_prod", how="inner")
    df_sku_cost_price = df_join.withColumn("profit", col("price") - col("cost"))
    df_sku_cost_price = df_sku_cost_price.join(df_status, on="cod_prod", how="inner")
except Exception as e:
    print("Error in New SKU Price and Cost ", e, "\n As tabelas que compõem essa tabela não tem atualizações.")
    pass

# ---- SKU Dataset
try:
    df_sku_dataset = remove_nan("sku_dataset", sku_dataset_schema)
except Exception as e:
    print("Error in SKU Dataset ", e, "\n Essa tabela não tem atualizações.")
    pass

# ---- Target Store

try:
    df_target_store = remove_nan("target_store", target_store_schema)
except Exception as e:
    print("Error in Target Store ", e, "\n Essa tabela não tem atualizações.")
    pass

# ---- Target Sales
try:
    df_target_sales = remove_nan("target_sales", target_sales_schema)
except Exception as e:
    print("Error in Target Sales ", e, "\n Essa tabela não tem atualizações.")
    pass

# ---- Store
try:
    df_store = remove_nan("store", store_schema)
except Exception as e:
    print("Error in Store ", e, "\n Essa tabela não tem atualizações.")
    pass

# ---- Transactions
try:
    df_transaction = remove_nan("transactions", transactions_schema)
    df_transaction = df_transaction.withColumn("unity_price", col("quantidade") - col("preco"))
except Exception as e:
    print("Error in Transactions ", e, "\n Essa tabela não tem atualizações.")
    pass

# ---- Rename column

try:
    df_employee = df_employee.withColumnRenamed("name","name") \
       .withColumnRenamed("id_store","id_store")
except Exception as e:
    print("Error in Rename column Employee ", e)
    pass

try:
    df_inventory = df_inventory.withColumnRenamed("nome_loja","name_store") \
        .withColumnRenamed("cod_prod","id_sku") \
        .withColumnRenamed("data","last_date") \
        .withColumnRenamed("estoque","quantity")
except Exception as e:
    print("Error in Rename column Inventory ", e)
    pass

try:
    df_sku_cost_price = df_sku_cost_price.withColumnRenamed("cod_prod","id_sku") \
        .withColumnRenamed("data_inicio","initial_date") \
        .withColumnRenamed("data_fim","final_date") \
        .withColumnRenamed("custo","cost") \
        .withColumnRenamed("preco","price") \
        .withColumnRenamed("profit","profit")
except Exception as e:
    print("Error in Rename column SKU Cost and Price ", e)
    pass 

try:
    df_dataset_sku = df_dataset_sku.withColumnRenamed("_c0","id_sku") \
        .withColumnRenamed("nome_completo","long_name") \
        .withColumnRenamed("nome_abrev","short_name") \
        .withColumnRenamed("categoria","category") \
        .withColumnRenamed("sub_categoria","sub_category") \
        .withColumnRenamed("marca","brand") \
        .withColumnRenamed("conteudo_valor","quantity")\
        .withColumnRenamed("conteudo_medida","type_quantity")
except Exception as e:
    print("Error in Rename column SKU Dataset ", e)
    pass

try:
    df_store = df_store.withColumnRenamed("nome_loja","ano") \
        .withColumnRenamed("regiao","region") \
        .withColumnRenamed("diretoria","board") \
        .withColumnRenamed("data_inauguracao","initial_date")
except Exception as e:
    print("Error in Rename column Store ", e)
    pass

try:
    df_target_store = df_target_store.withColumnRenamed("store_id","id_store")
except Exception as e:
    print("Error in Rename column Target Store ", e)
    pass

try:
    df_target_sales = df_target_sales.withColumnRenamed("id_employee","id_seller")
except Exception as e:
    print("Error in Rename column Target Sales ", e)
    pass

try:
    df_transaction = df_transaction.withColumnRenamed("data","data") \
        .withColumnRenamed("cod_vendedor","id_seller") \
        .withColumnRenamed("cod_loja","id_store") \
        .withColumnRenamed("cod_transacao","id_transaction") \
        .withColumnRenamed("quantidade","quantity") \
        .withColumnRenamed("cod_prod","id_store") \
        .withColumnRenamed("preco","total_price")
except Exception as e:
    print("Error in Rename column Transactions ", e)
    pass

# ---- Insert data in ClickHouse

try:
    df_employee.write.jdbc(
        url=jdbc_url,
        table="tb_employee",
        mode="append",
        properties=jdbc_properties
    )

    df_inventory.write.jdbc(
        url=jdbc_url,
        table="tb_inventory",
        mode="append",
        properties=jdbc_properties
    )

    df_sku_cost_price.write.jdbc(
        url=jdbc_url,
        table="tb_sku_cost_price",
        mode="append",
        properties=jdbc_properties
    )

    df_dataset_sku.write.jdbc(
        url=jdbc_url,
        table="tb_sku",
        mode="append",
        properties=jdbc_properties
    )

    df_store.write.jdbc(
        url=jdbc_url,
        table="tb_store",
        mode="append",
        properties=jdbc_properties
    )

    df_target_store.write.jdbc(
        url=jdbc_url,
        table="tb_target_store",
        mode="append",
        properties=jdbc_properties
    )

    df_target_sales.write.jdbc(
        url=jdbc_url,
        table="tb_target_salesperson",
        mode="append",
        properties=jdbc_properties
    )
except Exception as e:
    print("Error in Insert data in ClickHouse ", e)