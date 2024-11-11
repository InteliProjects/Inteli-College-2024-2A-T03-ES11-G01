import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor


# ---- Union datasets
df = pd.read_csv('transaction_fact_v6_2023.csv')
df = pd.DataFrame(df)
df = df.groupby(['data', 'cod_vendedor', 'cod_loja'])['preco'].sum().reset_index()
df2 = pd.read_csv('transaction_fact_v6_2024.csv')
df2 = df2.groupby(['data', 'cod_vendedor', 'cod_loja'])['preco'].sum().reset_index()
df_unido = pd.concat([df, df2], axis=0)

# ---- Prepare data
df_unido['data'] = pd.to_datetime(df_unido['data'])
df_unido['dia_semana'] = df_unido['data'].dt.weekday
X = df_unido[['cod_vendedor', 'dia_semana', 'cod_loja']]
y = df_unido['preco']
label_encoder = LabelEncoder()
X['cod_vendedor'] = label_encoder.fit_transform(X['cod_vendedor'])
X['cod_loja'] = label_encoder.fit_transform(X['cod_loja'])
X['dia_semana'] = label_encoder.fit_transform(X['dia_semana'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---- Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

# ---- Results
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R² Score: {r2}")

# ---- Predictions
predicoes = pd.DataFrame({'Real': y_test, 'Previsto': y_pred})
print(predicoes.head())