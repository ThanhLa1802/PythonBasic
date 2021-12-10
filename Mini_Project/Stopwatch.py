from tkinter import *
from datetime import datetime
import tkinter

counter = 61200
running = True

def counter_label(label):
    def count():
        if running:
            global counter
            if counter == 61200:
                display = "Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                print(tt)
                string = tt.strftime("%H:%M:%S")
                print(string)
                display = string 
            label['text'] = display
            label.after(1000, count)
            counter += 1
            print(counter)
    count()

def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
def Stop():
    global running
    running=False
    counter_label(label)
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'

def Reset(label):
    global counter
    counter = 61200
    if running == False:
        reset['state']='disabled'
        label['text']='Welcome!'
    else:
        label['text'] = 'Starting...'


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Stopwatch")
    # Fixing the window size.
    root.minsize(width=250, height=70)
    label = tkinter.Label(root, text="Welcome!", fg="black", font="SVN-Arial 30",)
    label.pack()
    f = tkinter.Frame(root)
    start = tkinter.Button(f, text='Start', width=6, command = lambda: Start(label))
    stop = tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop)
    reset = tkinter.Button(f, text='Reset',width=6, state='disabled', command = lambda:Reset(label))
    f.pack(anchor = 'center',pady=5)
    start.pack(side="left")
    stop.pack(side ="left")
    reset.pack(side="left")
    root.mainloop()