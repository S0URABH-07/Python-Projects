import os
from datetime import datetime

class HistoryLogger:
    def __init__(self, log_path="data/generation_history.log"):
        self.log_path = log_path

        log_dir = os.path.dirname(self.log_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def log_entry(self, data_payload, file_name):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] SUCCESS: Rendered '{file_name}' | Link URL : \"{data_payload}\"\n"
        
        with open(self.log_path, "a", encoding="utf-8") as file:
            file.write(log_line)