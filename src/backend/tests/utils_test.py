# test_utils.py

import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import hash_password, check_password
import bcrypt


def test_hash_password():
    password = 'mysecretpassword'
    hashed = hash_password(password)

    assert isinstance(hashed, bytes)
    assert bcrypt.checkpw(password.encode('utf-8'), hashed)

def test_check_password():
    password = 'mysecretpassword'
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    assert check_password(password, hashed) == True
    assert check_password('wrongpassword', hashed) == False

def test_check_password_with_str_hashed():
    password = 'mysecretpassword'
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    assert check_password(password, hashed) == True
    assert check_password('wrongpassword', hashed) == False
