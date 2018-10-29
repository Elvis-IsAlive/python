#! /usr/bin/python3.6

"""manipulate workbook censuspopdata.xlsx"""

import openpyxl, pprint



wb_name = "censuspopdata.xlsx"

print("opening workbook %s" % wb_name)


wb = openpyxl.load_workbook(wb_name)
s = wb.get_sheet_by_name("Population by Census Tract")

county_data = {}

for i in range(2, s.max_row):
    state = s["B" + str(i)].value
    county = s["C" + str(i)].value
    pop = s["D" + str(i)].value

    county_data.setdefault(state, {})      # Staat anlegen
    county_data[state].setdefault(county, {"tracts": 0, "pop": 0})  # county anlegen
    county_data[state][county]["tracts"] += 1   # jede Zeile stellt einen Tract dar
    county_data[state][county]["pop"] += pop



# File erstellen, das importiert werden kann
filename = "census2010.py" 
print("writing results to file %s" % filename)
with open(filename, "w") as f:
    f.write("all data = " + pprint.pformat(county_data))

print("done.")
