"""
为整个工程提供统一的绝对路径
"""
import os


def get_project_root() -> str
    """
    获取工程所在的根目录
    :return:字符串根目录
    """
    #当前文件的绝对路径
    current_file=os.path.abspath(__file__)
    #获取工程的根目录，先获取文件夹所在的文件夹绝对路径
    current_dir=os.path.dirname(current_file)