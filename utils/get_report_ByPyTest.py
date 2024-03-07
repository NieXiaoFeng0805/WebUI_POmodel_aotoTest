# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/7 16:17
# software: PyCharm
"""
文件说明：

"""
import pytest
if __name__ == '__main__':
    file_path = "../testcase/test_case.py"
    report_path = "../TheReport"
    command_lines = ["-s", file_path, "--alluredir={}".format(report_path),]
    pytest.main(command_lines)

    # 运行完后在终端输入  “allure serve TheReport”