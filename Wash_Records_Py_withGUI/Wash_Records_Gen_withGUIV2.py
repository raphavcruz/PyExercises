from pathlib import Path
import pandas as pd
import PySimpleGUI as sg
from docxtpl import DocxTemplate

document_path = Path(__file__).parent / "WashRecordTemplate.docx"
doc = DocxTemplate(document_path)

sg.change_look_and_feel('Dark Grey 13')

frame_layout = [
[sg.Checkbox('On', change_submits = True, enable_events=True, default='0',key='print_output')],
[sg.Listbox(values=[1,2,3], background_color='gray', disabled = False, key='_printer_pref_', size=(60, 6))],
]

layout = [
    [sg.Text("Date (YYYYMMDD):"), sg.Input(key="TODAY_INPUT", do_not_clear=False)],
    [sg.Text("Initials:"), sg.Input(key="NAME", do_not_clear=False)],
    [sg.Text("Wash count:"), sg.Input(key="WASH_COUNT", do_not_clear=False)],
    [sg.Text("Product:"), sg.Input(key="PRODUCT_MODEL", do_not_clear=False)],
    [sg.Checkbox("PCA", key="PCA_A"), sg.Checkbox("Stator", key="STA_A"), sg.Text("Other"), sg.Input(size=(19,0), key="OTHER_A", do_not_clear=False)],
    [sg.Text("Batch number:"), sg.Input(key="BATCH_NUMBER", do_not_clear=False)],
    [sg.Text("Serial numbers for products washed:"), sg.Input(key="SERIAL_NUM", do_not_clear=False)],
    [sg.Text("Program number:"), sg.Input(key="PROGRAM_NUM", do_not_clear=False)],
    [sg.Text("Paste wash report here:"), sg.Input(key="PASTE_REPORT", do_not_clear=False)],
    [sg.Button("Create Record"), sg.Exit()],
]

def Init(self):
    pca = self.values["pca"]
    sta = self.values["sta"]
    doc.render(values)

window = sg.Window("Wash Record Generator", layout, element_justification="right")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Create Record":
        values = dict(values)
        #['wwaasshh']/ f"{values['TODAY_INPUT']}-{values['NAME']}-{values['WASH_COUNT']}"
        #["DATE_NAME_NUM"] = {values['TODAY_INPUT']}-{values['NAME']}-{values['WASH_COUNT']}
        doc.render(dict(values))
        output_path = Path(__file__).parent / f"{values['TODAY_INPUT']}-{values['NAME']}-{values['WASH_COUNT']}.docx"
        #["DATE_NAME_NUM"] / f"{values['TODAY_INPUT']}-{values['NAME']}-{values['WASH_COUNT']}"
        doc.save(output_path)
        sg.popup("Record file saved!", f"File has been saved here: {output_path}",
        "Please do not forget to commit file to SVN")

window.close()