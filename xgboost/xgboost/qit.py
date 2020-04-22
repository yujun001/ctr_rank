
#实现一个数字反转
'''
class Solution(object):
    def reverse(self, x):
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[1:][::-1]
            x = int(str_x)
            x = -x
            return x

if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reverse(-130009912388)
    print(reverse_int)
'''

##一行代码实现1-N的数字分组，3个为一组。
'''
print([[x for x in range(1,1000)] [i:i+3] for i in range(0,100,3)])

or

list_a = [x for x in range(1,100)]
for i in range(0,len(list_a),3):
    print(list_a[i:i+3])
'''


##一段代码实现，删除list的重复元素
a = ['1','d','c','w','3','d','c']
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

or

a = ['1','d','c','w','3','d','c']
b = list(set(a))
b.sort(key=a.index)
print(b)


##找出两个数组中相同、不同的元素
a = ['a','c','a','d','c','e']
b = ['a','1','3','t']
print(set(a)&set(b))
print(set(a)^set(b))

##列表生成式，产生一个公差为11的等差数列
print([x for x in range(0,100,11)])
print([x*11 for x in range(10)])


##列表的下标表示

list = ['a','b','c','d','e']
    print(list[10:])

list[::-1] ##反转
list[:-1]  ##去掉最后一个
list[-1:]  ##最后一个



##将列表中的字典，按照制定列排序
class ranksolution(object):
    def rank(self,alist):
        rank_list = alist
        return sorted(rank_list,key=lambda x:x['age'],reverse= True)


if __name__ == '__main__':
    s = ranksolution()
    alist = [{'name': 'a', 'age': 10},
             {'name': 'b', 'age': 30},
             {'name': 'c', 'age': 25},
             {'age':12,'name':'d'}]
    rank_res = s.rank(alist)
    print(rank(alist))

##将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}

class strdict(object):
    def str2dict(self,st):
        dict_res = {}
        for items in st.split('|'):
            print(items)
            key,value = items.split(':')
            dict_res[key] = int(value)
            print(dict_res)
        return dict_res

if __name__ == '__main__':
    solu = strdict()
    st = "k:1|k1:2|k2:3|k3:4"
    res = solu.str2dict(st)
    print(res)


##实现字符串的反转

x = 'hello_world'
str = []
for items in x.split('_'):
    str.append(items)
res = str[1]+'_'+str[0]

print(res)


##合并两个有序列表,不使用函数
def merge_list(list1,list2,tmp):
    if (len(list1) == 0) or (len(list2) == 0):
        tmp.extend(list1)
        tmp.extend(list2)
        return tmp
    else:
        if list1[0] < list2[0]:
            tmp.append(list1[0])
            del list1[0]
        else:
            tmp.append(list2[0])
            del list2[0]
        return merge_list(list1,list2,tmp)

##两个有序列表
l1 = [2,2,3,1,5,6,9]
l1.sort(reverse = False)
l2 = [7,2,1,3,5,9,4]
l2.sort(reverse = False)
print(merge_list(l1,l2,[]))


##二分法查找,制定元素坐在的坐标位置。
def binary_search(list,value):
   low = 0
   high = len(list)-1
   while low<=high:
       mid = int((low+high)/2)
       guess = list[mid]
       if guess>value:
           high = mid-1
       elif guess<value:
           low = mid+1
       else:
           return mid
    return None

mylist = [1,3,5,7,9]
print (binary_search(mylist,9))


##选择排序
def minfind(array):
    minindex = 0
    minvalue = array[minindex]
    for i in range(1,len(array)):
        if array[i]<minvalue:
            minindex = i
    return minindex

def selectsort(array):
    newarray = []
    for i in range(0,len(array)):
        newarray.append(array.pop(minfind(array)))
    return newarray


array = [5,9,1,6,0,5,3,56,897]

print(selectsort(array))

##递归快速排序
def quicksort(list):
    if len(list)<2:
        return list #基线条件,为空或者只包含一个元素的数组是有序的
    mid = list[0]#递归条件
    lessbeforemid = [i for i in list[1:] if i<=mid]#小于基准值的元素组成的子数组
    biggeraftermid = [i for i in list[1:] if i > mid]#大于基准值的元素组成的子数组
    finallylist = quicksort(lessbeforemid)+[mid]+quicksort(biggeraftermid)
    return finallylist

print(quicksort([2,4,6,7,1,2,5]))



#字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
d= {'a':24,'g':52,'i':12,'k':33}
lis = sorted(d.items(),key=lambda x:x[1],reverse= True)   ##如果按key排序，就是键 x[0]
#[('g', 52), ('k', 33), ('a', 24), ('i', 12)]

new_dict = {}
for i in lis:
    new_dict[i[0]] = i[1]
print("新字典",new_dict)




##tuple,list 互换
a = ('a',2)
b = ['b',4]
list(a)
tuple(b)

##字典推导式
x = {('a',2),('b',3),('c',4)}
{key: value for (key, value) in x}


##输入日期， 判断这一天是这一年的第几天？
import datetime
def dayofyear():
    year = input("请输入年份: ")
    month = input("请输入月份: ")
    day = input("请输入天: ")
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    return (date1 - date2).days + 1


##一个jsonline格式的文件爱file.txt 大小约为10K,内存只有4G，读取共计10G的文件
def get_lines():
    l = []
    with open('file.txt','rb') as f:
        for eachline in f:
            l.append(eachline)
        return l

if __name__ == '__main__':
    for e in get_lines():
        process(e) #处理每一行数据


def get_lines():
    l = []
    with open('file.txt','rb') as f:
        data = f.readlines(60000)
    l.append(data)
    yield l


##一条代码实现，0-101的数据求和
count = sum(range(0,101))
print(count)


##装饰器本质上是一个python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
import time
def timeit(fun):
    def wrapper():
        start = time.clock()
        fun()
        end = time.clock()
        print('used:', end - start)
        return wrapper



def ZHUIYI_AI(we_):
    women_ = b'\xef\xbc\x8c'
    are_ = b'\xe8\x87\xaa\xe7\x84\xb6'
    all_ = b'\xe6\x87\x82\xe3\x80\x82'
    gods_ = we_ + women_ + are_ + all_
    print(gods_.decode(encoding='UTF-8'))


if __name__ == '__main__':
    ZHUIYI_AI(b'\xe6\x9c\x89AI')


##类的继承
##__class__方法指向了类对象
class A:
    def show(self):
        print('base show')

class B(A):
    def show(self):
        print('derived show')

if __name__ == '__main__':
    obj = B()
    obj.show()
    obj.__class__ = A
    obj.show()

ls = [1,2,3,4]
list1 = [i for i in ls if i >2]


dic1 = {x:x**2 for x in (2,4,5)}
print(dic1)


set1 = {x for x in 'hello world' if x not in 'low level'}
print(set1)


##global 定义全局变量
num = 9

def f1():
  global num
  num = 20

def f2():
 print(num)

f2()
f1()
f2()

##一行代码
a = 9
b = 8
a,b = b,a


##返回一个内置函数
def mulby(num):
  def gn(val):
      return num * val
  return gn


zw = mulby(7)
print(zw);


sum(range(0,101))


dic1 = {'age':23,'team':'word'}
print(dic1.values())

for key,values in dic1.items():
    print(key,values)


##字典的键删除，字典合并
del dic1['age']
dic2 = {'age':27}
dic1.update(dic2)


##集合去重，然后set容器转成集合
lis = [1,3,2,4,5,6,9]
a = set(lis)
a = list(a)
or
a = [ x for x in a]


##*中可以带入一个元组数据
def demo(args_f,*args_v):
    print(args_f)
    #print(type(args_v))
    for x in args_v:
        #print(type(x))
        print(x)
demo(1,2,3,5)


##**中可以带入一个键值对
def demo(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)

kwargs = {'name':'tom'}
demo(**kwargs)
or
demo(name='tom')


##文件的读写，与随机数生成
import random
fp = open('./rand.txt','wb')
for i in range(101):
    print(i)
    try:
        ran = random.randint(0,101)
        #fp.write(ran)
        print(ran)
        #fp.write('\n')
    except:
        pass
    finally:
        fp.close


##map 函数，列表推导式
##map()是 Python 内置的高阶函数，它接收一个函数f和一个 list，
#并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
## 可以有多个列表，同时使用lambda 匿名函数
list = [2,3,4,5,6]
def fn(x):
    return x**2

res = map(fn,list)   ##map返回的是个对象

res = [i for i in res if i>10]
print(res)


##随机树生成
##随机整数，随机小数，随机0-1小数
import  random
import  numpy as np
result = random.randint(10,20)
res = np.random.randn(5)
ret = random.random()

print("随机整数",result)
print("5个随机小数",res)
print("0-1随机小数",ret)



## (.*?) 提取文本
import re
str = '<div class="nam">中国</div>'
res = re.findall(r'<div class=".*">(.*?)</div>',str)

print(res)



##python2和python3的主要区别
1.Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')
  Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比如 print 'hi'
2.Python2 range(1,10)返回列表，python3中返回迭代器，节约内存
3.Python2中使用ascii编码，python中使用utf-8编码
4.Python2中unicode表示字符串序列，str表示字节序列
   Python3中str表示字符串序列，byte表示字节序列
5.Python2中为正常显示中文，引入coding声明，python3中不需要
6.Python2中是raw_input()函数，python3中是input()函数


##python中可变数据类型和不可变数据类型，并简述原理
1.不可变数据类型：数值型、字符串型string和元组tuple
如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存中则只有一个对象（一个地址）

2.可变数据类型：列表list和字典dict；
允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，只是改变了变量的值，
而不会新建一个对象，变量引用的对象的地址也不会变化


##字符串去重，并从小到大排序输出新的字符串
s = "ajldjlajfdljfddd"
x = list(set(s))
x = sorted(x,reverse= False)
res = ''.join(i for i in x)
or res = ''.join(x)


##sample
'1,2,3,4' -> [1,2,3,4]

del list
list(map(int,'1,2,3,4'.split(',')))

[int(i) for i in '1,2,3,4'.split(',')]


##lambda实现两个数相乘
sum = lambda x,y :x*y
sum(5,2)

##字典根据建从小到大排序
dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

list = sorted(dict.items(),key = lambda x:x[0],reverse = False)
print("按照键值排序",list)

new_dict ={}
for i in list:
    new_dict[i[0]] = i[1]
print("新的字典",new_dict)


##统计字符串每个单词出现的次数
from collections import  Counter
a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
b = ['1','3','2','1','4','2','1']
print(Counter(a))
print(Counter(b).items())

##统计字符串中指定字符的个数
str = "张三 美国  张三  英国  张三 韩国"
res = str.count("张三")
print(res)


##或者这样，统计字符串或者数组出现次数
dic = set(a)
res = {}
for i in dic:
    k = 0
    for j in range(len(a)):
        if i == a[j]:
            k+= 1
    res[i] = k
print(res)


##用正则过滤掉英文和数字
\d 匹配数字
\.?\d* 匹配小数
|[a-zA-Z]  匹配单词
import re
a = "not 404 found 张三 99 深圳"
list = a.split(" ")
print(list)
res = re.findall('\d+|[a-zA-Z]+',a)

for i in res:
    if i in list:
        list.remove(i)
print(list)

#new_res = ' '.join(x for x in list)
new_res = ' '.join(list)
print(new_res)


##filter()函数用于过滤序列，过滤掉不符合条件的元素，返回符合条件元素组成的新列表。
##最后只返回 True 的元素放到新列表，而map对于所有的元素都返回
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def fn(a):
    if(a%2 == 1):
        return a

newlist = map(fn,a)
new_list = [i for i in newlist]
print(new_list)

##列表推导式，构造新的列表
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i for i in a if i%2==1]
print(res)


##列表合并,(1)extend可以实现逐一添加，(2)append整体添加，需要循环使用 (3)也可以直接相加
list1 = [1,5,7,9]
list2 = [2,2,6,8]
#res = list1 + list2

for i in list2:
    list1.append(i)
print(list1)

#or
#list1.extend(list2)

list1.sort(reverse= False)
print(list1)


##字典合并，需要update
dict1.update(dict2)



##自定义异常 raise 抛出异常
def fn():
    try:
        for i in range(5):
            if i>2:
                raise Exception("数字大于2了")
    except Exception as ret:
        print(ret)

fn()

###
try..except..else没有捕获到异常，执行else语句。
try..except..finally不管是否捕获到异常，都执行finally语句。


##[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]？
a = [[1,2],[3,4],[5,6]]
j = [j for i in a for j in i]

#or
j= []
for i in a:
    j.extend(i)
print(j)



## join中是可迭代对象，字符串或者列表都可以
x="abc"
y="def"
z=["d","e","f"]
w = ('d','e','f')

##set 是个无序集合，慎用
s = {'d','e','f'}
type(s)
x.join(s)


m = x.join(y)
n = x.join(z)
p = x.join(w)
print(m)
print(n)
print(p)


##zip()函数的用法
#zip()函数在运算时，会以一个或多个序列（可迭代对象）做为参数，返回一个元组的列表。
#同时将这些序列中并排的元素配对。

a = [1,2]
b = [3,4]

a = (1,2)
b = (3,4)

a = "ab"
b = "xyz"

res = [i for i in zip(a,b)]
print(res)

##将元组列表转换成 dict
res_dict = {}
for j in res:
    res_dict[j[0]] = j[1]
print(res_dict)


##正则匹配与替换,替换数字
import re
a = "张明 98分"
#ret = re.sub(r'\d+',"100",a)
print(ret)



##解码编码
a = "哈哈哈哈".encode()
print(a)
res = a.decode(encoding= 'UTF-8')
print(res)


##简述mysql和redis区别？
redis： 内存型非关系数据库，数据保存在内存中，速度快。

mysql：关系型数据库，数据保存在磁盘中，检索的话，会有一定的Io操作，访问速度相对慢。




##正则匹配，匹配日期 2018=03-20

import re
url = 'https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'

res = re.findall(r'dateRange=(.*?)%7C(.*?)&',url)

print(res)



##递归获取，列表从小到大的顺序
list = [2,3,5,4,9,6]

(1)递归获取
new_list = []
def get_min(list):
    a = min(list)
    list.remove(a)
    new_list.append(a)
    if len(list)>0:
        get_min(list)
    return new_list

new_list = get_min(list)
print(new_list)

(2)利用sort 函数
list.sort(reverse = False)
or
sorted(list,reverse=False)


##键值对，传给字典
def fn(k,v,dic = {}):
    dic[k] = v
    print(dic)

fn('one',1)
fn('two',2)
fn('three',3,{})


##使用pop和del删除字典中的"name"字段，

dic={"name":"zs","age":18}
dic.pop("name")
print(dic)

dic = {"name":"zs","age":18}
del dic["name"]
print(dic)



##zip 迭代式转换成，输入可以是列表、元组
A = zip(("a","b","c","d","e"),(1,2,3,4,5))
res = [i for i in A]

dict_res = {}
for i in res:
    dict_res[i[0]]=i[1]
print(dict_res)

##{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

##dict()创建字典新方法，列表嵌套元组、列表嵌套列表
dict([('a', 1), ('b', 2), ('c', 3)])

dict([['a', 1], ['b', 2], ['c', 3]])

##{'a': 1, 'b': 2, 'c': 3}



####简述多线程、多进程？

进程：
1、操作系统进行资源分配和调度的基本单位，多个进程之间相互独立。

2、稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限制。

线程：
1、CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比进程更小的能独立运行的基本单位，
    一个进程下的多个线程可以共享该进程的所有资源。

2、如果IO操作密集，则可以多线程运行效率高，缺点是如果一个线程崩溃，都会造成进程的崩溃。


应用：
IO密集的用多线程，在用户输入，sleep 时候，可以切换到其他线程执行，减少等待的时间。

CPU密集的用多进程，因为假如IO操作少，用多线程的话，因为线程共享一个全局解释器锁，
    当前运行的线程会霸占GIL，其他线程没有GIL，就不能充分利用多核CPU的优势。



a = (i for i in range(3))



##yield 迭代器

yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一
个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行
到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句
继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次
遇到 yield。


yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用
类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        print(b)
        a, b = b, a + b
        n = n + 1

for n in fab(5):
    print(n)

##使用lambda 函数进行由大到小排序
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
a = sorted(foo,key = lambda x:x,reverse = True)
print(a)



##列表推导式，字典推导式，生成器（非元组推导式）
import random
list = [i for i in range(10)]
print("列表推导式",list)

ge = (i for i in range(10))
print("生成式",ge)

dict = {k:random.randint(4,9) for k in ['a','b','c','d']}
print("字典推导式",dict)



##根据列表中字符串长度排序,从大到小
s = ['ab','abc','a','adfg']
b = sorted(s,key = lambda x:len(x),reverse = True)

print(b,s)


##利用正则切分字符串
import re
s="info:xiaoZhang 33 shandong"
res = re.split(r':| ',s)
print(res)


##邮箱匹配
email_list = ['xiaoyu@163.com','xiaowang@163.comheihei','.com.xiaowang@qq.com']

for email in email_list:
    ret = re.match("[\w]{4,20}@163\.com$",email)
    if ret:
        print("%s 符合规定,邮箱地址是：%s" %(email,ret.group()))
    else:
        print("%s 不符合要求"% email)


##递归求和,
##1+2+3+4+。。+20
def get_sum(num):

    if num< 0:
        raise ValueError
    elif num <= 1:
        res = num
    else:
        res = num + get_sum(num - 1)
    return res

result = get_sum(100)
print(result)


##佩波那契数列 1+1+2+3+5+8
def fib(n):
    if n<1:
        raise ValueError
    elif n<=2:
        return n
    else:
        return fib(n-1)+fib(n-2)

sum = 0
for i in range(1,10):
    sum+=fib(i)
print("数列的前十个数和为:",sum)



##单词反转
def reverce(str_list,start,end):
    while start < end:
        str_list[start],str_list[end] = str_list[end],str_list[start]
        start += 1
        end -= 1
    sentence = 'hello, nice to meet you!'
    str_list = list(sentence)
    i = 0
    while i<len(str_list):
        if str_list[i]:
            start = i
            end = start+1
            while(end <len(str_list)and str_list[end]!=' '):
                end += 1
                reverce(str_list,start,end - 1)
            i = end
        else:
            i +=1

#先拆分后整合元素
str_list.reverse()
print(''.join(str_list))


##python 字典和json字符串相互转化
import json
dic = {"name":"zs"}

#字典转json字符串
res = json.dumps(dic)
print(res,type(res))

#json字符串转字典
ret = json.loads(res)
print(ret,type(ret))


##字符串大小写
str = "HHHuuu"
print(str.upper())
print(str.lower())


##去重空格的两种方法
str = "hello world ha ha"
res = str.replace(" ","")
print(res)


list = str.split(" ")
res= "".join(list)
print(res)


##正则匹配不是以4和7结尾的手机号
tels = ['135558897','18903289993','136876892','10086']

for tel in tels:
    ret = re.match("1\d{9}[0-3,5-6,8-9]",tel)
    if ret:
        print("想要的结果",ret.group())
    else:
        print("%s 不是想要的手机号" % tel)


##正则匹配所有的中文
title = '你好，hello, 世界'
pattern = re.compile(r'[\u4e00-\u9fa5]+')
result = pattern.findall(title)
print(result)


##求两个列表的交集、差集、并集？
a = [1,2,3,4]
b = [4,3,5,7]

#交集
jj1 = [i for i in a if i in b]
jj2 = list(set(a).intersection(set(b)))

#并集
bj1 = list(set(a).union(set(b)))

#差集
cj1 = list(set(b).difference(set(a)))
cj2 = list(set(a).difference(set(b)))


##lambda 匿名函数的好处
a = ["苏州","中国","哈哈","","","日本","","","德国"]
res = map(lambda x:"填充址" if x =="" else x,a)

res = list(res)
or
res = [i for i in res]


a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
b = eval(a)
new = {i[0]:i[1] for i in b}


a = "([1,2], [3,4], [5,6], [7,8], (9,0))"
b = eval(a)
new_dict = {i[0]:i[1] for i in b}


##收集关键字参数
def func(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])

func(a=1,b=2,c=3)


##传递一个列表或一个元组值时
def func(*args):
    for i in args:
        print(i)

func(3,2,1,4,7)


##统计文件中的大写字母数
import os
os.chdir('/Users/jun_yu/Documents/xgboost')

with open('c.txt') as f:
    count = 0
    for i in f.readline():
        if i.isupper():
            print(i)
            count+=1
    print(count)

##join()和split()函数
##join 将列表中元素拼接成字符串，split 将字符串分割成列表
'，'.join('12345')

'1，2，3，4，5'.split(',')



##循环、跳出语句
for i in range(7):
    if i ==3:
        print("跳出循环")
        continue  #跳到循环下一步
        #break    #直接结束循环
        #pass     #可以继续执行,1、空语句，什么也不做  2、在特别的时候用来保证格式或是语义的完整性
        print("dddd")
    else:
        print(i)


##数学运算
7//2 =3   #取整，返回整数
7/2  =3.5 #除法
7%2  =1   #取模，返回除法后的余数
7**2 =49  #取幂


##
match() 从第一个字符开始找, 如果第一个字符就不匹配就返回None, 不继续匹配. 用于判断字符串开头或整个字符串是否匹配,速度快。
search() 会整个字符串查找,直到找到一个匹配。
也就是说match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none









