import time
from plyer import notification

while True:
  notification.notify(title="PLease drink water!!",
                      message="It's been an hour, please drink a glass of water",
                      )
  time.sleep(60*60)
