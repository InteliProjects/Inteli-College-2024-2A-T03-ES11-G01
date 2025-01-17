import bcrypt

def hash_password(password: str) -> bytes:
    # generate new password hash
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def check_password(password: str, hashed: bytes) -> bool:
    if isinstance(hashed, str):
        hashed = hashed.encode('utf-8')

    return bcrypt.checkpw(password.encode('utf-8'), hashed)
