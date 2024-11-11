# test_models.py
import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest import mock
from models import User

@mock.patch('models.get_clickhouse_client')
def test_insert_user(mock_get_client):
    mock_client = mock.Mock()
    mock_get_client.return_value = mock_client

    User.insert_user('test@example.com', 'testuser', 'hashed_password', True, 123)

    mock_client.insert.assert_called_once_with(
        'users',
        [['test@example.com', 'testuser', 'hashed_password', True, 123]],
        column_names=['email', 'username', 'password_hash', 'is_seller', 'id_employee']
    )

@mock.patch('models.get_clickhouse_client')
def test_get_user_by_email(mock_get_client):
    mock_client = mock.Mock()
    mock_get_client.return_value = mock_client

    mock_client.query.return_value.result_rows = [('test@example.com', 'testuser', 'hashed_password', True, 123)]

    result = User.get_user_by_email('test@example.com')

    assert result == [('test@example.com', 'testuser', 'hashed_password', True, 123)]
    mock_client.query.assert_called_once_with(
        'SELECT email, username, password_hash, is_seller, id_employee FROM users WHERE email = %(email)s',
        {'email': 'test@example.com'}
    )

@mock.patch('models.get_clickhouse_client')
def test_get_user_by_email_not_found(mock_get_client):
    mock_client = mock.Mock()
    mock_get_client.return_value = mock_client

    mock_client.query.return_value.result_rows = []

    result = User.get_user_by_email('unknown@example.com')

    assert result is None
    mock_client.query.assert_called_once_with(
        'SELECT email, username, password_hash, is_seller, id_employee FROM users WHERE email = %(email)s',
        {'email': 'unknown@example.com'}
    )
