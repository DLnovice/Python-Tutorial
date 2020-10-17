#類物件支援兩種操作：屬性引用和具現化。
#屬性引用使用和 Python 中所有的屬性引用一樣的標準語法：obj.name。
#類物件創建後，類命名空間中所有的命名都是有效屬性名。 所以如果類定義是這樣

class MyClass:
    i = 12345
    def f(self):
       return 'hello world'
# 实例化类
x = MyClass()
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

#類的方法與普通的函數只有一個特別的區別——它們必須有一個額外的第一個參數名稱, 按照慣例它的名稱是 self。

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()

#在類的內部，使用 def 關鍵字來定義一個方法，與一般函式定義不同，類方法必須包含參數 self, 且為第一個參數，self 代表的是類的實例。

#class 定義

class people:
    #基本屬性
    name = ''
    age = 0
    #定義私有屬性,外部類別無法直接存取
    __weight = 0
    #定義構造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 說': 我 %d 歲。" %(self.name,self.age))
 
#範例

class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #調用父類別
        people.__init__(self,n,a,w)
        self.grade = g
    #複寫父類別
    def speak(self):
        print("%s 說: 我 %d 歲了，我在讀 %d 年级"%(self.name,self.age,self.grade))

#多重繼承

class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演說家，我演講的主題是 %s"%(self.name,self.topic))


class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
 
test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法


class Account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
 
    def deposit(self, amount):
        if amount <= 0:
             raise ValueError('amount must be positive')
        self.balance += amount
 
    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('balance not enough')
        self.balance -= amount
 
    def __str__(self):
        return 'Account({0}, {1}, {2})'.format(
            self.name, self.number, self.balance)

acct = Account('ALIN', '0988526756', 200000)  #建立類別物件
acct.deposit(500)  #使用類別物件操作其內函式
acct.withdraw(200)
print (acct)



#定義一個類別IO 兩個屬性

class IO:
  supporttedSrcs=["console","file"]
  def read(self, src):
    if src not in IO.supporttedSrcs:
      print("不支援")
    else:  
      print("Read from",src)
IO.read("file")
IO.read("filed")


class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def show(self):
    print(self.x,self.y) 
  def distance(self,targetX,targetY):
    return ((self.x-targetX)**2+(self.y-targetY)**2)**0.5   
p1 = Point(3,4)      #第一個實體物件
p1.show()

result = p1.distance(0,0)
print(result)


#fullname
class FullName:
  def __init__(self,first,last):
    self.first = first
    self.last = last

name1 = FullName("Yang Ting","Lin")
print(name1.first,name1.last)

name2 = FullName("Y.T.","Lin")
print(name2.first,name2.last)


class File:
  def __init__(self,name):
    self.name = name
    self.file = None
  def open(self):
    self.file = open(self.name,mode="r",encoding = "utf-8")
  def read(self):
    return self.file.read() 
    

########################################################################################3
# 明日科技 從零開始學 python 

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #创建空字典
        dict = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in dict:
                return dict[x],i
                print(dict[x])
            else:
                dict[nums[i]] = i
                print(dict[nums[i]])

y = [1, 2, 3, 4, 5]
sl = Solution()
sl.twoSum(y,5)
