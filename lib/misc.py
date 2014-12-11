import datetime

def list_average(list):
  if len(list) > 0:
    return float(sum(list)) / float(len(list))
  else:
    return float('inf')

def floor_datetime(dt, mins = 1):
  return dt - datetime.timedelta(minutes=dt.minute % mins, seconds=dt.second, microseconds=dt.microsecond)

def round_datetime(dt, mins = 1):
  dt += datetime.timedelta(minutes=mins/2)
  dt -= datetime.timedelta(minutes=dt.minute % mins, seconds=dt.second, microseconds=dt.microsecond)
  return dt
