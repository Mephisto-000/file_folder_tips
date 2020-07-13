import os, glob
import pathlib
import numpy as np
import pandas as pd
from pathlib import Path


def home_path():
    """使用者路徑"""
    path = Path.home()
    path = str(path)
    return path

def get_local_path():
    """取得目前工作目錄"""
    path = os.getcwd()
    return path

def get_absolute_path():
    """取得絕對路徑"""
    path_1 = os.path.abspath(".")
    path_2 = os.path.abspath("..")
    path_3 = os.path.abspath("path_tip.py")
    return path_1, path_2, path_3

def get_certain_path(aim, start):
    """取得特定路段相對路徑"""
    path = os.path.relpath(aim, start)
    return path


if __name__ == "__main__":
    home_path = home_path()
    print("\nHome path :", home_path)

    path_0 = get_local_path()
    print("\n目前工作目錄 :", path_0)

    path_1, path_2, path_3 = get_absolute_path()
    print("\n目前工作目錄的絕對路徑 :", path_1)
    print("\n目前工作目錄上一層的絕對路徑 :", path_2)
    print("\n目前檔案的絕對路徑 :", path_3)