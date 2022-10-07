from pathlib import Path

import PySimpleGUI as sg
from docxtpl import DocxTemplate

document_path = Path(__file__).parent / "WashRecordTemplate.docx"
doc = DocxTemplate(document_path)

sg.theme('Dark Grey 13')

layout = [
    [sg.Text("Date (YYYYMMDD):"), sg.Input(key="TODAY_INPUT", do_not_clear=False)],
    [sg.Text("Initials:"), sg.Input(key="NAME", do_not_clear=False)],
    [sg.Text("Wash count:"), sg.Input(key="WASH_COUNT", do_not_clear=False)],
    [sg.Text("Product:"), sg.Input(key="PRODUCT_MODEL", do_not_clear=False)],
    [sg.Text("PCA, STA or other:"), sg.Input(key="PCA_STA", do_not_clear=False)],
    [sg.Text("Batch number:"), sg.Input(key="BATCH_NUMBER", do_not_clear=False)],
    [sg.Text("Serial numbers of products washed:"), sg.Input(key="SERIAL_NUM", do_not_clear=False)],
    [sg.Text("Program number:"), sg.Input(key="PROGRAM_NUM", do_not_clear=False)],
    [sg.Text("Paste wash report here:"), sg.Multiline(key="PASTE_REPORT", size=(43,30), do_not_clear=False)],
    [sg.Button("Create Record"), sg.Exit()],
]

window = sg.Window("Wash Record Generator - Sinclair Interplanetary by Rocket Lab", layout, element_justification="right",)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Create Record":
        values = dict(values)
        values["DATE_NAME_NUM"] = '%s-%s-%s' % (values['TODAY_INPUT'],values['NAME'],values['WASH_COUNT'])
        output_path = Path(__file__).parent / f"{values['TODAY_INPUT']}-{values['NAME']}-{values['WASH_COUNT']}.docx"
        doc.save(output_path)
        sg.popup("Record file saved!", f"File has been saved here: {output_path}",
        "Please do not forget to commit file to SVN")

window.close()