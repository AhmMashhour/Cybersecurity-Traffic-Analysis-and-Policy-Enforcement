import os

log_path = "C:\\Windows\\System32\\winevt\\Logs"
for log_file in os.listdir(log_path):
    with open(os.path.join(log_path, log_file), 'r') as f:
        print(f.read())
