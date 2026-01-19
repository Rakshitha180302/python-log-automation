import os
import sys
from datetime import datetime

LOG_FILE = "logs/system.log"
OUTPUT_FILE = "output/log_summary.txt"

def parse_logs(file_path):
    summary = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    try:
        with open(file_path, "r") as file:
            for line in file:
                for level in summary:
                    if line.startswith(level):
                        summary[level] += 1
    except Exception as e:
        print(f"Error reading log file: {e}")

    return summary

def write_summary(summary, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as file:
        file.write("System Log Automation Report\n")
        file.write("============================\n")
        file.write(f"Generated on: {datetime.now()}\n\n")
        for level, count in summary.items():
            file.write(f"{level}: {count}\n")

def main():
    if not os.path.exists(LOG_FILE):
        print("Log file not found.")
        return

    summary = parse_logs(LOG_FILE)
    write_summary(summary, OUTPUT_FILE)
    print("Log analysis completed successfully.")

if __name__ == "__main__":
    main()
