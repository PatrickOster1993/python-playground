import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

temperatures = [12, 15, 14, 10, 9, 8, 11]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

mean_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)

root = tk.Tk()
root.title("Temperature Chart")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(weekdays, temperatures, marker='o', label="Temperature", color='blue')
ax.axhline(mean_temp, color='red', linestyle='--', label=f"Average ({mean_temp:.2f}°C)")

ax.set_xlabel("Weekdays")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Temperatures of the Week")
ax.legend()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()
