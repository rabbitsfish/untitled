li = []
with open('20190920_231922.csv', 'r+', encoding='utf-8', newline='') as f:
    # new_lines = [line.strip() for line in f.readlines()]
    # print(new_lines)
    li = [line.strip() for line in f.readlines()][1:]
    # print(li)

import xlrd
workbook = xlrd.open_workbook('音乐埋点.xlsx', encoding_override='utf-8')
sheet1 = workbook.sheet_by_index(0)
rows = sheet1.row_values(0)
posi = rows.index('Event ID')
cols = sheet1.col_values(posi)[1:]
for i in cols:
    if i not in li:
        print(i)