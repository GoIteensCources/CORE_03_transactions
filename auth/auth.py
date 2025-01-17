from .hash_tool import hash_password, check_password


def register_user(user_db, username, password):
    if username in user_db:
        print("Цей логін уже використовується. Оберіть інший.")
    else:
        user_db[username] = hash_password(password)
        print(f"Користувача {username} успішно зареєстровано.")


def authenticate_user(user_db, username, password) -> bool:
    if username not in user_db:
        print("Не зареестрований користувач")
        return False
    
    if check_password(password, h_pass=user_db[username]):
        print(f"Welcome! {username}")
        return True
    
    else:
        print("Incorrect Password")
        return False
      
        
if __name__ == "__main__":
    
    user_db = {}
    
    register_user(user_db, "admin", password="admin")
    print(user_db)
    username = "admin"
    
    if not authenticate_user(user_db, username, password="admin"):
        exit(0)
        