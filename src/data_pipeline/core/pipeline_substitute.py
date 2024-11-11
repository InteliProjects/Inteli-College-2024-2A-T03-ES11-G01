import pandas as pd
import torch
from transformers import BertModel, BertTokenizer
from sklearn.metrics.pairwise import cosine_similarity
import clickhouse_connect

# ---- Prepare BERT model
model_name = "neuralmind/bert-base-portuguese-cased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)
def gerar_embedding_bert(texto):
    inputs = tokenizer(texto, return_tensors="pt", max_length=512, truncation=True, padding="max_length")
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()


# ---- Connection ClickHouse
client = clickhouse_connect.get_client(host='localhost', port=8123, username='ENV_USER_NAME', password='ENV_PASSWORD')
query = "SELECT * FROM working_data"
result = client.query(query)
df = pd.DataFrame(result.result_rows, columns=result.column_names)
df = df.filter(tag='sku_dataset')

# ---- Convert json to dataframe
df = pd.json_normalize(df['data_row'])


# ---- Generate embeddings
df['texto_completo'] = df['nome_completo'] + " " + df['descricao'] + " " + df['categoria'] + " " + df['sub_categoria']
df['embedding'] = df['texto_completo'].apply(gerar_embedding_bert)


# ---- Recommend products
def recomendar_produto(nome_produto, df):
    if nome_produto not in df['nome_abrev'].values:
        raise ValueError(f"O produto '{nome_produto}' não foi encontrado no DataFrame.")
    idx = df[df['nome_abrev'] == nome_produto].index[0]
    produto_embedding = df.loc[idx, 'embedding']
    sim_scores = cosine_similarity([produto_embedding], df['embedding'].tolist())[0]
    sim_scores = list(enumerate(sim_scores))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    recomendacoes_idx = [i[0] for i in sim_scores]
    recomendacoes = df['nome_completo'].iloc[recomendacoes_idx]
    return recomendacoes

def aplicar_recomendacao(row, df):
    try:
        return recomendar_produto(row['nome_abrev'], df).tolist()
    except ValueError as e:
        print(e)
        return []
    
df['recomendacoes'] = df.apply(lambda row: aplicar_recomendacao(row, df), axis=1)
df_insert = df[['cod_prod', 'recomendacoes']]
df_insert.rename(columns={'cod_prod': 'id_sku', 'recomendacoes': 'name_complete_recommendations'}, inplace=True)
dados = [tuple(x) for x in df_insert.to_numpy()]
client.insert('tb_substitute_sku', dados)