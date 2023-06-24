#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/31 15:15
# @Author  :Rj.Zhao
# @File    : tools
import os
import glob
import json


def return_file_name(file_path, type="png"):
    """
    find all file names in one folder based on specific type, return file name list in abs path and only file name separately
    file_path: str
    type: file type
    """
    if type == "excel":
        # find excel path
        xls_file_lyst = glob.glob(file_path + "/" + "*.xlsx")
        xls_file_lyst_name = [i.split("/")[-1] for i in xls_file_lyst]
        return xls_file_lyst, xls_file_lyst_name
    elif type == 'json':
        # find json path
        json_file_lyst = glob.glob(file_path + "/" + "*.json")
        json_file_lyst_name = [i.split("/")[-1] for i in json_file_lyst]
        return json_file_lyst, json_file_lyst_name
    elif type == 'png':
        # find png
        png_file_lyst = glob.glob(file_path + "/" + "*.png")
        png_file_lyst_name = [i.split("/")[-1] for i in png_file_lyst]
        return png_file_lyst, png_file_lyst_name
    elif type == 'dir':
        # find dir path
        dir_lyst = []
        for file in os.scandir(file_path):
            if file.is_dir():
                dir_lyst.append(file.path)
        dir_lyst_name = [i.split("/")[-1] for i in dir_lyst]
        return dir_lyst, dir_lyst_name
