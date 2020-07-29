import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import main


root = tk.Tk()

root.title("Sysinfo")
root.geometry("800x600")
root.resizable(True, True)


#--- Interval ---
interval_label = ttk.Label(root, text="Plot-Interval in sec: ")
interval_label.pack(anchor=CENTER)

interval_scale = Scale(
    root,
    from_= 10,
    to = 60,
    length = 600,
    orient = "horizontal",
    resolution = 10,
)
interval_scale.pack(anchor=CENTER)



#--- Time ---
time_label = ttk.Label(root, text="Plot-Time in min: ")
time_label.pack(anchor=CENTER)

time_scale = Scale(
    root,
    from_= 1,
    to = 60,
    length = 600,
    orient = "horizontal",
    resolution = 1,
)
time_scale.pack(anchor=CENTER)


# --- Space for Plot-Soltution
plot_frame = Frame(root, background="White")
plot_frame.pack(fill="both", expand=1)




def graph():
    x = main.plot_time_x()
    y = main.plot_cpu_temp_y()
    fig = Figure()
    fig.add_subplot().plot(x,y)

    canvas = FigureCanvasTkAgg(fig, master=root)#f
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=1)


# ---Button ---
# ---Button/Frame
button_frame = Frame(root)
button_frame.pack(side=BOTTOM)


# --- Start-button : start ploting with selected paramerters ---
start_button = ttk.Button(button_frame, text="Start", command=graph)
start_button.grid(row=0, column=0, sticky="W")


# --- Cancel-button : stop process   /// imo second exit button
cancel_button = ttk.Button(button_frame, text="Cancel", command=root.destroy)
cancel_button.grid(row=0, column=1)

# --- Exit-button : close window
quit_button = ttk.Button(button_frame, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=2)


root.mainloop()
