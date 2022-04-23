# if output does not come, please delete pdf file and again insert pdf file then its work
# sometime pdfplumber corrupt the files.
import re
import pdfplumber
import pandas as pd
from collections import namedtuple
Line=namedtuple('Line','Name Phone Mobile Email Office_Address Residence_Address')
company_re = re.compile(r'(V\d+) (.*) Phone:')
line_re = re.compile(r'\d{2}/\d{2}/\d{4} \d{2}/\d{2}/\d{4}')

file = 'File.pdf'

lines = []
total_check = 0


with pdfplumber.open(file) as pdf:
    pages = pdf.pages
    for page in pdf.pages:
        text = page.extract_text()
        for line in text.split('\n'):
            print(line)
            comp = company_re.search(line)
            if comp:
                vend_no, vend_name = comp.group(1), comp.group(2)

            elif line.startswith('Name'):
                doctype = 'Name'

            elif line.startswith('Mobile'):
                doctype = 'Mobile'

            elif line.startswith('Office'):
                doctype = 'Office'    
            
            elif line.startswith('Phone'):
                doctype = 'Phone'

            elif line.startswith('Residence'):
                doctype = 'Residence'
                
            elif line_re.search(line):
                items = line.split()
                lines.append(Line(vend_no, vend_name, doctype, *items))
  