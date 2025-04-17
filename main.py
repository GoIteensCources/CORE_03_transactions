from authentication import register_user, authenticate_user
from database import users_db, transactions, categories, wallet
from managment.transactions import *
from managment.budget  import *
from log_sett import log
from managment.reports import generate_monthly_report


def auth():
    while 1:
        res = input("для реестраціі оберіть 1, для авторизації -- 0: ")
        if res == "1":
            print("PЕЕСТРАЦIЯ")
            username = input("Username: ")
            password = input("Password: ")
            register_user(username, password, users_db)
            print(users_db)
            
        else:
            print("Авторизація")
            username = input("Username: ")
            password = input("Password: ")
            if not authenticate_user(username, password, users_db):
                continue
            else:
                log.info("AUTH ok")
                break


def interface_budget():
    while 1:                
        print("\n --MENU--\n")
        print("1. Додати бюджет на місяць")
        print("2. відобразити гаманець")
        print("3. Змінити гаманець")
        
        choise = input("Оберіть опцію: ")
        
        if choise == "1":
            show_wallet(wallet)
        
        elif choise == "2":            
            set_monthly_budget(wallet = wallet,
                               month = int(input("Mounth: ")),
                               amount = int(input("amount: ")),)
        elif choise == "3":
            edit_wallet
            

if __name__ == "__main__":

    log.info("Вітаємо у доданку 'керування витратами'!!")    
    
    auth()
    
    while 1:             
        print("\n --MENU--\n")
        print("1. Додати транзакцію")
        print("2. Редагувати транзакцію")
        print("3. Видалити транзакцію")
        print("4. Показати всі транзакції")
        print("5. Підрахувати загальні витрати")  # поки не реалізовано
        print("6. Підрахувати витрати за категорією") 
        print("7. Гаманець")
        print("8. Створити звіт")
        print("9. Вийти")
        
        choise = input("Оберіть опцію: ")
        
        if choise == "1":
            
            amount = float(input("Введіть суму транзакції: "))
            category = input("Введіть категорію транзакції: ")
            date = input("Введіть дату транзакції (YYYY-MM-DD) / пустий для поточної дати : ")
            
            if create_transaction(transactions, amount, category, date):
                show_transactions(transactions)
            else:
                 print("не вдалося створити транзакцію")
        
        elif choise == "2":
            transaction_id = int(input("Введіть ID транзакції: "))
            
            print("Поточні дані:", transactions[transaction_id])
            
            amount = input("Нова сума (залиште порожнім, щоб не змінювати): ")
            category = input("Нова категорія (залиште порожнім, щоб не змінювати): ")
            date = input("Нова дата (залиште порожнім, щоб не змінювати): ")
            edit_transaction(0)
        
        elif choise == "3":
            if delete_transaction():
                print("транзакція видаленна")
        
        elif choise == "4":
            show_transactions(transactions)
        
        elif choise == "5":
            print("Функція ще не реалізована.")  
        
        elif choise == "6":
            category = input("Введіть категорію (Food / Entertainment / Transport): ")
            total = calc_total_expences_by_category(category)
            print(f"Загальні витрати в категорії '{category}': {total}")
        
        elif choise == "7":
            interface_budget()    
            
        elif choise == "8":
            print("введіть рік та місяць за який бажаєте отримати звіт:")
            year = int(input("Pік: "))
            month = int(input("Місяць: "))
            report = generate_monthly_report(transactions, wallet, year, month)        
            if report:
                print("Звіт створено.")
                
        elif choise == "9":
            print("До побачення!")
            exit()
        else:
            print("Невірна опція. Спробуйте ще раз.")
    