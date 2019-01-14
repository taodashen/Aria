#!/usr/bin/env python
# encoding: utf-8
'''
@author: zhoutao
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: zhoutao970226@gmail.com
@software: pycharm
@file: Aria2-BtTracker.py
@time: 2019/1/11 19:28
@desc:
'''

import requests
import re


# 从github上获取Bt-Tracker
def get_tracker(type):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/57.0.2987.133 Safari/537.36 '
    }
    if type == '0':
        url = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt"
    else:
        url = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt"
    print(url)
    html = requests.get(url=url, headers=headers).content.decode("utf-8")
    return html


# 处理bt-tracker
def handle_str(tracker):
    tracker_list = tracker.split('\n\n')
    # print(tracker_list)
    bt_tracker_str = ""
    for bt_tracker in tracker_list:
        if bt_tracker != "":
            bt_tracker_str = bt_tracker_str + bt_tracker + ","
    # print(bt_tracker_str)
    return bt_tracker_str


# 写入aria2.conf文件
def main():
    # 打开文件读取内容
    print("Get Best or All Bt-Tracker(0/1):")
    tracker_type = input()
    html = get_tracker(tracker_type)
    result = handle_str(html)

    print("Append or Replace(0/1):")
    func = input()

    file = open("aria2.conf", "r")
    file_list = file.readlines()
    file.close()

    # 处理字符串
    line_num = len(file_list)
    if func == '0':
        file_list[line_num - 1] += result
    if func == '1':
        file_list[line_num - 1] = "bt-tracker=" + result

    # 打开文件写入内容
    file = open("aria2.conf", "w+")
    file.writelines(file_list)
    file.close()
    pass

main()
