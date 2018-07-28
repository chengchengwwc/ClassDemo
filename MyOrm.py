# -*- coding: utf-8 -*-
# @Time : 18-7-28 下午7:09
# @Author : weicheng.wang# @Site : 
# @File : MyOrm.py
# @Software: PyCharm

import numbers


class Filed:
    pass



class IntField(Filed):

    def __init__(self,db_column,min_value=None,max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column

        if min_value is not None:
            if isinstance(min_value,numbers.Integral):
                raise ValueError("min value value need")

        if max_value is not None:
            if isinstance(max_value,numbers.Integral):
                raise ValueError("min value value need")

        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("max must be larger than min")



    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise  ValueError("int value need")

        if value < self.min_value or value > self.max_value:
            raise ValueError("value should be between min and max")
        self._value = value


    def __delete__(self, instance):
        pass


class CharField(Filed):

    def __init__(self,max_length=None):
        self._value = None
        self.max_length = max_length
        if max_length is None:
            raise ValueError("you must write max_length")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value,str):
            raise ValueError("String value need")

        if len(value) > self.max_length:
            raise ValueError("Value must between max_length")

        self._value = value



class ModelMetaClass(type):

    def __new__(cls,name,bases,attrs, **kwargs):
        if name == "BaseModel":
            return super().__new__(name,bases,attrs, **kwargs)
        fields = {}
        for key,value in attrs.items():
            if isinstance(value,Filed):
                fields[key] = value
        attrs_meta = attrs.get("Meta",None)
        _meta= {}
        db_table = name.lower()
        if attrs_meta is not None:
            table_name = getattr(attrs_meta,"table",None)
            if table_name is not None:
                db_table = table_name
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        return super().__new__(name,bases,attrs,**kwargs)



class BaseModel(metaclass=ModelMetaClass):
    def __init__(self,*args,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
        return super().__init__()

    def save(self):
        fileds = []
        values = []
        for key,value in self.fields.items():
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower()
            fileds.append(db_column)
            value = getattr(self,key)
            values.append(values)

        sql = 'insert {db_table}({fileds}) value ({values})'.format(db_table=self.db_table,fileds=",".format(fileds),values=",".format(values))


class User(BaseModel):
    name = CharField(max_length=100)
    age = IntField(db_column="Age")

    class Meta:
        db_table = "AKAK"









