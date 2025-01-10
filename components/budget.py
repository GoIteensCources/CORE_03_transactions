import datetime as dt


def set_mounth_budget(month: int, amount:int, wallet: dict) -> bool:
    try:
        year = dt.date.today().year
        month_key = str(dt.date(month=month, year=year, day=1))
    except ValueError as e:
        print("Помилка: номер місяця повинен бути в межах від 1 до 12. ")
        return False
    else:
        wallet[month_key] = amount
        print(f"Бюджет на {month_key} встановлено: {amount}.")
        return True


if __name__ == "__main__":
    wallet = {}
    set_mounth_budget(13, 10000, wallet)
    print(wallet)
    