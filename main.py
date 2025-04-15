import hashlib

users_db = {"admin": '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'}   # {"login": "hash_passw"}

categories = ["Food", "Entertainment", "Transport"]

transactions = {
    1: {'amount': 400, 'category': 'Transport', 'date': '2024-11-06'},
    2: {'amount': 119, 'category': 'Food', 'date': '2024-12-08'},
    3: {'amount': 236, 'category': 'Entertainment', 'date': '2024-11-17'},
    4: {'amount': 230, 'category': 'Food', 'date': '2024-12-04'},
    5: {'amount': 275, 'category': 'Entertainment', 'date': '2024-12-21'},
    6: {'amount': 431, 'category': 'Transport', 'date': '2024-12-03'},
    7: {'amount': 464, 'category': 'Food', 'date': '2024-12-06'},
    8: {'amount': 224, 'category': 'Entertainment', 'date': '2024-11-27'},
    9: {'amount': 93, 'category': 'Food', 'date': '2024-12-30'},
    10: {'amount': 405, 'category': 'Food', 'date': '2024-12-05'}
}

# __auth____
def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(password:str, hash_passvord:str):
    return hash_password(password) == hash_passvord


def register_user(username, password):
    if username in users_db:
        print("Цей логін уже використовується. Оберіть інший.")
    else:
        users_db[username] = hash_password(password)
        print(f"Користувача {username} успішно зареєстровано.")
        

def authenticate_user(username, password):
    if username not in users_db.keys():
        print(" користувача не існує")
        return False
    if check_password(password, users_db[username]):
        print(f"Welcome! {username}")
        return True
    else:
        print("Пароль невірний")
        return False


# ___transactions______

# EGor
def create_transaction():
    try:
        next_id = max(transactions.keys()) + 1
    except ValueError: 
        next_id = 1

    amount = float(input("Введіть суму транзакції: "))
    category = input("Введіть категорію транзакції: ")
    date = input("Введіть дату транзакції (YYYY-MM-DD): ")

    transactions[next_id] = {'amount': amount, 'category': category, 'date': date}
    print(f"Транзакцію {next_id} успішно додано.")
    return transactions


# Kiryl
def edit_transaction(transaction_id:int,amount:int=None,  category:str = None, date:str=None):
    transaction_id = int(input("Введіть ID транзакції, яку хочете змінити: "))
    if transaction_id in transactions:
        print("Поточні дані:", transactions[transaction_id])
        amount = int(input("Нова сума: "))
        category = input("Нова категорія: ")
        date = input("Нова дата (рррр-мм-дд): ")
        
        transactions[transaction_id] = {
            'amount': amount,
            'category': category,
            'date': date
        }
        print(f"Транзакція {transaction_id} оновлена.")
    else:
        print("Транзакція з таким ID не знайдена.")

# Bogdan
def delete_transaction():...    


# Andriy
def show_transactions(transactions: dict): ... 

    
# Artem
def calc_total_expences_by_category(category:str) -> int:
    total = 0
    for transaction in transactions.values():
        if transaction['category'] == category:
            total += transaction['amount']
    return total


# mark
def calc_total_expences_by_period(start_date:str, end_date:str) -> int: ... 



    

if __name__ == "__main__":
    print("Вітаємо у доданку 'керування витратами'!!")    
    
    while 1:
        res = input("для реестраціі оберіть 1, для авторизації -- 0: ")
        if res == "1":
            print("PЕЕСТРАЦІЯ")
            username = input("Username: ")
            password = input("Password: ")
            register_user(username, password)
            print(users_db)
            
        else:
            print("Авторизація")
            username = input("Username: ")
            password = input("Password: ")
            if not authenticate_user(username, password):
                continue
            else:
                break
            
    print("\n --MENU--\n")
    print("1. Додати транзакцію")
    print("2. Редагувати транзакцію")
    print("3. Видалити транзакцію")
    print("4. Показати всі транзакції")
    print("5. Підрахувати витрати")
    print("6. Вийти")
    
    choise = input("Оберіть опцію: ")
    
    