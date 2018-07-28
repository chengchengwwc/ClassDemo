# -*- coding: utf-8 -*-
# @Time : 18-7-28 下午6:11
# @Author : weicheng.wang# @Site : 
# @File : attr_desc.py
# @Software: PyCharm

from datetime import datetime,date
import numbers


class IntField:

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise  ValueError("int value need")
        self.value = value


    def __delete__(self, instance):
        pass


class NonDataInteField:

    def __get__(self, instance, owner):
        pass



class User:

    age = IntField()













if __name__ == "__main__":
   user = User()
   user.__dict__["age"] = "DDD"
   print (user.__dict__)
   print (user.age)


