from pathlib import Path
import pandas as pd
import PySimpleGUI as sg
from docxtpl import DocxTemplate

document_path = Path(__file__).parent / "WashRecordTemplate.docx"
doc = DocxTemplate(document_path)

sg.theme('Dark Grey 13')

layout = [
    [sg.Text("Date (YYYYMMDD):"), sg.Input(key="TODAY_INPUT", do_not_clear=False)],
    [sg.Text("Initials:"), sg.Input(key="NAME", do_not_clear=False)],
    [sg.Text("Wash count:"), sg.Combo(['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'], size=(43,0), key="WASH_COUNT")],
    [sg.Text("Product:"), sg.Combo(['RW-0.003', 'RW-0.01', 'RW-0.03', 'RW3-0.06', 'RW4-0.2', 'RW4-0.4', 'RW4-1.0', 'ST-16RT2', 'Other', 'Multiple'], size=(43,0), key="PRODUCT_MODEL")],    
    [sg.Text("PCA, STA, Other or Multiple:"), sg.Combo(['PCA', 'Stator', 'Other', 'Multiple'], size=(43,0), key="PCA_STA")],
    [sg.Text("Batch number:"), sg.Input(key="BATCH_NUM", do_not_clear=False)],
    [sg.Text("Serial numbers for products washed:"), sg.Input(key="SERIAL_NUM", do_not_clear=False)],
    [sg.Text("Paste wash report here:"), sg.Multiline(key="PASTE_REPORT", size=(43,30), do_not_clear=False)],
    [sg.Button("Create Report"), sg.Exit()],
]

window = sg.Window("Wash Record Generator - Sinclair Interplanetary by Rocket Lab", layout, element_justification="right",)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Create Report":
        values = dict(values)
        values["DATE_NAME_NUM"] = '%s-%s-%s' % (values['TODAY_INPUT'],values['NAME'],values['WASH_COUNT'])
        doc.render(values)
        output_path = Path(__file__).parent / f"{values['TODAY_INPUT']}-{values['NAME']}-{values['WASH_COUNT']}.docx"
        doc.save(output_path)
        sg.popup("Record file saved!", f"File has been saved here: {output_path}",
        "Please do not forget to commit file to SVN")

window.close()