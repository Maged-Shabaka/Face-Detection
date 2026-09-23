import psutil
import time
from winotify import Notification

notified = False

while True:
    battery = psutil.sensors_battery()

    if battery is None:
        print("Battery information not available.")
        break
    percent = battery.percent
    plugged = battery.power_plugged

    print(f"Battery: {percent}% | Charger: {plugged}")

    if percent <= 30 and not plugged:

        if not notified:
            msg=f"Battery is at {percent}%. Please plug in your charger."
            print(msg)

            notification = Notification(
                app_id="Battery Alert",
                title="Battery Low", 
                msg=msg, 
                duration="short") 

            notification.show()
            notified = True

        else:
            notified = False

        time.sleep(60) 