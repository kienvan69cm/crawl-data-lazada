import openpyxl
import pprint

wb = openpyxl.load_workbook("data.xlsx")
sheet = wb['Sheet']
pprint.pprint(list(sheet.values), width=40)
