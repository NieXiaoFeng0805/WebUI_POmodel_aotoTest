# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/7 16:17
# software: PyCharm
"""
文件说明：

"""
import pytest
import os

if __name__ == '__main__':
    # 是获取当前get_report_ByPyTest.py的父级目录
    base_path = os.path.dirname(os.path.abspath(__file__))

    file_path = "../test_case/test_index.py"
    report_path = "../TheReport"
    command_lines = ["-s", file_path, "--alluredir={}".format(report_path), ]
    pytest.main(command_lines)

    # 运行完后在终端输入  “allure serve TheReport”
