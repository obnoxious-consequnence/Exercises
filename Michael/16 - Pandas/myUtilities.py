from datetime import datetime, timedelta, time
import numpy as np

def get_meeting_dates(period, time_of_day, frequency, start=datetime.now()):
    if frequency > period.days:
        raise ValueError("To many meetings!")
    day_deltas = np.linspace(0, period.days - 1, frequency, dtype=int)
    print("day_deltas", day_deltas)
    base_time_of_day = datetime.combine(start, time_of_day)
    print("base_time_of_day", base_time_of_day)
    list_of_meetings = [base_time_of_day + timedelta(int(day_delta)) for day_delta in day_deltas]
    return list_of_meetings
