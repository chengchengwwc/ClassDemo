# -*- coding: utf-8 -*-
# @Time : 18-7-28 下午6:03
# @Author : weicheng.wang# @Site : 
# @File : getattr.py
# @Software: PyCharm

from datetime import datetime,date


class User:
    def __init__(self,name,birthday,info={}):
        self.name = name
        self.birthday = birthday
        self.info = info


    def __getattr__(self, item):
        return self.info[item]





if __name__ == "__main__":
    user = User(name="lele",birthday=date(year=1988,month=10,day=10))
    print ("in {} file".format(__file__))


