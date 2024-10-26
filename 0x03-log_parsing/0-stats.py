#!/usr/bin/python3
""" reads stdin line by line and computes metrics """
import sys
import re
import signal

# Signal handler for keyboard interruption
count = 0
status_report_dic = {}
total_file_size = 0


def signal_handler(sig, frame):
    printStats(total_file_size, status_report_dic)
    sys.exit(0)


# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)


def printStats(total_file_size, status_report_dic):
    """ print stats """
    print(f'File size: {total_file_size}')
    for key, value in dict(sorted(status_report_dic.items())).items():
        print(f'{key}: {value}')


try:
    for line in sys.stdin:
        pattern = r'(?:\d{1,3}(?:\.\d{1,3}){3}) - \[(?:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] ".*?" (\d+) (\d+)$'

        m = re.search(pattern, line.strip())
        if not m:
            continue
        status = m.group(1)
        try:
            int(status)
        except Exception:
            continue
        if status not in ['200', '301', '400', '401',
                          '403', '404', '405', '500']:
            continue
        file_size = m.group(2)
        try:
            int(file_size)
        except Exception:
            continue
        total_file_size = total_file_size + int(file_size)
        try:
            status_report_dic[status] = status_report_dic[status] + 1
        except KeyError:
            status_report_dic[status] = 1
        count += 1
        if count >= 10:
            count = 0
            printStats(total_file_size, status_report_dic)
except KeyboardInterrupt:
    print("Interruption------------")
    printStats(total_file_size, status_report_dic)
