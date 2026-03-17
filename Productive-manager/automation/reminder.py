import schedule
import time
import sqlite3
from datetime import date

def check_deadline():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()

    today = str(date.today)
    c.execute("SELECT name,deadline FROM tasks")
    tasks = c.fetchall()

    for task in tasks:
        if task[1] == today:
            print("Reminder: Task due today -> ",task[0])
    conn.close()

schedule.every().day.at("09:00").do(check_deadline)

while True:
    schedule.run_pending()
    time.sleep(60)