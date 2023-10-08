# -*- codeing = utf-8 -*-
# @Time : 2020/12/4 0:04
# @Author : Li Canghao
# @Name : C_means.py
# @Software : PyCharm
import math
import random
import matplotlib.pyplot as plt   #用于做图

class twoD:
    x = 0.0
    y = 0.0
    belong = 0      #所属哪个类

    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
    def toString(self):
        return str(self.x) + " " + str(self.y)

def Distance(a,b):
    return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

def GenerateTrains():               #随机生成训练集并写入文件中
    number = random.randint(100,200)
    try:
        f = open("trains.txt","w")  #因为测试了N次，为了不占用空间，用了w模式而不是a追加
        try:
            for i in range(number):
                temp = twoD(random.random()*4041-2020,random.random()*4041-2020)  #数据范围为[-2020,2020]
                f.write(temp.toString())
                if i != number-1:
                    f.write("\n")
            print("-----创建训练集成功-----")
        finally:
            f.close()
            print("-----文件关闭-----")
    except Exception as ex:
        print("-----出现异常",ex,"-----")

def ReadTrains():                   #读取训练集
    trains = []
    try:
        f = open("trains.txt","r")
        print("-----读取训练集成功-----")
        try:
            for line in f.readlines():
                train = line.split()
                temp = twoD(train[0],train[1])
                trains.append(temp)
            return trains
        finally:
            f.close()
            print("-----文件关闭-----")
    except Exception as ex:
        print("-----出现异常",ex,"-----")

def C_mean(trains,c):
    centers = trains[0:c]                       #[切片]，选择C个点作为初始类心，这里将前c个作为初始类心
    new_centers =[]                             #记录新的类心
    numbers = []                                 #桶，记录一个类有多少个模式
    counts = 0                                  #记录未变的类的数量
    while counts < c:
        numbers = [0 for i in range(c)]
        #new_centers = [twoD for i in range(c)]  #计算每个类 新的类心  #该写法有问题，指向同一个twoD，改一个全部都会更改，浅复制
        new_centers = [twoD(0,0) for i in range(c)]  #深复制，不会指向同一个目标
        for i in range(len(trains)):            #遍历样本点
            mindistance = 1e7                   #最小距离
            minindex = 0                        #记录离哪个类心距离近
            for j in range(len(centers)):       #遍历当前点，找到距离最小的类心
                if Distance(trains[i],centers[j]) < mindistance:
                    mindistance = Distance(trains[i],centers[j])
                    minindex = j
            trains[i].belong = minindex         #归属minindex类
            new_centers[minindex].x += trains[i].x         #计算新的类心 先算总的x,y
            new_centers[minindex].y += trains[i].y
            #for n,z in enumerate(new_centers):
               # print(n,z.x,z.y)
            #print("new_centers[%d].x = %d,new_centers[%d].y = %d"%(minindex,new_centers[minindex].x,minindex,new_centers[minindex].y))
            numbers[minindex] += 1              #该类中 模式的数量+1
            '''for n,z in enumerate(numbers):
                print(n,z)'''
            #print("trains[%d].belong = %d,numbers[%d] = %d"%(i,trains[i].belong,minindex,numbers[minindex]))
        '''  for i in new_centers:
                print(i.x,i.y)
            print("-"*30)'''
        for i,center in enumerate(centers):     #遍历类心，比较新类心和旧类心是否发生变化
            #print("new_centers[%d].x = %d,new_centers[%d].y = %d"%(i,new_centers[i].x,i,new_centers[i].y))
            new_centers[i].x /= float(numbers[i])
            new_centers[i].y /= float(numbers[i])
            #print("new_centers[%d].x = %d,new_centers[%d].y = %d"%(i,new_centers[i].x,i,new_centers[i].y))
            if ((new_centers[i].x - center.x < 1e-6) and (new_centers[i].y - center.y < 1e-6)):
                counts += 1                     #未变的类数量+1
            centers[i] = new_centers[i]         #更新类心
    print("-----处理完毕，展示结果-----")
    colors = ["red","blue","green","coral","tan","yellow","brown","gold","orange","peru"]
    marks = ["+","x","o","v","^","<",">","1","2","3"]
    for i,center in enumerate(centers):
        print("当前第%d类，类心为：(%d,%d) 共有%d个模式，它们分别是："%(i + 1,center.x,center.y,numbers[i]))
        for j,train in enumerate(trains):
            if train.belong == i:
                print("\t%d:(%d,%d)"%(j+1,train.x,train.y))
                plt.scatter(train.x,train.y,marker = marks[i],c = colors[i])
    plt.show()



'''def ShowPlot():
    for i in range(c):
        plt.scatter()'''

print("-----准备创建训练集-----")
GenerateTrains()
print("-----准备读取训练集-----")
trains = ReadTrains()
print(len(trains))
c = int(input("请输入需要分成多少类"))
print("-----C均值聚类开始-----")
C_mean(trains,c)
print("-----C均值聚类结束-----")
#ShowPlot()



