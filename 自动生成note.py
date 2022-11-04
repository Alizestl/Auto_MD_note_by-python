import os
import datetime


def create_file(path):

    now = datetime.datetime.now()
    # current time

    file_date = now.strftime("22-%m-%d")
    file_name = file_date + ".md"
    # file_name + file_format

    os.chdir(path)
    # switch working path

    f = open(file_name, 'w')
    # create file


if __name__ == '__main__':

    path1 = r'C:\Users\zcbaa\Desktop\I DO WHAT in A DAY'
    path2 = r'F:\学习笔记\C++\Note'
    # path

    create_file(path1)
    create_file(path2)