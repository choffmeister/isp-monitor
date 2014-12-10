import datetime
import os
import ping_lib
import sys

nullout = open(os.devnull, 'w')
original_stdout = sys.stdout

def ping(ip, timeout = 1000):
  sys.stdout = nullout
  timestamp = datetime.datetime.now()
  ping_obj = ping_lib.Ping(ip, timeout=timeout)
  latency = ping_obj.do()
  sys.stdout = original_stdout
  return (timestamp, ip, latency)

def to_csv_line(timestamp, ip, latency):
  return '%s;%s;%s\n' % (timestamp.strftime('%Y-%m-%d %H:%M:%S.%f'), ip, latency)

def from_csv_line(line):
  parts = line.split(';')
  timestamp = datetime.datetime.strptime(parts[0].strip(), '%Y-%m-%d %H:%M:%S.%f')
  ip = parts[1].strip()
  if parts[2].strip() != 'None':
    latency = float(parts[2].strip())
  else:
    latency = None
  return (timestamp, ip, latency)
