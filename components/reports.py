import datetime as dt
from typing import Generator


def filter_transactions_by_month(transactions: dict, month:int, year:int) -> Generator:
    for transaction_id, details in transactions.items():
        if dt.datetime.fromisoformat(details['date']).year == year and dt.datetime.fromisoformat(details['date']).month == month:
            yield transaction_id, details
            

def generate_monthly_report(transactions: dict, wallet: dict, year: int, month: int) -> list[str]:
    """
    Генерує звіт про транзакції за вказаний місяць з урахуванням бюджету.
    
    :param transactions: Словарь с транзакциями.
    :param wallet: Словарь с бюджетами.
    :param year: Год.
    :param month: Месяц (1-12).
    :return: Список строк с отчетом.
    """
    report = []
    report.append(f"Отчет за {year}-{month:02d}:\n")
    
    month_key = f"{year}-{month:02d}-01"
    budget = wallet.get(month_key, 0)

    filtered_transactions = list(filter_transactions_by_month(transactions, month=month, year=year))
    total_expenses = sum(details['amount'] for _, details in filtered_transactions)
    
    for transaction_id, details in filtered_transactions:
        report.append(f"ID: {transaction_id}, Дата: {details['date']}, Категорія: {details['category']}, Сума: {details['amount']}\n")

    report.append("*"*25+"\n")
    report.append(f"Загальний бюджет: {budget}\n")
    report.append(f"Загальні витрати за місяць: {total_expenses}\n")
    report.append(f"Залишок бюджета: {budget - total_expenses}\n")

    return report



def create_report_file(report, filename):
    pass


if __name__ == "__main__":
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
    
    print(list(filter_transactions_by_month(transactions, 10, 2023)))