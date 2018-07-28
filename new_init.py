# -*- coding: utf-8 -*-
# @Time : 18-7-28 下午6:36
# @Author : weicheng.wang# @Site : 
# @File : new_init.py
# @Software: PyCharm


class User:


    def __new__(cls, *args, **kwargs):
        print ("in new")
        print (kwargs)
        return super().__new__(cls)


    def __init__(self,name):
        print ("in init")
        self.name = name

#new 用来控制对向的生成过程
#new 不返回对象就不会产生init
if __name__ == "__main__":
    user = User(name="DDD")
    print (user.name)
