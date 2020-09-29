#-*- coding:utf-8 -*-

import os, sys
import re

# 度分秒转为经纬度
def convert2degree(str_lat_lon):
    # 22°17'12.24''_114°09'13.37''
    lat_str, lon_str = str_lat_lon.split("_")
    lat_split = re.split(u"°|\'|\"", lat_str)[:3]
    if len(lat_split) == 3:
        x = [float(j) for j in lat_split]
        lat= x[0] + x[1] / 60. + x[2] / 3600.

    lon_split = re.split(u"°|\'|\"", lon_str)[:3]
    if len(lon_split) == 3:
        x = [float(j) for j in lon_split]
        lon= x[0] + x[1] / 60. + x[2] / 3600.
    print(lon, lat)


# 替换符号
def substitute_name_by_sign(path):
    file_list =  os.listdir(path)
    os.chdir(path)
    for img_name in file_list:
        if "^" in img_name:
            split_list = img_name.split("^")
            # os.rename(img_name, new_name)
            new_name = img_name.replace("^","°").replace("’","'").replace("‘","'")
            os.rename(img_name, new_name)
            print(img_name, new_name)

# substitute_name_by_sign(input())
while True:
    convert2degree(input())#eg "22°19'09.55''_114°11'15.73''"
