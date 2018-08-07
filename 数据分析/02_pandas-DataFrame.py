from pandas import Series, DataFrame
import pandas

# 与Serise，字典这种一维数据结构不同，DataFrame是一种二维的数据结构，类似于MySQL数据库的表，注意每一列数据数量需保持一致
data = {"name":['google','baidu','yahoo'],"marks":[100,200,300],"price":[1,2,3]}
# 其中的键name，marks，price被称为columns
d1 = DataFrame(data)
print(d1)

# 当然，DataFrame的索引也可以自己定义
d2 = DataFrame(data,columns=["name","marks","price"],index=["a","b","c"])
print(d2)

# 通过多级嵌套字典定义DataFrame,用此方法每一列数据数量可以不一致，对于没有规定的数据默认为NaN
data2 = {
    "name":
        {"a": 'google', "b": 'baidu', "c": 'yahoo',"d": '360'},
    "marks":
        {"a": 100, "b": 200, "c": 300},
    "price":
        {"a": 1,"b": 2,"c": 3}}
d3 = DataFrame(data2)
print(d3)

# 得到某一列的全部内容
print(d3["name"])

# 修改columns名称,被修改的列数据都变为NaN
d4 = DataFrame(data2,columns=["name","marks","level"])
print(d4)

# 设置默认值
d4["level"] = 1
print(d4)

# 修改单个数据，类似字典操作
copy_d = d4.copy()
copy_d["level"]["c"] = 100
print(d4)

# 用Series数据为DataFrame赋值
s1 = Series([10,20,30,40],index=["a","b","c","d"])
d4["level"] = s1
print(d4)

