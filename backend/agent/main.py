import schedule
import time

from service import run

run()

schedule.every(30).seconds.do(run)

while True:

    schedule.run_pending()

    time.sleep(1)
