# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/2/19 11:33
# software: PyCharm
"""
文件说明：读取文件内容

"""
import csv
import yaml


def get_csv_data(path):
    with open(path, 'r') as file:
        data_list = list(csv.reader(file))
    return data_list


def get_yaml_data(path):
    with open(path, 'r') as file:
        data_list = yaml.safe_load(file)
    return data_list


yaml_data = get_yaml_data('../data/login_data.yaml')
print(yaml_data)
