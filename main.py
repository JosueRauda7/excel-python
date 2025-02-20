import openpyxl
wb = openpyxl.load_workbook('prueba.xlsx')
sheet = wb.active

def main():
    for row in sheet.iter_rows(min_row=2, max_row=5, min_col=1, max_col=2):
        for cell in row:
            print(cell.value)
    sheet['A4'] = '3'
    sheet['B4'] = 'Prueba'
    wb.save('prueba2.xlsx')

if __name__ == '__main__':
    main()