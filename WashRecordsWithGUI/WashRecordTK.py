import tkinter
from tkinter import *
from tkinter import filedialog

window = tkinter.Tk()
window.title("Wash Record Generator - Sinclair Interplanetary by Rocket Lab")

frame = tkinter.Frame(window)
frame.pack()


def enter_data():
    dataentry = date_entry.get()
    nameentry = name_entry.get()
    washentry = wash_spinbox.get()
    pcastaentry = pcasta_combobox.get()
    prodentry = prod_combobox.get()
    batchentry = batch_entry.get()
    serialentry = serial_entry.get()
    reportentry = report_entry.get()

    #print("Today:", dataentry, "Product: ", prodentry)

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.docx')
    #filedata = str

#User input frame
user_info_frame = tkinter.LabelFrame(frame)
user_info_frame.grid(row= 0, column= 0, sticky="news", padx=10, pady=10)

#User info
date_label = tkinter.Label(user_info_frame, text="Date:")
date_label.grid(row=0, column=0)
name_label = tkinter.Label(user_info_frame, text="Initials:")
name_label.grid(row=1, column=0)
wash_label = tkinter.Label(user_info_frame, text="Wash Count:")
wash_label.grid(row=2, column=0)
pcasta_label = tkinter.Label(user_info_frame, text="Product:")
pcasta_label.grid(row=3, column=0)
prod_label = tkinter.Label(user_info_frame, text="PCA, STA, or Other:")
prod_label.grid(row=4, column=0)
batch_label = tkinter.Label(user_info_frame, text="Batch Number:")
batch_label.grid(row=5, column=0)
serial_label = tkinter.Label(user_info_frame, text="Serial # for products washed:")
serial_label.grid(row=6, column=0)
report_label = tkinter.Label(user_info_frame, text="Paste wash report here:")
report_label.grid(row=7, column=0)

date_entry = tkinter.Entry(user_info_frame)
date_entry.grid(row=0, column=1)
name_entry = tkinter.Entry(user_info_frame)
name_entry.grid(row=1, column=1)
wash_spinbox = tkinter.Spinbox(user_info_frame, values=["001", "002", "003", "004", "005", "006", "007", "008", "009"])
wash_spinbox.grid(row=2, column=1)
pcasta_combobox = ttk.Combobox(user_info_frame, values=["RW-0.003", "RW-0.01","RW-0.03", "RW3-0.06", "RW4-0.2", "RW4-0.4", "RW4-1.0", "ST-16RT2", "Other", "Multiple"])
pcasta_combobox.grid(row=3, column=1)
prod_combobox = ttk.Combobox(user_info_frame, values=["PCA", "Stator", "Other", "Multiple"])
prod_combobox.grid(row=4, column=1)
batch_entry = tkinter.Entry(user_info_frame)
batch_entry.grid(row=5, column=1)
serial_entry = tkinter.Entry(user_info_frame)
serial_entry.grid(row=6, column=1)
report_entry = tkinter.Entry(user_info_frame)
report_entry.grid(row=7, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5, )

button = tkinter.Button(frame, text="Generate Report", command= enter_data, saveFile)
button.pack()
button.grid(row=3, column=0, sticky="news", padx=10, pady=10)



window.mainloop()