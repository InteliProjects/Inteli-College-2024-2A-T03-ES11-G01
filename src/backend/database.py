import clickhouse_connect
import os
from dotenv import load_dotenv

load_dotenv()

CLICKHOUSE_HOST = os.getenv('CLICKHOUSE_HOST')
CLICKHOUSE_PORT = os.getenv('CLICKHOUSE_PORT')

def get_clickhouse_client():
    client = clickhouse_connect.get_client(host=CLICKHOUSE_HOST, port=CLICKHOUSE_PORT)

    return client

def create_table_users() -> None:
    client = get_clickhouse_client()
    client.command('''
        CREATE TABLE IF NOT EXISTS users (
            email String,
            username String,
            password_hash String,
            is_seller Boolean,
            id_employee Int32
        ) ENGINE = MergeTree()
        ORDER BY username
    ''')