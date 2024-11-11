import pandas as pd
import clickhouse_connect
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder


# ---- Connection ClickHouse
client = clickhouse_connect.get_client(host='localhost', port=8123, username='ENV_USER_NAME', password='ENV_PASSWORD')
query = "SELECT * FROM working_data"
result = client.query(query)
df = pd.DataFrame(result.result_rows, columns=result.column_names)
df = df.filter(tag='transactions')
df2 = pd.DataFrame(result.result_rows, columns=result.column_names)
df2 = df.filter(tag='transactions')

# ---- Convert json to dataframe
df = pd.json_normalize(df['data_row'])

# ---- Calulate croos-selling
def gerar_regras_associacao(data4, data, min_support=0.001, min_confidence=0.1, top_n=10):
    inner_trans = pd.merge(data4, data, on='cod_prod')
    resultado = inner_trans.sort_values(by='cod_transacao')
    transacoes = resultado.groupby('cod_transacao')['nome_abrev'].apply(list)
    te = TransactionEncoder()
    transformed_data = te.fit(transacoes).transform(transacoes)
    trans = pd.DataFrame(transformed_data, columns=te.columns_)
    frequent_itemsets = apriori(trans, min_support=min_support, use_colnames=True)
    regras = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
    num_regras = len(regras)
    if num_regras > 0:
        num_regras_exibir = min(top_n, num_regras)
        regras_ordenadas = regras.sort_values(by='lift', ascending=False).head(num_regras_exibir)
        return regras_ordenadas[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
    else:
        return pd.DataFrame(columns=['antecedents', 'consequents', 'support', 'confidence', 'lift'])

df_insert = gerar_regras_associacao(df, df2, min_support=0.001, min_confidence=0.1, top_n=10)

dados = [tuple(x) for x in df_insert.to_numpy()]
client.insert('tb_substitute_sku', dados)