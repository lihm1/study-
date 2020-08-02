print("hello")
print("finally")
############### 类的定义
def build(first-name,last-name):
    person={'first':first-name,'last':last-name}
    return person

class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+"is now sitting")

mydog=Dog('hh',2)
mydog.sit()
#%%
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+ self.make + ' ' + self.model
        print(long_name.title())
        
mynewcar=Car('qsu','a2',2016)
mynewcar.get_descriptive_name()

# %%
#############类的继承
class car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+ self.make + ' ' + self.model
        print(long_name.title())
    def read_odomter(self):
        print("this car has"+str(self.odometer_reading)+"miles on it")
class electrice(car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
my_tesla=car('hhh','hsudh',2016)
my_tesla.get_descriptive_name()
###########可以在一个模块中储存多个类
from ## import ##，##

#%%
########读取文件
filename='test.txt'
with open(filename) as file_object:
         for line in file_object:
            print(line.rstrip())#### 逐行读取
       lines=file_object.readlines() ####将其中所有的行储存在一个列表中
pi_string=''
for line in lines:
   pi_string +=line.rstrip()
print(pi_string)


# %%
###写入空文件
filename='iu.txt'
with open(filename,'w') as file_object:
    file_object.write("I love iu.\n")
    file_object.write("IU is so beautiful.\n")
#%%
################################
##re 模块 与正则表达式相连
import re
str="allb22c33"
m=re.compile("\d+")
print(m.findall(str))
print(m.search(str))
# %%
list=['sdhaj','hdus','hdi','wshd']
print(list[1])

# %%
rage=3
while rage<3:
    rage=rage+1
    print("怒气值"+str(rage))
if rage==3:
    print("your are win!")

# %%
def sum(number=10,number2=2):
 print(number+number2)


#%%
def say():
    print("hsadaksdkls")
    say()
    
# %%
###datetime时间模块
import datetime
print(datetime.datetime.now())
###random随机数模块
#%%
##操做excel 的模块 xlrd
import xlrd
data =xlrd.open_workbook('SigProfiler_signature_assignment_rules.xlsx')
table=data.sheets()[0]###通过索引顺序获取工作表
print(table.row_values(0))


# %%
####image
from PIL import Image
import os
im = Image.open("散点图.jpeg")
im.show()


# %%
#z字典
dict内置函数创建字典
dict1=dict(one=1, two=2,three=3 )
dict3=dict{'one': 1,'two': 2,'three':3}
#fromkeys创建字典
dict1.fromkeys((1,2,3),"number")
##keys values item
dict4={}
dict4=dict4.fromkeys(range(32),"zan")
dict4.keys()
dict4.values()
#%%
import os

# %%
os.getcwd()


# %%
