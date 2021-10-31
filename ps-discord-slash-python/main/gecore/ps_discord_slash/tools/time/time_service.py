from datetime import datetime, timedelta
import pytz
from dateutil.relativedelta import relativedelta

from gecore.ps_discord_slash.tools.time.time_variants import grab_month_variant_by_number, MonthVariant

one_hour_in_seconds = 3600
day_in_seconds = 86400
three_days = (day_in_seconds * 3)


def get_utc_day_from_timestamp(timestamp: int) -> int:
    current_date = datetime.fromtimestamp(timestamp, tz=pytz.utc)
    result = current_date.replace(hour=0, minute=0, second=0, microsecond=0)
    return int(result.timestamp())


def get_earlier_day(timestamp: int, days: int) -> int:
    previous_day = timestamp - (day_in_seconds * days)
    calibrated_day = get_utc_day_from_timestamp(previous_day)
    return calibrated_day


def get_current_time() -> int:
    return int(datetime.now(tz=pytz.utc).timestamp())


def get_month_from_timestamp(timestamp: int) -> MonthVariant:
    utc_datetime = datetime.fromtimestamp(timestamp, tz=pytz.utc)
    return grab_month_variant_by_number(utc_datetime.month)


def check_if_before_pst_midnight(timestamp: int) -> bool:
    utc_datetime = datetime.fromtimestamp(timestamp, tz=pytz.utc)
    if utc_datetime.hour < 7:
        return True
    else:
        return False


def move_to_next_month(starting_day: int) -> int:
    ref_date = datetime.fromtimestamp(starting_day, tz=pytz.utc)
    if ref_date.month == 12:
        year = ref_date.year + 1
        jan_first = datetime.fromisocalendar(day=1, year=year, week=1)
        return int(jan_first.timestamp())
    else:
        next_month = ref_date + relativedelta(months=+1)
        next_month = next_month.replace(day=1)
        return int(next_month.timestamp())


def move_back_a_month(starting_day: int) -> int:
    ref_date = datetime.fromtimestamp(starting_day, tz=pytz.utc)
    if ref_date.month == 12:
        previous_month = ref_date + relativedelta(months=-1)
        dec_first = previous_month.replace(day=1)
        return int(dec_first.timestamp())
    else:
        previous_month = ref_date + relativedelta(months=-1)
        previous_month = previous_month.replace(day=1)
        return int(previous_month.timestamp())


def can_move_5days_forward(starting_day: int) -> bool:
    ref_date = datetime.fromtimestamp(starting_day, tz=pytz.utc)
    twenty_days_end = ref_date + timedelta(days=19)
    return ref_date.month == twenty_days_end.month


def move_5days_backward(starting_day: int) -> int:
    ref_date = datetime.fromtimestamp(starting_day, tz=pytz.utc)
    minus_5_days = ref_date - timedelta(days=5)
    if ref_date.month == minus_5_days.month:
        return int(minus_5_days.timestamp())
    else:
        return int(ref_date.replace(day=1).timestamp())


def get_twenty_days(starting_day: int) -> dict:
    day_list: dict = {}
    ref_date = datetime.fromtimestamp(starting_day, tz=pytz.utc)
    for day in range(20):
        new_ref_date = ref_date + timedelta(days=day)
        if new_ref_date.day >= ref_date.day:
            day_list[new_ref_date.day] = int(new_ref_date.timestamp())
        else:
            break
    return day_list
    # we're making a dictionary of days + time. Because the custom id needs the timestamp instead of the day.