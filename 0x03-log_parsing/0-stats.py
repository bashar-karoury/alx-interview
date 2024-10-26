#!/usr/bin/python3
""" reads stdin line by line and computes metrics """
import sys
import re
count = 0
status_report_dic = {}
total_file_size = 0
try:
    for line in sys.stdin:
        pattern = r'(\d+)\s+(\d+)$'
        m = re.search(pattern, line)
        status = m.group(1)
        file_size = m.group(2)
        total_file_size = total_file_size + int(file_size)
        try:
            status_report_dic[status] = status_report_dic[status] + 1
        except KeyError:
            status_report_dic[status] = 1
        count += 1
        if count >= 10:
            count = 0
            print(f'File size: {total_file_size}')
            for key, value in dict(sorted(status_report_dic.items())).items():
                print(f'{key}: {value}')
except KeyboardInterrupt:
    print(f'File size: {total_file_size}')
    for key, value in dict(sorted(status_report_dic.items())).items():
        print(f'{key}: {value}')
