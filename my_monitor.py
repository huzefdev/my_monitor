import datetime
import time

# user log input
user_input = int(input("How many lines you want log:"))
# creates "monitor.txt" and write logs
with open("monitor.txt", "w") as f:
    for i in range(user_input):
        # adds timestamp into a log file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if (i % 5 == 0 and i % 3 == 0):
            level = "CRITICAL"
            msg = "System Overheating AND High Memory!"
        elif (i % 5 == 0):
            level = "WARN"
            msg = "System overheating!"
        elif (i % 3 == 0):
            level = "WARN"
            msg = "High memory usage detected!"
        else:
            level = "INFO"
            msg = "System operating nominal"
        # shows log all in "monitor.txt"
        f.write(f"[{timestamp}] {level} (line{i}) : {msg}\n")
        # Optional: Add a tiny delay so the timestamps actually change
        time.sleep(0.08)
print("Log generation Complete!")
