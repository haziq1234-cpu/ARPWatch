from datetime import datetime

def log_alert(severity, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} | {severity} | {message}"

    print(entry)

    with open("arpwatch.log", "a") as file:
        file.write(entry + "\n")


log_alert("WARNING", "Test alert generated")
log_alert("HIGH", "Second test alert generated")
