#!/usr/bin/python3
""" reads stdin line by line and computes metrics """
import sys
import re
import signal

# Initialize counters
total_file_size = 0
status_code_counts = {code: 0 for code in [
    200, 301, 400, 401, 403, 404, 405, 500]}
count = 0

# Define a regular expression pattern for the expected input format
pattern = re.compile(
    r'^\d{1,3}(?:\.\d{1,3}){3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)

# Function to print the metrics


def print_metrics():
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

# Signal handler for keyboard interruption


def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)


# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

try:
    # Read each line from standard input
    for line in sys.stdin:
        match = pattern.match(line.strip())

        # Skip lines that don't match the expected format
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            # Update total file size and status code count
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            # Print metrics every 10 lines
            count += 1
            if count == 10:
                print_metrics()
                count = 0
except KeyboardInterrupt:
    # Handle keyboard interrupt and print final metrics
    print_metrics()
