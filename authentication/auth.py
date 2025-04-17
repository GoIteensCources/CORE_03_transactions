from .hash_tools import hash_password, check_password


def register_user(username: str, password: str, users_db: dict):
    if username in users_db:
        print("Цей логін уже використовується. Оберіть інший.")
    else:
        users_db[username] = hash_password(password)
        print(f"Користувача {username} успішно зареєстровано.")
        

def authenticate_user(username: str, password: str, users_db: dict):
    if username not in users_db.keys():
        print(" користувача не існує")
        return False
    if check_password(password, users_db[username]):
        print(f"Welcome! {username}")
        return True
    else:
        print("Пароль невірний")
        return False
