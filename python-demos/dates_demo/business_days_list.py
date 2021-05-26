from datetime import timedelta, date
from collections.abc import Generator
import holidays

def business_days(sdate: date, edate: date) -> list[date]:
    """ business days using a list """

    days: list[str] = []
    us_holidays = holidays.UnitedStates()

    num_of_days = (edate - sdate).days + 1

    for day_num in range(num_of_days):
        the_date = sdate + timedelta(days=day_num)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            days.append(the_date)

    return days

if __name__ == "__main__":

    start_date = date(2021, 1, 1)
    end_date = date(2021, 3, 31)

    for business_day in business_days(start_date, end_date):
        print(business_day)
