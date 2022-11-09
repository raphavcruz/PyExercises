import tkinter as tk
from tkinter import END, ttk
from tkinter.font import BOLD
from PIL import ImageTk
from tkcalendar import *

bg_color = "#000000"

def enter_data():

    Cal_Entry = date_entry_cal.get()
    NameEntry = name_entry.get()
    WashEntry = wash_spinbox.get()
    ProdEntry = prod_combobox.get()
    PCASTAEntry = pcasta_combobox.get()
    BatchEntry = batch_entry.get()
    SerialEntry = serial_entry.get()
    ReportEntry = report_entry.get(1.0, END)

    print(
    "Date:", Cal_Entry,", "
    "Initials:", NameEntry,", "
    "Wash Count:", WashEntry,", "
    "Product:", ProdEntry,", "
    "PCA, STA or Other:", PCASTAEntry,", "
    "Batch Number", BatchEntry,", "
    "Serial #s for products washed:", SerialEntry,", "
    "Wash Report:", ReportEntry,
    )

#Initialize app
gui = tk.Tk()
gui.title("Wash Record Generator - Sinclair Interplanetary by Rocket Lab")

#App placement on screen
#gui.eval("tk::PlaceWindow . left")
x = gui.winfo_screenwidth() // 2
y = int(gui.winfo_screenheight() * 0.1)
gui.geometry("600x850+" + str(x) + "+" + str(y))
gui.configure(bg=bg_color)

#Frames inside parent window (gui)
frame0 = tk.Frame(gui, width=600, height= 107, bg=bg_color, padx=0, pady=0)
frame0.pack()
frame0.pack_propagate(False)

frame1 = tk.Frame(gui, width=600, height= 800, bg=bg_color, padx=10, pady=10)
frame1.pack()
frame1.pack_propagate(False)

frame2 = tk.Frame(gui, width=600, height= 130, bg=bg_color, padx=0, pady=0)
frame2.pack()
frame2.pack_propagate(False)

frame3 = tk.Frame(gui, width=600, height= 150, bg=bg_color, padx=0, pady=0)
frame3.pack()
frame3.pack_propagate(False)

#paddying for all widgets inside frame1
for widget in frame1.winfo_children():
    widget.grid_configure(padx=5, pady=8)

#user_input, labels & entries
date_label = tk.Label(frame1, text="Date:", bg=bg_color, fg="white", font=("TkMenuFont", 11), anchor="e", width=19)
date_label.grid(row=0, column=0, padx=10, pady=1)
name_label = tk.Label(frame1, text="Initials:", bg=bg_color, fg="white", font=("TkMenuFont", 11), anchor="e", width=19)
name_label.grid(row=1, column=0, padx=10, pady=1)
wash_label = tk.Label(frame1, text="Wash Count:", bg=bg_color, fg="white", font=("TkMenuFont", 11), anchor="e", width=19)
wash_label.grid(row=2, column=0, padx=10, pady=1)
pcasta_label = tk.Label(frame1, text="Product:", bg=bg_color, fg="white", font=("TkMenuFont", 11), anchor="e", width=19)
pcasta_label.grid(row=3, column=0, padx=10, pady=1)
prod_label = tk.Label(frame1, text="PCA, STA, or Other:", bg=bg_color, fg="white", font=("TkMenuFont", 11), anchor="e", width=19)
prod_label.grid(row=4, column=0, padx=10, pady=1)
batch_label = tk.Label(frame1, text="Batch Number:", bg=bg_color, fg="white", font=("TkMenuFont", 11), anchor="e", width=19)
batch_label.grid(row=5, column=0, padx=10, pady=1)
serial_label = tk.Label(frame1, text="SNs for products washed:", bg=bg_color, fg="white", font=("TkMenuFont", 11), anchor="e", width=19)
serial_label.grid(row=6, column=0, padx=10, pady=1)
report_label = tk.Label(frame1, text="Paste wash report here:", bg=bg_color, fg="white", font=("TkMenuFont", 11), anchor="e", width=19)
report_label.grid(row=7, column=0, padx=10, pady=1)

date_entry_cal = DateEntry(frame1, width=57)
date_entry_cal.grid(row=0, column=1)
name_entry = tk.Entry(frame1, width=60)
name_entry.grid(row=1, column=1)
wash_spinbox = tk.Spinbox(frame1, width=58, values=["001", "002", "003", "004", "005", "006", "007", "008", "009"])
wash_spinbox.grid(row=2, column=1)
pcasta_combobox = ttk.Combobox(frame1, width=57, values=["RW-0.003", "RW-0.01","RW-0.03", "RW3-0.06", "RW4-0.2", "RW4-0.4", "RW4-1.0", "ST-16RT2", "Other", "Multiple"])
pcasta_combobox.grid(row=3, column=1)
prod_combobox = ttk.Combobox(frame1, width=57, values=["PCA", "Stator", "Other", "Multiple"])
prod_combobox.grid(row=4, column=1)
batch_entry = tk.Entry(frame1, width=60)
batch_entry.grid(row=5, column=1)
serial_entry = tk.Entry(frame1, width=60)
serial_entry.grid(row=6, column=1)
report_entry = tk.Text(frame1, width=45, height=25)
report_entry.grid(row=7, column=1, padx=10, pady=2)

#Button and banners
button = tk.Button(frame2, text="GENERATE REPORT", font=("TkHeadingFont", 12, BOLD), bg="#D72020", fg="#FFFFFF", cursor="hand2", activebackground="#DC143C", activeforeground="#FFFFFF", command=enter_data)
button.grid(row=15, column=0, sticky="news", padx=10, pady=10)

logo_img = ImageTk.PhotoImage(file="WashAppTop.png")
logo_widget = tk.Label(frame0, image=logo_img, bg=bg_color)
logo_widget.image = logo_img
logo_widget.pack()

logo_img = ImageTk.PhotoImage(file="WashAppBottom.png")
logo_widget = tk.Label(frame3, image=logo_img, bg=bg_color)
logo_widget.image = logo_img
logo_widget.pack()

gui.mainloop()