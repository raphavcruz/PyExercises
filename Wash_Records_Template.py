from pathlib import Path
import datetime
from docxtpl import DocxTemplate

document_path = Path(__file__).parent / "WashRecordTemplate.docx"
doc = DocxTemplate(document_path)

product = "ST"
part = "PCA"
batch = "025"
serial_number = "025, 026, 027..."
program_number = "01"
date = "TODAY"
today_input = "2022xx04"
washed_by = "RC"
wash_count = "xxx"

wash_record = (today_input, washed_by, wash_count)
line1 = "some text"

context = {
    "PRODUCT_MODEL": product,
    "PCASTA": part,
    "BATCH_NUMBER": batch,
    "SERIAL_NUM": serial_number,
    "PROGRAM_NUM": program_number,
    "NAME": washed_by,
    "DATE_NAME_NUM": wash_record,
    "PASTE_REPORT": line1,
    "TODAY_INPUT": today_input

}

doc.render(context)
doc.save(Path(__file__).parent / f"{today_input}-{washed_by}-{wash_count}.docx")