#========變數========
#依型態資訊是記錄在宣告在變數之上，或者是執行時期的物件之上，程式語言可以區分為靜態（Static）語言（例如C/C++、Java）與動態（Dynamic）語言（例如Python、JavaScript）。
#Python是動態語言，也就是變數本身並沒有型態資訊，型態的資訊是在執行時期的物件之上，在Python中要建立變數，無需宣告型態，只要命名變數並指定值給它，就建立了一個變數，在建立變數之前，嘗試存取某個變數會發生變數未定義的錯誤。
x = 1.0
y = x
print("x 記憶體位址代表數字 : ", id(x))  #id()函式來取得所參考物件的記憶體位址代表數字
#在Python中，==用來比較兩個物件的實質內容是否相同。
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("比較兩串列是否相同 : ", list1 == list2)

#========運算子========
#最基本的就是+、-、*、/運算子，當他們用在數值運算時是較為直覺的加、減、乘、除運算。不過，+在Python的物件上，往往可以作串接物件的作用，例如串接字串、串接Tuple、串接串列等，結果都是產生新的物件傳回：
print("alin" + "yiwen")
print("alinyiwen" * 3)
print("數值次方運算 :", 9**2)

#========物件與記憶體管理========
#如果想要知道一個物件有幾個名稱參考至它，可以使用sys.getrefcount()函式。
import sys
print(sys.getrefcount(1))
x = [1, 2, 3]
y = x
z = x
q = x
print(sys.getrefcount(x))

#========end操作========
# 關鍵字end可以用於將結果输出到同一行，或者在輸出的末尾添加不同的字符
# Fibonacci series: 斐波纳契数列
# 兩個元素的總和確定了下一個數
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b

#其中 a, b = b, a+b 的计算方式為先計算右邊表達式，然後同時賦值給左邊，等同於：
#n=b  m=a+b  a=n  b=m    
