from lib.PerpetualTimer import *
try:
    from tkinter import *
    import tkinter.ttk as ttk
except ImportError:
    from Tkinter import *
    import ttk

t = None

def printer():
    print ('ipsem lorem')

def start_timer():
    global t
    t = PerpetualTimer(1,printer)
    t.start()

def stop_timer():
    global t
    if not t == None:
        t.cancel()

tk = Tk()

bt_start = Button(tk, text ="Start", command = start_timer)
bt_start.pack()

bt_stop = Button(tk, text ="Stop", command = stop_timer)
bt_stop.pack()

tk.mainloop()
t.cancel()
