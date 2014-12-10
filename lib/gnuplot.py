import datetime
import re
import subprocess

def run(gnuplot_path, cwd):
  process = subprocess.Popen(['gnuplot', gnuplot_path], stdout=subprocess.PIPE, cwd=cwd)
  out, err = process.communicate()
  return out
