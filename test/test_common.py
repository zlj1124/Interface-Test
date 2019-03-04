from common.read_excel import ReadExcel
from common.write_to_excel import Writedata
from common.permutations import Permutations
from common.generate_testcases import Generagetestcases


class Test():
    # 测试读取excel
    def test_read_excel(self):
        excel = ReadExcel("../test/data_origin/test_read_excel.xlsx")
        s0, s1 = excel.read_and_save_cols_excel()
        print(s0, s1)

    # 测试向excel中写数据
    def test_write_xcel(self):
        s = [[1, 2], [0]]
        W = Writedata()
        W.data_write("../test/reports/test_write_excel.xls", s)

    # 测试自由组合
    def test_permutations(self):
        excel = ReadExcel('../test/data_origin/test_read_excel.xlsx')
        s0, s1 = excel.read_and_save_cols_excel()
        # 将测试用例排列组合
        datagroup = s0
        permutations = Permutations(datagroup)
        # 用ss0列表存储排列组合的测试用例
        ss0 = permutations.assemble()
        print(ss0)
        # 将测试用例结束排列组合
        datagroup1 = s1
        permutations1 = Permutations(datagroup1)
        # 用ss1列表存储排列组合的测试用例
        ss1 = permutations1.assemble()
        print(ss1)

    # 测试自由组合生成测试用例
    def test_generate_testcases(self):
        g = Generagetestcases()
        g.generate_testcases("../test/data_origin/test_read_excel.xlsx",  # read path
                             "../test/data/test_case_01.xls",  # write path 01
                             '../test/data/test_case_02.xls')  # write path 02


if __name__ == '__main__':
    # Test().test_read_excel()
    # Test().test_write_xcel()
    # Test().test_permutations()
    Test().test_generate_testcases()