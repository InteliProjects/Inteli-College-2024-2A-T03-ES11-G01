import re
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime
import os
from prefect import task

from pydantic import BaseModel, Enum, ValidationError

class RoleEnum(str, Enum):
    seller = 'vendedor'
    manager = 'gerente'

class StatusEnum(str, Enum):
    active = 'ativo'
    inactive  = 'não ativo'

class ContentMeasureEnum(str, Enum):
    ml = 'ml'
    lbs  = 'lbs'
    oz  = 'oz'

class Employee(BaseModel):
    id_employee: str  
    name: str 
    surname: str 
    cpf: str
    status: StatusEnum  
    role: RoleEnum  
    initial_date: datetime  
    end_date: datetime | None
    store_id: str
    
class SkuCost(BaseModel):
    cod_prod: str
    data_inicio: datetime
    data_fim: datetime | None
    custo: float
    
class SkuDataset(BaseModel):
    cod_prod: str
    nome_abrev: str
    nome_completo: str
    descricao: str
    categoria: str	
    sub_categoria: str
    marca: str
    conteudo_valor: float
    conteudo_medida: ContentMeasureEnum
    
class SkuPrice(BaseModel):
    cod_prod: str
    data_inicio: datetime
    data_fim: datetime | None
    preco: float
    
class SkuStatusDataset(BaseModel):
    cod_prod: str
    data_inicio: datetime
    data_fim: datetime | None
    
class Store(BaseModel):
    nome_loja: str
    regiao: str
    diretoria: str
    data_inauguracao: datetime
    
class TargetStore(BaseModel):
    month: str
    store_id: str
    sales_target: int
    
class TargetSalesperson(BaseModel):
    id_employee: str
    sales_target: int
    month: str

class Year(BaseModel):
    data: datetime
    cod_vendedor: str
    cod_loja: str
    cod_transacao: str
    quantidade: int
    cod_prod: str
    preco: float

tables_columns_model = {
  "employee_final": Employee,
  "sku_cost": SkuCost,
  "sku_dataset": SkuDataset,
  "sku_price": SkuPrice,
  "sku_status_dataset": SkuStatusDataset,
  "store_final": Store,
  "target_store_final": TargetStore,
  "target_salesperson_final": TargetSalesperson,
  "year": Year
}

tables_columns = {
  "employee_final": [
    "id_employee",
    "name",
    "surname",
    "cpf",
    "status",
    "role",
    "initial_date",
    "end_date",
    "store_id"
  ],
  "sku_cost": [
    "cod_prod",
    "data_inicio",
    "data_fim",
    "custo"
  ],
  "sku_dataset": [
    "cod_prod",	
    "nome_abrev",
    "nome_completo",
    "descricao",	
    "categoria",	
    "sub_categoria",	
    "marca",	
    "conteudo_valor",	
    "conteudo_medida"
  ],
  "sku_price": [
    "cod_prod",	
    "data_inicio",	
    "data_fim",
    "preco"
  ],
  "sku_status_dataset": [
    "cod_prod",
    "data_inicio",	
    "data_fim"
  ],
  "store_final": [
    "nome_loja",
    "regiao",
    "diretoria",
    "data_inauguracao"
  ],
  "target_store_final": [
    "month",
    "store_id",
    "sales_target"
  ],
  "target_salesperson_final": [
    "id_employee",
    "sales_target",
    "month"
  ],
  "year": [
    "data",
    "cod_vendedor",
    "cod_loja",
    "cod_transacao",
    "quantidade",
    "cod_prod",
    "preco"
  ]
}

@task
def prepare_dataframe_for_insert(filename, df):
  df['date_ingestion'] = datetime.now()
  df['data_row'] = df.apply(lambda row: row.to_json(), axis=1)
  df['tag'] = remove_file_pattern(filename).replace(".parquet", "")
  
  return df[['date_ingestion', 'data_row', 'tag']]

# Convert csv file to parquet
@task
def convert_to_parquet(filename, temp_folder):
  if filename.endswith(".csv"):
    csv_path = os.path.join(temp_folder, filename)
    parquet_path = os.path.join(temp_folder, filename.replace(".csv", ".parquet"))
    df = pd.read_csv(csv_path)
    df.to_parquet(parquet_path, index=False)
    print(f"Convertido: {csv_path} -> {parquet_path}")

# Convert json file to parquet
@task   
def convert_to_other_type(filename, temp_folder):
  if filename.endswith(".csv"):
    csv_path = os.path.join(temp_folder, filename)
    json_path = os.path.join(temp_folder, filename.replace(".csv", ".json"))
    df = pd.read_csv(csv_path)
    df.to_json(json_path, index=False)
    print(f"Convertido: {csv_path} -> {json_path}")

@task
def remove_file_pattern(filename):
  pattern = r'(_\d{2}_\d{2}_\d{4}_\d{2}_\d{2}_\d{2})\.parquet$'
  filename = re.sub(pattern, '.parquet', filename)
  return filename

@task
def validate_file(filename, df):
  columns = df.columns
  filename = remove_file_pattern(filename)
  
  if '20' in filename:
    filename = 'year'

  for data in tables_columns:
    if data in filename:  
      
      for column in columns:
        if column not in tables_columns[data]:
          return False
      
  return True

@task
def validate_file_model(filename, df):
  
  if '20' in filename:
    filename = 'year'

  for data in tables_columns_model:
    if data in filename:  
      
      for row in df:        
        try:
          data.model_validate(row)
        except ValidationError as e:
          return False
    else:
      return False
    
  return True