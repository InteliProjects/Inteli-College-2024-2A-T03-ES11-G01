import json
from dotenv import load_dotenv
import core.clickhouse_client as clickhouse_client
import os
import pandas as pd

load_dotenv()

CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST")
CLICKHOUSE_PORT = os.getenv("CLICKHOUSE_PORT")

client = clickhouse_client.get_client()

query = "SELECT * FROM working_data WHERE date_ingestion >= now() - INTERVAL 1 DAY"

def remove_nan(df, tag):

    df_filtered = df[df['tag'] == tag]
    df_filtered['data_row'] = df_filtered['data_row'].apply(json.loads)
    df_json = pd.json_normalize(df_filtered['data_row'])
    df_cleaned = df_json.dropna()
    return df_cleaned

def filter_only(df, tag):
    df_filtered = df[df['tag'] == tag]
    df_filtered['data_row'] = df_filtered['data_row'].apply(json.loads)
    df_json = pd.json_normalize(df_filtered['data_row'])
    return df_json

def remove_column(df):
    return df.drop(columns=['date_ingestion'], errors="ignore")

def pipeline():
    result = client.query(query)
    df = pd.DataFrame(result.result_rows, columns=result.column_names)
    print(df)

    df_employee = ''
    df_inventory = ''
    df_cost = ''
    df_sku_cost_price = ''
    df_dataset_sku = ''
    df_sku_dataset = ''
    df_price = ''
    df_store = ''
    df_status = ''
    df_target_store = ''
    df_target_salesperson = ''
    df_transaction = ''
    
    try:
        df_employee = remove_nan(df, 'employee_final')
        df_employee = df_employee[df_employee['end_date'].isnull()]
    except Exception as e:
        print("Error in Employee ", e, "\n Essa tabela não tem atualizações")
        pass   

    try:
        df_inventory = remove_nan(df, 'inventory')
        df_inventory['data'] = pd.to_datetime(df_inventory['data'])
        df_inventory = df_inventory.sort_values(by=['cod_prod', 'nome_loja', 'data'], ascending=[True, True, False])
        df_last = df_inventory.drop_duplicates(subset=['cod_prod', 'nome_loja'], keep='first')
    except Exception as e:
        print("Error in Inventory ", e, "\n Essa tabela não tem atualizações")
        pass

    try:
        df_cost = filter_only(df, 'sku_cost')
        df_cost = df_cost[df_cost['data_fim'].isnull()]
    except Exception as e:
        print("Error in SKU Cost ", e, "\n Essa tabela não tem atualizações.")
        pass

    try:
        df_price = filter_only(df, 'sku_price')
        df_price = df_price[df_price['data_fim'].isnull()]
    except Exception as e:
        print("Error in SKU Price ", e, "\n Essa tabela não tem atualizações.")
        pass

    try:
        df_status = filter_only(df, 'sku_status_dataset')
        df_status = df_status[df_status['data_fim'].isnull()]
    except Exception as e:
        print("Error in SKU Status ", e, "\n Essa tabela não tem atualizações.")
        pass

    try:
        df_cost = df_cost.drop(columns=["data_incio", "data_fim"], errors="ignore")
        df_price = df_price.drop(columns=["data_incio", "data_fim"], errors="ignore")
        df_join = pd.merge(df_price, df_cost, on="cod_prod", how="inner")
        df_join['profit'] = df_join['price'] - df_join['cost']
        df_sku_cost_price = pd.merge(df_join, df_status, on="cod_prod", how="inner")
    except Exception as e:
        print("Error in New SKU Price and Cost ", e, "\nAs tabelas que compõem essa tabela não têm atualizações.")
        pass

    try:
        df_sku_dataset = remove_nan(df, 'sku_dataset')
    except Exception as e:  
        print("Error in Sku DataSet ", e, "\n Essa tabela não tem atualizações")
        pass

    try:
        df_dataset_sku = remove_nan(df, 'sku_dataset')
    except Exception as e:  
        print("Error in Sku DataSet ", e, "\n Essa tabela não tem atualizações")
        pass

    try:
        df_target_store = remove_nan(df, 'target_store_final')
    except Exception as e:
        print("Error in Target Store Final ", e, "\n Essa tabela não tem atualizações")
        pass

    try:
        df_target_salesperson = remove_nan(df, 'target_salesperson_final')
    except Exception as e:
        print("Error in Target Salesperson Final ", e, "\n Essa tabela não tem atualizações")
        pass


    try:
        df_store = remove_nan(df, 'store_final')
    except Exception as e:
        print("Error in Store Final ", e, "\n Essa tabela não tem atualizações")
        pass

    try:
        df_transaction = remove_nan(df, 'transactions')
        df_transaction['unity_price'] = df_transaction['quantidade'] - df_transaction['preco']
    except Exception as e:
        print("Error in Transactions ", e, "\n Essa tabela não tem atualizações")
        pass

    try:
        df_employee = df_employee.rename(columns={
                "name": "name",
                "id_store": "id_store"
            })
    except Exception as e:
        print("Error in Rename column Employee ", e)
        pass

    try:
        df_inventory = df_inventory.rename(columns={
            "nome_loja": "name_store",
            "cod_prod": "id_sku",
            "data": "last_date",
            "estoque": "quantity"
        })
    except Exception as e:
        print("Error in Rename column Inventory ", e)
        pass

    try:
        df_sku_cost_price = df_sku_cost_price.rename(columns={
            "cod_prod": "id_sku",
            "data_inicio": "initial_date",
            "data_fim": "final_date",
            "custo": "cost",
            "preco": "price",
            "profit": "profit"
        })
    except Exception as e:
        print("Error in Rename column SKU Cost and Price ", e)
        pass

    try:
        df_dataset_sku = df_dataset_sku.rename(columns={
            "_c0": "id_sku",
            "nome_completo": "complete_name",
            "nome_abrev": "short_name",
            "categoria": "category",
            "sub_categoria": "sub_category",
            "marca": "brand",
            "conteudo_valor": "contents",
            "conteudo_medida": "contents_measurement"
        })
    except Exception as e:
        print("Error in Rename column SKU Dataset ", e)
        pass

    try:
        df_store = df_store.rename(columns={
            "nome_loja": "name",
            "regiao": "region",
            "diretoria": "management",
            "data_inauguracao": "initial_date"
        })
    except Exception as e:
        print("Error in Rename column Store ", e)
        pass

    try:
        df_target_store = df_target_store.rename(columns={
            "store_id": "id_store"
        })
    except Exception as e:
        print("Error in Rename column Target Store ", e)
        pass

    try:
        df_target_salesperson = df_target_salesperson.rename(columns={
            "id_employee": "id_seller"
        })
    except Exception as e:
        print("Error in Rename column Target Sales ", e)
        pass

    try:
        df_transaction = df_transaction.rename(columns={
            "data": "date",
            "cod_vendedor": "id_seller",
            "cod_loja": "id_store",
            "cod_transacao": "id_transaction",
            "quantidade": "quantity",
            "cod_prod": "id_sku",
            "preco": "total_price"
        })
    except Exception as e:
        print("Error in Rename column Transactions ", e)
        pass

    try:
        df_employee = remove_column(df_employee)
        clickhouse_client.insert_dataframe(client, "tb_employee", df_employee)
    except Exception as e:
        print("Error in Insert data in ClickHouse", e)        
        
    try:
        df_inventory = remove_column(df_inventory)
        clickhouse_client.insert_dataframe(client, "tb_inventory", df_inventory)
    except Exception as e:
        print("Error in Insert data in ClickHouse", e)
        
    try:
        tb_sku_cost_price = remove_column(tb_sku_cost_price)
        clickhouse_client.insert_dataframe(client, "tb_sku_cost_price", df_sku_cost_price)
        
    except Exception as e:
        print("Error in Insert data in ClickHouse", e) 
        
    try:
        df_dataset_sku = remove_column(df_dataset_sku)
        clickhouse_client.insert_dataframe(client, "tb_sku", df_dataset_sku)
    except Exception as e:
        print("Error in Insert data in ClickHouse", e)
        
    try:
        df_store = remove_column(df_store)
        clickhouse_client.insert_dataframe(client, "tb_store", df_store)
    except Exception as e:
        print("Error in Insert data in ClickHouse", e)
        
    try:
        tb_target_store = remove_column(tb_target_store)
        clickhouse_client.insert_dataframe(client, "tb_target_store", df_target_store)
    except Exception as e:
        print("Error in Insert data in ClickHouse", e)
        
    try:
        tb_target_salesperson = remove_column(tb_target_salesperson)
        clickhouse_client.insert_dataframe(client, "tb_target_salesperson", df_target_salesperson)
    except Exception as e:
        print("Error in Insert data in ClickHouse", e)