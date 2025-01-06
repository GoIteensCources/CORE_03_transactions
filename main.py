import hashlib
import datetime as dt


categories = ["Food", "Entertainment", "Transport"]

transactions = {
    1: {'amount': 400, 'category': 'Transport', 'date': '2023-11-06'},
    2: {'amount': 119, 'category': 'Food', 'date': '2023-12-08'},
    3: {'amount': 236, 'category': 'Entertainment', 'date': '2023-11-17'},
    4: {'amount': 230, 'category': 'Food', 'date': '2023-12-04'},
    5: {'amount': 275, 'category': 'Entertainment', 'date': '2023-12-21'},
    6: {'amount': 431, 'category': 'Transport', 'date': '2023-12-03'},
    7: {'amount': 464, 'category': 'Food', 'date': '2023-12-06'},
    8: {'amount': 224, 'category': 'Entertainment', 'date': '2023-11-27'},
    9: {'amount': 93, 'category': 'Food', 'date': '2023-12-30'},
    10: {'amount': 405, 'category': 'Food', 'date': '2023-12-05'},
    
}



def hash_password(data: str):
    return hashlib.sha256(data.encode()).hexdigest()

def check_password(password, h_pass) -> bool:
    return hash_password(password) == h_pass


user_db = {"user": hash_password("user")}  # {"username": "hash_password"}



def register_user(username, password):
    if username in user_db:
        print("Цей логін уже використовується. Оберіть інший.")
    else:
        user_db[username] = hash_password(password)
        print(f"Користувача {username} успішно зареєстровано.")


def authenticate_user(username, password) -> bool:
    if username not in user_db:
        print("Не зареестрований користувач")
        return False
    if check_password(password, h_pass=user_db[username]):
        print(f"Welcome! {username}")
        return True
    else:
        print("Incorrect Password")
        return False
        
   
   
def add_transaction(amount:int, category:str, date = None):
    max_key = max(transactions.keys())
    new_key = max_key + 1
    
    # "check date
    # dt.date.fromtimestamp(date)"
    
    
    curr_date = dt.date.today().strftime('%Y-%m-%d')

    transactions[new_key] = {
        'amount': amount,
        'category': category,
        'date': date if date else curr_date
    }

    print(transactions)
    

def edit_transaction(transaction_id: int, amount=None, date=None, category=None):
    if transaction_id in transactions:
        if amount is not None:
            transactions[transaction_id]["amount"] = amount

        if date is not None:
            transactions[transaction_id]["date"] = date

        if category is not None:
            transactions[transaction_id]["category"] = category
        
        print("Змінено {transaction_id}")        
    else:
        print(f"Не існує такої транзакції = {transaction_id}")

        
def delete_transaction(transactions_id:int):
    transactions.pop(transactions_id)


def show_transactions():
    ...


# ------ show info --------------------

def calculate_total(category=None):
    res = None
    res1 = None
    res2 = None
    if category in transactions == "Food":
        res = total[category]
        print(f"Витрати на їжу: {res}")
    elif category in transactions == "Entertainment":
        res1 = total[category]
        print(f"Витрати на розваги: {res1}")
    elif category in transactions == "Transport":
        res2 = total[category]
        print(f"Витрати на транспорт: {res2}")
 
 
if __name__ == "__main__":
    
    register_user("admin", password="admin")
    print(user_db)
    
    username = input("Enter username: ")
    password = input("Enter Password: ")
    
    if not authenticate_user(username, password):
        exit(0)
    
    while True:
        print("\n ---- MENU ----")
        print("1. Додати транзакцію")
        print("2. Редагувати транзакцію")
        print("3. Видалити транзакцію")
        print("4. Показати всі транзакції")
        print("5. Підрахувати витрати")
        print("0. Вийти")    
        
        choise = input("Оберіть дію: ")
                
        if choise == "1":
            amount = int(input("Введіть суму: "))
            category = input(f"Введіть категорію {category}: ")
            add_transaction(amount, category)
            
        elif choise == "2":
            transaction_id = int(input("Введіть ID транзакції: "))
            amount = input("Нова сума (залиште порожнім, щоб не змінювати): ")
            category = input("Нова категорія (залиште порожнім, щоб не змінювати): ")
            date = input("Нова дата (залиште порожнім, щоб не змінювати): ")
            edit_transaction(transaction_id,
                             amount=int(amount) if amount else None,
                             date=date if date else None,
                             category=category if category else None)
            
        elif choise == "3":
            transaction_id = int(input("Введіть ID транзакції: "))
            delete_transaction(transaction_id)
            
        elif choise == "4":
            show_transactions()
            
        elif choise == "5":
            category = input("Введіть категорію для підрахунку (або залиште порожнім для всіх): ")
            total = calculate_total(category if category else None)
            if category:
                print(f"Витрати по {category}: {total}")
            else:
                print(f"Загальні витрати: {total}")
            
        elif choise == "0":
            print(f"До побачення, {username}!!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")
            