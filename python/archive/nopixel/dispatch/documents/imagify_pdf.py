from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from pathlib import Path
import csv
import os
import re

os.chdir(Path(Path(__file__).parent))

print(Path(__file__).parent)


pdf_file = Path.joinpath(Path(__file__).parent, 'Copy of SA Central Dispatch SOPs - NP 4.0.pdf')
# pdf_file = Path.joinpath(Path(__file__).parent, 'SA Central Dispatch SOPs - NP 4.0.pdf')
# pdf_file = Path.joinpath(Path(__file__).parent, 'Dispatch Roster - NP 4.0.pdf')
# pdf_file = Path.joinpath(Path(__file__).parent, 'SACD Final Remarks.pdf')
output_folder = Path.joinpath(Path(__file__).parent, 'output')
print(pdf_file)

images = convert_from_bytes(open(pdf_file, 'rb').read(), poppler_path=r'C:\Users\elena\Documents\poppler\Library\bin', output_folder=output_folder, fmt='png')
print(len(images))
