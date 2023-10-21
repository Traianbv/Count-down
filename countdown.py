import threading
import time
from tkinter import *
from win10toast import ToastNotifier
from tkinter import messagebox

class CountDown():

    def __init__(self):
        self.window = Tk()
        self.window.geometry("430x250")
        self.window.config(pady=25, padx=50)
        self.window.title("Count Down Timer")

        self.title = Label(text="Enter time format in seconds ! ", font=("Helvetica, 15"))
        self.title.grid(columnspan=2, column=0, row=0, pady=15)

        self.entry_time = Entry(font=("Helvetica, 20"))
        self.entry_time.grid(columnspan=2, column=0, row=1)
        self.entry_time = Entry(font=("Helvetica, 20"))
        self.entry_time.grid(columnspan=2, column=0, row=1)
        self.entry_time = Entry(font=("Helvetica, 20"))
        self.entry_time.grid(columnspan=2, column=0, row=1)

        self.start_button = Button(text="Start", font=("Helvetica, 15"), padx=15, command=self.start)
        self.start_button.grid(column=0, row=2, pady=15)

        self.stop_button = Button(text="Stop", font=("Helvetica, 15"), padx=15, command=self.stop)
        self.stop_button.grid(column=1, row=2)

        self.label = Label(text="Timer: 00:00:00")
        self.label.grid(columnspan=2, column=0, row=3, pady=20)

        self.stop_loop = True

        self.window.mainloop()


    def start_threadin(self):
        t = threading.Thread(target=self.start)
        t.start()


    def start(self):
        self.stop_loop = False

        hours, minutes, seconds = 0, 0, 0
        time_split = self.entry_time.get().split(":")
        try:
            if len(time_split) == 3:
                hours = int(time_split[0])
                minutes = int(time_split[1])
                seconds = int(time_split[3])
            elif len(time_split) == 2:
                minutes = int(time_split[0])
                seconds = int(time_split[1])
            elif len(time_split) == 1:
                seconds = int(time_split[0])
        except Exception:
            messagebox.showinfo(title="Info", message="Invalid time format !")



        full_time = hours * 3600 + minutes * 60 + seconds

        while full_time > 0 and not self.stop_loop:
            full_time -= 1
            minutes, seconds = divmod(full_time, 60)
            hours, minutes = divmod(minutes, 60)

            self.label.config(text=f"Timer: {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.window.update()
            time.sleep(1)

        if not self.stop_loop:
            toast = ToastNotifier()
            toast.show_toast("Time Finish ")
            self.window.destroy()



    def stop(self):
        self.stop_loop = True
        self.label.config(text="Timer: 00:00:00")


CountDown()





