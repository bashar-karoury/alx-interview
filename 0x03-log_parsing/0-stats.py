#!/usr/bin/python3
""" reads stdin line by line and computes metrics """
import sys
import re


def printStats(total_file_size, status_report_dic):
    """ print stats """
    print(f'File size: {total_file_size}')
    for key, value in dict(sorted(status_report_dic.items())).items():
        print(f'{key}: {value}')


count = 0
status_report_dic = {}
total_file_size = 0
try:
    for line in sys.stdin:
        pattern = r'(?:\d{1,3}(?:\.\d{1,3}){3}) - \[(?:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] ".*?" (\d+) (\d+)$'

        m = re.search(pattern, line)
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
    printStats(total_file_size, status_report_dic)
    raise
