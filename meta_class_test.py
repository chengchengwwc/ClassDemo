# -*- coding: utf-8 -*-
# @Time : 18-7-28 下午6:45
# @Author : weicheng.wang# @Site : 
# @File : meta_class_test.py
# @Software: PyCharm


def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company


def say(self):
    return "DDD"

class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls,*args, **kwargs)



class BaseClass(metaclass=MetaClass):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "BaseClass"



    def answer(self):
        return "HAHAH"



if __name__ == "__main__":
    #Myclass =create_class("user")
    #my_obj = Myclass()
    #print (type(my_obj))

    User = type("user",(BaseClass,),{"name":"user","say":say})
    my_obj = User()
    print (my_obj)

