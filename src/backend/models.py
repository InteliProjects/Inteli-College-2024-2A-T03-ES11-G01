from database import get_clickhouse_client

class User:
    def __init__(self, email, username, password_hash, is_seller, id_employee):
        self.email = email
        self.username = username
        self.password_hash = password_hash
        self.is_seller = is_seller
        self.id_employee = id_employee

    @staticmethod
    def insert_user(email: str, username: str, hashed_password: str, is_seller: bool, id_employee: int) -> None:
        client = get_clickhouse_client()

        row = [email, username, hashed_password, is_seller, id_employee]
        data = [row]
        client.insert('users', data, column_names=['email', 'username', 'password_hash', 'is_seller', 'id_employee'])

    @staticmethod
    def get_user_by_email(email: str) -> list | None:
        client = get_clickhouse_client()

        query = 'SELECT email, username, password_hash, is_seller, id_employee FROM users WHERE email = %(email)s'
        
        result = client.query(query, {'email': email})
    
        user_data = result.result_rows

        if len(user_data) == 0:
            return None

        return user_data