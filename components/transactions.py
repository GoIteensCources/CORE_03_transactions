import datetime as dt
import pprint as pp

   
def add_transaction(transactions, amount:int, category:str, date = None):
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
    

def edit_transaction(transactions, transaction_id: int, amount=None, date=None, category=None):
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

        
def delete_transactions(transactions, transactions_id:int):
    try:
        transactions.pop(transactions_id)
    except KeyError as ke:
        print(f"no such element exists: {ke}")
    else:
        print("item deleted successfully")


def show_transactions(transactions):
    pp.pprint(transactions)


# ------ show info --------------------

def calculate_total(transactions, category=None) -> int:
    total: int = 0
    for trans in transactions.values():
        if category is None or trans['category'] == category:
            total += trans['amount']
    return total
 