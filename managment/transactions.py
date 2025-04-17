import datetime as dt


# Egor
def create_transaction( transactions:dict, amount: int, category: str, date: str=None)->dict:
    try:
        next_id = max(transactions.keys()) + 1
    except ValueError: 
        next_id = 1    
    else:
        curr_date = dt.date.today().strftime('%Y-%m-%d')
        transactions[next_id] = {'amount': amount, 
                                'category': category, 
                                'date': date if date else curr_date}
        return transactions[next_id]


# Kiryl
def edit_transaction( transactions:dict, transaction_id:int, amount:int=None,  category:str = None, date:str=None):
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


# Bogdan
def delete_transaction(transaction_id: int, transactions: dict) -> bool:
    if transaction_id in transactions:
        del transactions[transaction_id]
        return True  
    else:
        return False


# Andriy
def show_transactions(transactions: dict):
    print("Всі транзакції:")
    for tr_id, transaction in transactions.items():
        print(f"ID: {tr_id}, Сума: {transaction['amount']}, Категорія: {transaction['category']}, Дата: {transaction['date']}")

    
# Artem
def calc_total_expences_by_category(category:str, transactions:dict) -> int:
    total = 0
    for transaction in transactions.values():
        if transaction['category'] == category:
            total += transaction['amount']
    return total
