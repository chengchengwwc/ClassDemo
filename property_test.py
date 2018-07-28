# -*- coding: utf-8 -*-
# @Time : 18-7-28 下午5:13
# @Author : weicheng.wang# @Site : 
# @File : property_test.py
# @Software: PyCharm


from datetime import datetime,date


class User:
    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self,value):
        self._age = value






if __name__ == "__main__":
    user = User(name="lele",birthday=date(year=1988,month=10,day=10))
    print ("in {} file".format(__file__))

