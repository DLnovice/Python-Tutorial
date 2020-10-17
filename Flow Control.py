#=========if 陳述句==========
#要在某條件成立時才進行某些動作，Python提供了if運算式,if可以搭配else，在if條件不成立時，執行else中定義的程式碼
#在Python中，區塊是從:開始，同屬一個區塊的程式碼，必須有相同的縮排（例如四個空白或一個Tab鍵）。

n1 = int(input("請輸入第一個數字: "))
n2 = int(input("請輸入第二個數字: "))
op = input("請輸入運算: +,-,*,/")
if(op == "+"):
  print(n1+n2)
elif(op=="-"):
  print(n1-n2)
elif(op=="*"):
  print(n1*n2)
elif(op=="/"):
  print(n1/n2)
else:
  print("三小...")        


import sys
score = int(input('輸入分數：'))
if score >= 90:
    print('得 A')
elif score >= 80 and score < 90:
    print('得 B')   
elif score >= 70 and score < 80:
    print('得 C')   
elif score >= 60 and score < 70:
    print('得 D')       
else:
    print('不及格')
#判斷基數偶數
input = int(input('輸入整數：'))
print('{0} 為 {1}'.format(input, '奇數' if input % 2 else '偶數'))

#==========for 與 while 陳述句==========
#如果你想要循序取出某個序列，例如串列，則可以使用for陳述句
#如果你有指定範圍或索引的需求，則可以使用range()類別產生一個range物件，由它來迭代出所指定的數字範圍，而你再利用這些數字作為索引
#range類別可以指定起始、結結與步進值：range([start,] stop[, step]) -> range object
#for陳述可以搭配一個可選的else陳述，當for迴圈中沒有遇到任何break陳述而離開迴圈時，就會執行else區塊。例如以下判斷輸入數字是否為質數：

n = 1
while n<5:
  print(n)
  n=n+1
else:
  print(n)

number = int(input('輸入數字：'))
half = number // 2
for num in range(2, half + 1):
    if (number % num) == 0:
        print(number, '不是質數')
        break
else:
    print(number, '是質數')

#break陳述可以讓你離開迴圈，而continue則可以讓你跳過該次迭代continue後的程式碼，直接作下一次迭代。例如以下僅顯示小寫英文字母：

text = input('輸入英文字母：')
for letter in text:
    if letter.isupper():
        continue
    print(letter, end='')

#while迴圈根據所指定的條件式來判斷是否執行迴圈本體，例如以下是個求最大公因數的程式：

print('輸入兩個數字...')
m = int(input('number 1: '))
n = int(input('number 2: '))
while n != 0:
   r = m % n
   m = n
   n = r
print("GCD:", m)

#Python中沒有其它語言的do while語句，所以必須使用判斷式及break來達成。例如判斷輸入為奇數或偶數，直到使用者回答No為止：

while True:
    number = int(input('輸入數字：'))
    print('輸入數為', '奇數' if number % 2 else '偶數')
    if(input('繼續？（Yes/No）') == 'No'):
        break

#==========for 包含式（Comprehension==========
#你可以在for運算式中使用包含式語法來進行值的收集，for運算結束傳回收集的結果
#如果以()包括for包含式，則會建立一個產生器物件（本身是個具有__next__()的迭代器），可以直接對其迭代來逐一取得元素。例如建立一個質數產生器

import math
def primes(max):
    prime = [1] * max
    for i in range(2, int(math.sqrt(max))):
        if prime[i] == 1:
            for j in range(2 * i, max):
                if j % i == 0:
                    prime[j] = 0
    return (i for i in range(2, max) if prime[i] == 1)
                
for prime in primes(1000):
    print("印出1~1000的質數 : ",prime, end=" ")

#==========try、raise 陳述句==========
#以下這個程式，預期使用者要輸入整數：

input = int(input('輸入整數：'))
print('{0} 為 {1}'.format(input, '奇數' if input % 2 else '偶數'))

#如果使用者輸入的不是整數，就會出現錯誤：
#在Python中程式若發生錯誤，會丟出例外事件，以上例而言就是引發（Raise）ValueError物件，如果程式沒有處理例外而丟出至執行環境，則會顯示例外追蹤（Traceback）並中斷程式。如果你想要處理例外，則可以使用try...except語句。例如：

try:
    input = int(input('輸入整數：'))
    print('{0} 為 {1}'.format(input, '奇數' if input % 2 else '偶數'))
except ValueError:
    print('請輸入阿拉伯數字')

#try..except的except可以指定多個物件，也可以有多個except，如果沒有指定except後的物件型態，則表示捕捉所有引發的物件。舉例來說，上例中若使用者於輸入時輸入Ctrl+Z，在Windows環境下會引發EOFError，若輸入Ctrl+C，則會引發KeyboardInterrupt。下例中處理這些可能的狀況：

import traceback
from fileinput import input
try:
    input = int(input('輸入整數：'))
    print('{0} 為 {1}'.format(input, '奇數' if input % 2 else '偶數'))
except ValueError:
    print('請輸入阿拉伯數字')
except (EOFError, KeyboardInterrupt):
    print('使用者中斷程式')
except:   
    print('不明的程式中斷')
    traceback.print_exc()

#try還可以搭配finally，一但設置，無論有無引發物件，finally區塊一定會執行，這通常用來作為關閉若干資源的區塊
#try也可以搭配else區塊，如果try區塊中沒有任何的錯誤發生，則會執行else區塊：
#可以使用raise自行引發例外。