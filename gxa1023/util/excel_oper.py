
# #获取execl对象
# workbook = xlrd.open_workbook('E:\\Download\\paycharman\\exl_test.xlsx')
# #获取工工作表
# sheet = workbook.sheet_by_index(0)
# #获取值
# value = sheet.cell_value(1,1)
# for i in range(0,sheet.nrows):
#     for j in range(0, sheet.ncols):
#         print(sheet.cell_value(i,j))
#
#
import xlrd

class Excel_e:

    def __init__(self, path, sheet_name):
        self.workbook = xlrd.open_workbook(path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)
        # for i in range(0,sheet.nrows):
        #     for j in range(0, sheet.ncols):
        #         print(sheet.cell_value(i,j))

    def get_nrow(self):
        return self.sheet.nrows

    def get_ncol(self):
        return self.sheet.ncols

    def get_cell(self, row, col):
        cell_v = self.sheet.cell_value(row, col)
        if cell_v=='null':
            return ''
        return cell_v

# if __name__ == '__main__':
#     excel_e = Excel_e('E:\\Download\\paycharman\\exl_test.xlsx', )
#     print(excel_e.get_cell())
