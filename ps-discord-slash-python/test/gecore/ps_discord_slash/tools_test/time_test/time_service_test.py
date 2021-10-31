from datetime import datetime
import unittest

from gecore.ps_discord_slash.tools.time.time_service import get_month_from_timestamp, move_5days_backward


class TimeServiceTest(unittest.TestCase):

    def test_get_month_from_timestamp(self):
        october = 10
        october_first_timestamp = 1633046400
        result = get_month_from_timestamp(october_first_timestamp)
        self.assertEqual(october, result.value[1])

    def test_move_5days_backward_returnfirst(self):
        october = 10
        oct_6_utc = 1633478400
        result = move_5days_backward(oct_6_utc)
        month = get_month_from_timestamp(result)
        oct_first = datetime.fromtimestamp(oct_6_utc).replace(day=1)
        self.assertEqual(october, month.value[1])
        self.assertEqual(oct_first.timestamp(), result)

    def test_move_5days_backward_returnfirstondiff(self):
        october = 10
        oct_4_utc = 1633305600
        result = move_5days_backward(oct_4_utc)
        month = get_month_from_timestamp(result)
        oct_first = datetime.fromtimestamp(oct_4_utc).replace(day=1)
        self.assertEqual(october, month.value[1])
        self.assertEqual(oct_first.timestamp(), result)