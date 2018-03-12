#列表生成式即List Comprehensions,python内置用来创建list的生成式
#生成list：[1,2,3,4,5,6,7,8,9,10],可以用list(range(1,11))

##生成 [1*1,2*2,3*3,...,10*10]
#一循环：
L=[]
i=1
while i<11:         #for  x in range(1,11)
    L.append(i*i)
    i+=1

print(L)
#二：
l=[x*x for x in range(1,11)]
print(l)

#2层循环
ll=[m+n for m in 'ABC' for n in 'XYZ']
print(ll)

#列出当前目录下的所有文件和目录名
import os                           #导入os模块
m=[d for d in os.listdir('..')]      #os.listdir可以列出文件和目录，一个.当前，两个..上一级
print(m)

#for同时使用多个变量
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)

l2=[k + '=' + v for k,v in d.items()]   #这里+是print里的，作用
print(l2)

#把list中所有字符串变成小写：
L=['Hello','World','IBM','Apple']
CL=[s.lower() for s in L]           #注意：非字符串类型没有lower办法
print(CL)


##*******练习
L1 = ['Hello', 'World',18, 'Apple', None]
L2 = []
for s in L1:
    if isinstance(s,str)==True:
        L2.append(s.lower())
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
