import tkinter as tk
from datetime import datetime
import winsound

def set_alarm():
    alarm_time = alarm_entry.get()
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        alarm_datetime = datetime.now().replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
        now = datetime.now()
        time_difference = alarm_datetime - now
        if time_difference.total_seconds() <= 0:
            alarm_datetime = alarm_datetime.replace(day=alarm_datetime.day + 1)
            time_difference = alarm_datetime - now

        alarm_status.config(text=f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}")
        window.after(int(time_difference.total_seconds() * 1000), trigger_alarm)
    except Exception as e:
        alarm_status.config(text="Invalid time format")

def trigger_alarm():
    winsound.Beep(1000, 1000)
    alarm_status.config(text="Ringing!")

window = tk.Tk()
window.title("Alarm Clock")
window.config(width=500, height=500, padx=20, pady=20, bg="white")

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tk.PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)

alarm_label = tk.Label(text="Enter alarm time 24-Hour format (HH:MM) :", bg="white")
alarm_label.grid(row=0+1, column=0)

alarm_entry = tk.Entry(width=10, highlightthickness=2)
alarm_entry.grid(row=0+1, column=1)

set_alarm_button = tk.Button(text="Set Alarm", command=set_alarm, width=8)
set_alarm_button.grid(row=1+1, column=1)

alarm_status = tk.Label(text="Alarm Status: Alarm not set!", bg="white")
alarm_status.grid(row=2+1, column=0, columnspan=2)

window.mainloop()