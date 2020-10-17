#在Python中要定義函式，是使用def來定義

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

print("最大公因數 : ",gcd(20, 30)) # 顯示 10

#gcd是函式名稱，m與n為參數（Parameter）名稱，如果要傳回值則使用return，如果函式執行完畢但沒有使用return傳回值，則傳回None。

#實際上，def是個陳述句，Python執行到def時，會產生一個函式物件，為function的實例，即然函式是個物件，它可以指定給其它的變數，例如：

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

print(gcd(20, 30))         # 顯示 10
print(type(gcd))           # 顯示 <class 'function'>

gcd2 = gcd
print(gcd2(20, 30))        # 顯示 10
print(id(gcd), id(gcd2))   # 兩個顯示的數字相同

#在Python中同一個名稱空間中，不能有相同的函式名稱。如果你定義了兩個函式具有相同的名稱但擁有不同的參數個數，則後者定義會覆蓋前者定義。
#由於Python是動態語言，只需在設計時確認傳入函式的物件所擁有的特性或方法，無需採函式重載中，依型態不同來區別所呼叫函式的部份，至於依參數個數不同來區別的函式重載概念，在Python中可以使用預設引數（Argument）來解決。例如：

def sum(a, b, c = 100):
    return a + b + c

print(sum(10, 20, 30))   # 顯示 60
print(sum(10, 20))       # 顯示 30

#像sum這種加總數字的需求，事先可能不知道要傳入的引數個數，可以在定義函式的參數時使用*，表示該參數接受不定長度引數。例如：

def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum(1, 2))        # 顯示 3
print(sum(1, 2, 3))     # 顯示 6
print(sum(1, 2, 3, 4))  # 顯示 10

#你傳入函式的引數，會被收集在一個Tuple中，再設定給numbers參數。有趣的是，如果你有個函式擁有固定的參數，你可以將一個Tuple傳入，只要在傳入時加上*，則Tuple中每個元素會自動指定給各個參數。例如：

def sum3(a, b, c):
    return a + b + c

numbers = (1, 2, 3)
print(sum3(*numbers))

#**則可以將關鍵字引數收集在一個字典物件中，當一個函式所需要的參數個數很多時，可以使用這個方式。例如：

def dosome(**args):
  print(args)
dosome(name = 'Justin', passwd = 123456, job = '?')

#反過來的話，如果函式參數個數固定，你也可以傳給函式一個字典物件，只要在物件前加上**，則Python會依字典物件的鍵名稱，將值指定給對應名稱的參數。例如：

def sum3(a, b, c):
    return a + b + c

args = {'a' : 1, 'b' : 2, 'c' : 3}
print(sum3(**args))


#在Python中，函式中還可以定義函式，稱之為區域函式（Local function），你可以使用區域函式將某個函式中的演算組織為更小的單元，例如，在 選 擇排序 的實作時，每次會從未排序部份選擇一個最小值放置到已排序部份之後，在底下的範例中，尋找最小值的演算就實作為區域函式的方式：

def selection(number):
    # 找出未排序中最小值
    def min(m, j):
        if j == len(number):
            return m
        elif number[j] < number[m]:
            return min(j, j + 1)
        else:
            return min(m, j + 1)
    
    for i in range(0, len(number)):
        m = min(i, i + 1)
        if i != m:
            number[i], number[m] = number[m], number[i]

number = [18,55, 62, 38, 92, 77]
print("排序前 : ",number)
selection(number)
print("排序後 : ",number)     # 顯示 [1, 2, 3, 5, 7, 9]



############################################################################
#定義函式
def multipy(n1,n2):
  
  return n1*n2
#呼叫函式
NN = multipy(20,30)+multipy(10,10)
#print(NN)
#程式的包裝
def calculate(x,y):
  sum = 0
  for n in range(x,y):
    sum = sum+n
  print(sum)
calculate(10,10)
#參數的預設資料
def power(base,exp=0):
  print(base**exp)
#使用參數名稱對應
def divide(n1,n2):
  print(n1/n2)
#divide(2,4)   
#divide(n2 = 2,n1 = 4)

def avg(*ns):
  sum = 0
  for n in ns:
    sum = sum+n
  print(sum/len(ns))

#avg(2,4,7)
#avg(-1,-4,67,100)  