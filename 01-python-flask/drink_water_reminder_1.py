import time
from plyer import notification

# Function to send a desktop notification
def remind_drink_water():
    notification.notify(
        title="Drink Water Reminder",
        message="It's time to drink a glass of water!\nHappy coding & Stay hydrated.",
        app_name="Water Reminder",
        timeout=5  # Notification duration (in seconds)
    )

# Main loop to run the reminder every 1 hour
while True:
    remind_drink_water()
    time.sleep(3600)  # Wait for 1 hour (3600 seconds) before sending the next reminder
