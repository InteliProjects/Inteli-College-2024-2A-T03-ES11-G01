import json
from dotenv import load_dotenv
import core.clickhouse_client as clickhouse_client
import os
import pandas as pd

load_dotenv()

CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST")
CLICKHOUSE_PORT = os.getenv("CLICKHOUSE_PORT")

client = clickhouse_client.get_client()

query = "SELECT * FROM working_data WHERE tag = 'transactions'"

def remove_nan(df):
    df['data_row'] = df['data_row'].apply(json.loads)
    df_json = pd.json_normalize(df['data_row'])
    df_cleaned = df_json.dropna()
    return df_cleaned

def aplicar_arima_e_forecast(valores_mensais, steps=3):
    try:
        # Converter a lista de valores mensais em uma série temporal
        series = pd.Series(valores_mensais)

        # Definir o modelo ARIMA(p=1, d=1, q=1) como exemplo
        model = ARIMA(series, order=(1, 1, 1))
        
        # Ajustar o modelo
        model_fit = model.fit()

        # Fazer forecast para os próximos "steps" períodos
        forecast = model_fit.forecast(steps=steps)

        # Retornar o forecast como uma lista
        return forecast.tolist()
    except Exception as e:
        print(f"Erro ao aplicar ARIMA: {e}")
        return [None] * steps  # Se der erro, retorna uma lista de None


def pipeline():
    try:
        result = client.query(query)
        df = pd.DataFrame(result.result_rows, columns=result.column_names)
        df = remove_nan(df)
        df['data'] = pd.to_datetime(df['data'])
        df['mes'] = df['data'].dt.to_period('M')
        df_grouped = df.groupby(['cod_vendedor', 'mes'])['preco'].sum().reset_index()
        df_final = df_grouped.groupby('cod_vendedor')['preco'].apply(list).reset_index()
        df_final.columns = ['cod_vendedor', 'valor_mensal']
    except Exception as e:
        print("Error in Transactions: ", e)
        pass 
    df['forecast'] = df['valor_mensal'].apply(lambda x: aplicar_arima_e_forecast(x, steps=3))
    try:
        df = df.rename(columns={
            "cod_vendedor": "id_seller",
            "valor_mensal": "monthly_income",
            "forecast": "forecast"
        })
    except Exception as e:
        print("Error in Rename column Transactions ", e)
        pass   
    try:
        clickhouse_client.insert_dataframe(client, "tb_projection", df)
    except Exception as e:
        print("Error in Insert data in ClickHouse", e)    

