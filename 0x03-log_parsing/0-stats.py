#!/usr/bin/python3
"""
Script reads log lines from stdin, computes metrics, and prints statistics
based on the specified log format.
"""

import sys
import re


if __name__ == '__main__':

    total_size, lines_processed = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {i: 0 for i in codes}

    def print_statistics(stats: dict, total_size: int) -> None:
        """
        Print the aggregated statistics based on the accumulated status counts.

        Args:
        stats (dict): A dictionary containing counts of status codes.
        total_size (int): Total accumulated file size.

        Prints:
        The total file size and the count of each status code in the given
        dictionary.
        Status codes with a count greater than zero are displayed in
        ascending order.
        """
        print(f'File size: {total_size}')
        for i, j in sorted(stats.items()):
            if j:
                print(f'{i}: {j}')

    try:
        for line in sys.stdin:
            lines_processed += 1
            # Define a regular expression pattern for the expected input format
            pattern = re.compile(
                r'^\d{1,3}(?:\.\d{1,3}){3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
            )
            match = pattern.match(line.strip())

            # Skip lines that don't match the expected format
            try:
                if match:
                    status_code = match.group(1)
                    int(status_code)
                    file_size = int(match.group(2))
                    if status_code in stats:
                        stats[status_code] += 1
                    total_size += file_size
                else:
                    continue
            except BaseException:
                continue

            if lines_processed % 10 == 0:
                print_statistics(stats, total_size)
        print_statistics(stats, total_size)
    except KeyboardInterrupt:
        print_statistics(stats, total_size)
        raise
