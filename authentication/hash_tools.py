import hashlib


def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(password:str, hash_passvord:str):
    return hash_password(password) == hash_passvord
