from auth.auth import register_user, authenticate_user
from components.reports import generate_monthly_report
from database import transactions, user_db, categories, wallet
from components.transactions import *
from components.budget import set_mounth_budget


if __name__ == "__main__":
    
    register_user(transactions, user_db, "admin", password="admin")
    print(user_db)
    
    # username = input("Enter username: ")
    # password = input("Enter Password: ")
    username = "admin"
    
    if not authenticate_user(transactions, user_db, username, password="admin"):
        exit(0)
    
    while True:
        print("\n ---- MENU ----")
        print("1. Додати транзакцію")
        print("2. Редагувати транзакцію")
        print("3. Видалити транзакцію")
        print("4. Показати всі транзакції")
        print("5. Підрахувати витрати")
        
        print("6. Додати бюджет")
        print("7. Створити звіт")
        print("0. Вийти")    
        
        choise = input("Оберіть дію: ")
                
        if choise == "1":
            amount = int(input("Введіть суму: "))
            category = input(f"Введіть категорію {categories}: ")
            add_transaction(transactions, amount, category)
            
        elif choise == "2":
            transaction_id = int(input("Введіть ID транзакції: "))
            amount = input("Нова сума (залиште порожнім, щоб не змінювати): ")
            category = input("Нова категорія (залиште порожнім, щоб не змінювати): ")
            date = input("Нова дата (залиште порожнім, щоб не змінювати): ")
            edit_transaction(
                transaction_id, 
                amount=int(amount) if amount else None, 
                date=date if date else None,
                category=category if category else None
                )
            
        elif choise == "3":
            transaction_id = int(input("Введіть ID транзакції: "))
            delete_transactions(transactions, transaction_id)
            
        elif choise == "4":
            show_transactions(transactions)
            
        elif choise == "5":
            category = input("Введіть категорію для підрахунку (або залиште порожнім для всіх): ")
            total = calculate_total(transactions, category if category else None)
            if category:
                print(f"Витрати по {category}: {total}")
            else:
                print(f"Загальні витрати: {total}")
        
        elif choise == "6":
            month = int(input("Month: "))
            amount = int(input("Amount: "))
            set_mounth_budget(month=month, amount=amount, wallet=wallet)            
        
        elif choise == "7":
                month = int(input("Введіть місяць: "))
                year = input("Введіть рік, або залиште порожнім шоб створити для поточного року: ")
                year = int(year) if year else dt.date.today().year
                
                report = generate_monthly_report(transactions, wallet, year=year, month=month)
    
                create_report_file(report, f"{year}-{month:02d}")
                
            
        elif choise == "0":
            print(f"До побачення, {username}!!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")
            