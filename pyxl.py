import openpyxl

book = openpyxl.load_workbook("C:\Users\dhana\OneDrive\Desktop\excel")

sheet = book.active

cell = sheet.cell(row = 3 , column = 1)

print(cell.value)