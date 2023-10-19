import sys
import subprocess
procs = []
for i in range(86):
    proc = subprocess.Popen([sys.executable, 'python.py', '{}in.csv'.format(i), '{}out.csv'.format(i)])
    procs.append(proc)
for proc in procs:
    proc.wait()
