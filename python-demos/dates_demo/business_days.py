""" business days module """
import datetime
import holidays

def business_days() -> list[datetime.date]:
    start_date = datetime.date(2021, 5, 1)
    end_date = datetime.date(2021, 6, 1)
    us_holidays = holidays.US()
    delta = end_date - start_date
    
    print("For start date", start_date, "and end date", end_date)
    print("The delta is", delta)
    print("The business days are:")

    for i in range(delta.days + 1):
        day = start_date + datetime.timedelta(days=i)
        if day not in us_holidays and day.weekday() not in [5,6]:
            print(day)

business_days()
