import pandas as pd
from sqlalchemy import create_engine
import time

# --- configs ---
USER = 'admin'
PASS = 'Dadosfera123'
HOST = 'dadosfera-bernardodb.cdce84egka8x.us-east-2.rds.amazonaws.com'
PORT = '3306'
DB_NAME = 'dadosfera_case'
ARQUIVO_CSV = 'products.csv' 
TABELA_DESTINO = 'products'

# creating connection engine
engine = create_engine(f'mysql+pymysql://{USER}:{PASS}@{HOST}:{PORT}/{DB_NAME}')

print(f"🚀 Iniciando leitura do arquivo: {ARQUIVO_CSV}")
start_time = time.time()

# rreading in (chunks) to avoid overloading the RAM.
chunk_size = 20000 
batch_no = 1

for chunk in pd.read_csv(ARQUIVO_CSV, chunksize=chunk_size):
    print(f"📦 Enviando lote {batch_no} ({len(chunk)} linhas)...")
    chunk.to_sql(TABELA_DESTINO, con=engine, if_exists='append' if batch_no > 1 else 'replace', index=False)
    batch_no += 1

end_time = time.time()
print(f"✅ Sucesso! Total de tempo: {round(end_time - start_time, 2)} segundos.")