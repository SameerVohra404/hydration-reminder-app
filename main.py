import time
from plyer import notification

print("Hydration Reminder is RUNNING")
print("Close this window to stop.")
print("First reminder in 1 hour...")

try:
    while True:
        notification.notify(
            title="Hydration Reminder",
            message="Time to Drink Water",
            timeout=10
        )
        time.sleep(60 * 60)  # 1 hour
except Exception as e:
    print("Error:", e)
    input("Press Enter to close...")