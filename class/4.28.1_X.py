import xlrd

file = 'f110020_earning_20210428.xls'
data = xlrd.open_workbook(file)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
# print(nrows, ncols)

sheet1 = data.sheet_by_index(0)
# rows = sheet1.row_values(2)
# print(rows)
current_value = 0
sum_money = 0
for i in range(1, nrows):
    sum_money = sum_money + 1
    current_value = current_value + 1
    current_value = current_value * (1 + float(sheet1.cell(i, 3).value.strip('%')) * 0.01)
print("你总共投入了：", sum_money, '元')
print("基金现在市值：", round(current_value, 2), '元')

