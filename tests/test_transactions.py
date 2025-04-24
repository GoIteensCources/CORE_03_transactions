import datetime as dt
import pytest
from managment.transactions import create_transaction


@pytest.fixture
def transactions():
    return {
        1: {'amount': 400, 'category': 'Transport', 'date': '2024-11-06'},
        2: {'amount': 119, 'category': 'Food', 'date': '2024-12-08'}
    }


def test_create_transactions_with_date(transactions):    
    res = create_transaction(transactions=transactions, 
                             amount = 300, 
                             category = "Food", 
                             date="2025-03-12")
    new_key = max(transactions.keys())
        
    assert len(transactions) == 3
    assert transactions[new_key]["amount"] == 300
    assert transactions[new_key]["category"] == "Food"
    assert transactions[new_key]["date"] == "2025-03-12"
    
    
def test_create_transactions_without_date(transactions):
   
    res = create_transaction(transactions=transactions, 
                             amount = 300, 
                             category = "Food", 
                             )
    new_key = max(transactions.keys())
    
    assert len(transactions) == 3
    assert transactions[new_key]["amount"] == 300
    assert transactions[new_key]["category"] == "Food"
    assert transactions[new_key]["date"] == dt.date.today().strftime('%Y-%m-%d')