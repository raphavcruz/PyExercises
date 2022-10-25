from struct import pack
import tkinter as tk
from tkinter import Widget, ttk
from PIL import ImageTk

bg_color = "#000000"

#Initialize app
root = tk.Tk()
root.title("Wash Record Generator - Sinclair Interplanetary by Rocket Lab")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=600, height= 800, bg=bg_color)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

frame2 = tk.Frame(root, width=600, height= 130, bg=bg_color)
frame2.grid(row=9, column=0)
frame2.pack_propagate(False)

#user_input
date_label = tk.Label(frame1, text="Date:", bg=bg_color, fg="white", font=("TkMenuFont", 12))
date_label.grid(row=0, column=0)
name_label = tk.Label(frame1, text="Initials:", bg=bg_color, fg="white", font=("TkMenuFont", 12))
name_label.grid(row=1, column=0)
wash_label = tk.Label(frame1, text="Wash Count:", bg=bg_color, fg="white", font=("TkMenuFont", 12))
wash_label.grid(row=2, column=0)
pcasta_label = tk.Label(frame1, text="Product:", bg=bg_color, fg="white", font=("TkMenuFont", 12))
pcasta_label.grid(row=3, column=0)
prod_label = tk.Label(frame1, text="PCA, STA, or Other:", bg=bg_color, fg="white", font=("TkMenuFont", 12))
prod_label.grid(row=4, column=0)
batch_label = tk.Label(frame1, text="Batch Number:", bg=bg_color, fg="white", font=("TkMenuFont", 12))
batch_label.grid(row=5, column=0)
serial_label = tk.Label(frame1, text="Serial # for products washed:", bg=bg_color, fg="white", font=("TkMenuFont", 12))
serial_label.grid(row=6, column=0)
report_label = tk.Label(frame1, text="Paste wash report here:", bg=bg_color, fg="white", font=("TkMenuFont", 12))
report_label.grid(row=7, column=0)

date_entry = tk.Entry(frame1)
date_entry.grid(row=0, column=1)
name_entry = tk.Entry(frame1)
name_entry.grid(row=1, column=1)
wash_spinbox = tk.Spinbox(frame1, values=["001", "002", "003", "004", "005", "006", "007", "008", "009"])
wash_spinbox.grid(row=2, column=1)
pcasta_combobox = ttk.Combobox(frame1, values=["RW-0.003", "RW-0.01","RW-0.03", "RW3-0.06", "RW4-0.2", "RW4-0.4", "RW4-1.0", "ST-16RT2", "Other", "Multiple"])
pcasta_combobox.grid(row=3, column=1)
prod_combobox = ttk.Combobox(frame1, values=["PCA", "Stator", "Other", "Multiple"])
prod_combobox.grid(row=4, column=1)
batch_entry = tk.Entry(frame1)
batch_entry.grid(row=5, column=1)
serial_entry = tk.Entry(frame1)
serial_entry.grid(row=6, column=1)
report_entry = tk.Entry(frame1)
report_entry.grid(row=7, column=1)

logo_img = ImageTk.PhotoImage(file="WashRecordsWithGUI/WashAppBottom.png")
logo_widget = tk.Label(frame2, image=logo_img, bg=bg_color)
logo_widget.image = logo_img
logo_widget.pack()

# run app
root.mainloop()