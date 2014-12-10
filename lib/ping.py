import datetime
import re
import subprocess

def ping(ip):
  def run_ping(ip, count, wait):
    process = subprocess.Popen(['ping', '-c%d' % count, '-W%d' % wait, ip], stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out

  def extract_packet_loss(ping_out):
    try:
      match = re.search('(\d+(\.\d+)?)% packet loss', ping_out, re.IGNORECASE)
      return float(match.group(1))
    except Exception, e:
      return None

  def extract_rounttrip_time(ping_out):
    try:
      match = re.search('(\d+(\.\d+)?)/(\d+(\.\d+)?)/(\d+(\.\d+)?)/(\d+(\.\d+)?)', ping_out, re.IGNORECASE)
      return (float(match.group(1)), float(match.group(3)), float(match.group(5)))
    except Exception, e:
      return (None, None, None)

  timestamp = datetime.datetime.now()
  ping_out = run_ping(ip, 1, 1.0)
  packet_loss = extract_packet_loss(ping_out)
  latency_min, latency_avg, latency_max = extract_rounttrip_time(ping_out)
  return (timestamp, ip, latency_avg)

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
