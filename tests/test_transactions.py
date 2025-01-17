from components.transactions import add_transaction
import pytest
import datetime as dt


@pytest.fixture
def transactions():
    return {
        1: {'amount': 400, 'category': 'Transport', 'date': '2023-11-06'},
        2: {'amount': 119, 'category': 'Food', 'date': '2023-12-08'},
    }


def test_add_transaction(transactions):      
    add_transaction(transactions, amount=42, category="Transport")    
    new_key = max(transactions.keys())
    assert transactions[new_key]['amount'] == 42
    assert transactions[new_key]['category'] == "Transport"
    assert transactions[new_key]['date'] == dt.date.today().strftime('%Y-%m-%d')
    
    
@pytest.mark.skip    
def test_add_transaction_with_date(transactions):    
    add_transaction(transactions, amount=42, category="Transport", date="2024-12-08")    
    new_key = max(transactions.keys())
    assert transactions[new_key]['amount'] == 42
    assert transactions[new_key]['category'] == "Transport"
    assert transactions[new_key]['date'] == "2024-12-08"
