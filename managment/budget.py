import datetime as dt


def set_monthly_budget(month:int, amount:int, wallet: dict): 
    try:
        year = dt.date.today().year
        month_key = str(dt.date(year=year, month=month, day=1))
    except ValueError as e:
        print("Uncorrect value 'month', must have 1 ... 12")
        return False
    else:
        wallet[month_key] = amount
        return True


def show_wallet(wallet: dict):
    if not wallet:
        print("Гаманець порожній.")
    for month, amount in wallet.items():        
        print(f"Budget on {month} = {amount}")
    

def edit_wallet(wallet: dict, month:int, amount:int):
    pass


if __name__ == "__main__":
    wallet = {"2024-12-01": 10000}
    set_monthly_budget(4, 20000, wallet)
    show_wallet(wallet)
