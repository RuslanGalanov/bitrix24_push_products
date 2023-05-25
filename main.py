import xlrd, xlwt

from src.functions import parsing




if __name__ == '__main__':

    book = xlrd.open_workbook('spareparts.xls')

    data = parsing(book=book)

    workbook = xlwt.Workbook()
    sheet_out = workbook.add_sheet('data')


    for i in range(len(data)):

        poses = [item for item in data[i].position if item]

        sheet_out.write(i, 0, data[i].refference)
        sheet_out.write(i, 1, ' / '.join(poses))
        sheet_out.write(i, 2, data[i].ru_name)
        sheet_out.write(i, 3, data[i].en_name)
        sheet_out.write(i, 4, data[i].price)
        sheet_out.write(i, 5, ' / '.join(data[i].group))

    workbook.save('data.xls')

    book.release_resources()
    del book