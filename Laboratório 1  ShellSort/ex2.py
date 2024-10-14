from shellsort import *
import datetime
import os, platform, subprocess, re

def get_processor_name():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command ="sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).decode().strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub( ".*model name.*:", "", line,1)
    return ""


with open('Laboratório 1  ShellSort/entrada1.txt', 'r') as f:
    processor = get_processor_name()
    for line in f:
        arr = line.split()
        arr = list(map(lambda x: int(x), arr))
        n = arr.pop(0)

        for size in [100, 1000, 10000, 100000]:
            for sequence in ['SHELL', 'KNUTH', 'CIURA']:
                time_before = datetime.datetime.now()
                shell_sort(arr, n, sequence, False)
                time_after = datetime.datetime.now()
                milisseconds = (time_after-time_before).microseconds/1000
                print(f'{sequence},{size},{milisseconds},{processor}')            

