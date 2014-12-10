import signal
import sys
import time

def handle_signal(_signo, _stack_frame):
  sys.exit(0)

def register_signals(_handler):
  signal.signal(signal.SIGTERM, _handler)
  signal.signal(signal.SIGINT, _handler)

def run(loop, delay = 1.0):
  register_signals(handle_signal)

  while True:
    loop()
    time.sleep(delay)
