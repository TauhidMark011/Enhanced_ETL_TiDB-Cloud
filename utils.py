# Contains helper functions such as logging for tracking the ETL process.
from datetime import datetime

def log(message):
    # This function records logs with timestamps in a text file.
    with open("log_file.txt", "a", encoding="utf-8") as log_file:  #to record the logs, Open the log file in append mode
        log_file.write(f"{datetime.now()} - {message}\n")