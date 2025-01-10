import hashlib


def hash_password(data: str):
    return hashlib.sha256(data.encode()).hexdigest()

def check_password(password, h_pass) -> bool:
    return hash_password(password) == h_pass
