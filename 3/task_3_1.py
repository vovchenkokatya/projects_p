from datetime import datetime, timedelta

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        return (datetime.today() - date).days
    except ValueError:
        return "Wrong input!"

if __name__ == '__main__':
    date = "2007-11-15"
    date1 = "fghjk"
    print(get_days_from_today(date))
    print(get_days_from_today(date1))