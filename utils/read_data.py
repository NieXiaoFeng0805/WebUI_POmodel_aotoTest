# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/2/19 11:33
# software: PyCharm
"""
文件说明：读取文件内容

"""
import csv
import yaml
import json
import os

def get_csv_data(path):
    with open(path, 'r') as file:
        csv_list = csv.reader(file)
        next(csv_list)
        data_list = list(csv_list)
    return data_list


# def get_yaml_data(path):
#     with open(path, 'r') as file:
#         data_list = yaml.safe_load(file)
#     return data_list

# 灵活获取yaml文件
def get_yaml_data(file_name, key):
    with open('..%sdata%s%s'%(os.sep,os.sep,file_name),'r',encoding='utf-8') as f:
        meta_data = yaml.safe_load(f)[key]
        # print(meta_data)
        data_list = list()
        # print(data_list)
        # 先提取第一层key值，再提取字典对应的value
        for data in meta_data.values():
            data_list.append(data)
        return data_list

def get_json_data(path):
    with open(path, 'r') as file:
        data_json = json.loads(file.read())
        # print(temp)
        # print(temp['rule'])
        # print(temp['rule']['namespace'])
    return data_json


yaml_data = get_yaml_data('login_data.yml',"test_login_data")
print(yaml_data)
