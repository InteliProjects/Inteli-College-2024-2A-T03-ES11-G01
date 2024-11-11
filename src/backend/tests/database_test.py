# test_database.py
import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest import mock
from database import get_clickhouse_client, create_table_users

@mock.patch('database.clickhouse_connect.get_client')
def test_get_clickhouse_client(mock_get_client):
    mock_client = mock.Mock()
    mock_get_client.return_value = mock_client

    client = get_clickhouse_client()
    
    assert client == mock_client
    mock_get_client.assert_called_once_with(host=mock.ANY, port=mock.ANY, user=mock.ANY, password=mock.ANY)

@mock.patch('database.get_clickhouse_client')
def test_create_table_users(mock_get_client):
    mock_client = mock.Mock()
    mock_get_client.return_value = mock_client

    create_table_users()

    mock_client.command.assert_called_once_with('''
        CREATE TABLE IF NOT EXISTS users (
            email String,
            username String,
            password_hash String,
            is_seller Boolean,
            id_employee Int32
        ) ENGINE = MergeTree()
        ORDER BY username
    ''')
