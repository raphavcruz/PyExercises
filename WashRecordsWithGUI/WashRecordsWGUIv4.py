from pathlib import Path
import pandas as pd
import PySimpleGUI as sg
from PySimpleGUI import *
from docxtpl import DocxTemplate
import os
#from tkinter import *
from datetime import datetime

document_path = Path(__file__).parent / "WashRecordTemplate.docx"
doc = DocxTemplate(document_path)

sg.theme('Dark Grey 13')

def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)



layout = [
    Text("Date:"),sg.Input(key="TODAY_INPUT", size=(33,0)), sg.CalendarButton('Calendar', target='_CALENDAR_', pad=None, font=('MS Sans Serif', 10, 'bold'), 
    key='_CALENDAR_', format=('%d %B, %Y')),
    Text("Initials:"), sg.Input(key="NAME", do_not_clear=False),
    Text("Wash count:"), sg.Combo(['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'], size=(43,0), key="WASH_COUNT"),
    Text("Product:"), sg.Combo(['RW-0.003', 'RW-0.01', 'RW-0.03', 'RW3-0.06', 'RW4-0.2', 'RW4-0.4', 'RW4-1.0', 'ST-16RT2', 'Other', 'Multiple'], size=(43,0), key="PRODUCT_MODEL"),    
    Text("PCA, STA, Other or Multiple:"), sg.Combo(['PCA', 'Stator', 'Other', 'Multiple'], size=(43,0), key="PCA_STA"),
    Text("Batch number:"), sg.Input(key="BATCH_NUM", do_not_clear=False),
    Text("Serial numbers for products washed:"), sg.Input(key="SERIAL_NUM", do_not_clear=False),
    Text("Paste wash report here:"), sg.Multiline(key="PASTE_REPORT", size=(43,30), do_not_clear=False),
    Button("Create Report"), sg.Exit(),
    Input(key='-BROWSE-', enable_events=True, visible=False),
    Input(key='Save As', enable_events=True, visible=False),
    FileSaveAs(),
    Button('<'),
    Button('>')
]

window = sg.Window("Wash Record Generator - Sinclair Interplanetary by Rocket Lab", layout, element_justification="right")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Create Report":
       # values = dict(values)
       # values["DATE_NAME_NUM"] = '%s-%s-%s' % (values['TODAY_INPUT'],values['NAME'],values['WASH_COUNT'])
       # doc.render(values)
        #save_file_at_dir('new_dir/sub_dir', 'new_file.txt', 'new text')
        #output_path = Path(__file__).parentfile / f"{values['TODAY_INPUT']}-{values['NAME']}-{values['WASH_COUNT']}.docx"
        #doc.save(output_path)
        #sg.popup("Record file saved!", f"File has been saved here: {output_path}",
        #"Please do not forget to commit file to SVN")
        if event == "Calendar":
            window['_CALENDAR_']()
"""
sg.Popup('Title',
        'The results of the window.',
        'The button clicked was "{}"'.format(event),
        'The values are', values)
"""
window.close()