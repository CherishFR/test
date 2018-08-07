from pandas import Series
import pandas

s1 = Series(["刘锦涛",23,"男"],index=["姓名","年龄","性别"])
print(s1)

# Series的操作与字典类似，可以看作一个竖着显示的字典
print(s1["姓名"])
s1["姓名"] = "刘涛"
print(s1["姓名"])
dic = {"姓名":"刘锦涛","年龄":23,"性别":"男"}
s2 = Series(dic)
print(s2)

# 自动对其，没有的项会显示NaN
s3 = Series(dic,index=["姓名","年龄","籍贯"])
print(s3)

# 判断是否为空，如果为空则返回True，
print(pandas.isnull(s3))  # 也可以对Series对象调用这个方法：s3.isnull()

# 修改索引名称,索引的数量必须与修改前对应，否则会报错
s1.index = ["姓名","多少岁了","性别"]
print(s1)


