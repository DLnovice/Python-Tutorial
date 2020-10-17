#＝＝＝＝＝＝＝＝字串string＝＝＝＝＝＝＝＝
text = "aliyiwinn"
print("字串長度 : ", len(text))

text1 = "alin"
text2 = "yiwen"
print("字串相加 : ", text1 + text2)

name = "alinyiwen"
print("字串切片1 : ", name[0:3])
print("字串切片2 : ", name[::-1])  #表示從索引0至結尾，以負偏移1方式取得字串，結果就是反轉字串。
print("改大寫 : ", name.upper())
print("改小寫 : ", name.lower())

#＝＝＝＝＝＝＝＝串列list＝＝＝＝＝＝＝＝
list1 = []
list1.append(821111)
list1.append('alinyiwen')
print(list1)
list1.pop()
print("pop操作 :　", list1)
list1.remove(821111)
print("remove操作 :　", list1)
list1.insert(0, 'louis.lin')
print("insert操作 :　", list1)

list13 = [6, 1, 7, 3, 8]
list13.sort()
print(list13)
list13.sort(reverse=True)
print(list13)

#＝＝＝＝＝＝＝＝集合set＝＝＝＝＝＝＝＝
#集合（Set）是無序、元素不重複的集合。要建立集合，可以使用{}包 括元素的實字方式來建立集合。
family = set()
family.add('alin')
family.add('yiwen')
print("集合成員 : ", family)

admins = {'Justin', 'caterpillar'}  # 建立 set
users = {'momor', 'hamini', 'Justin'}
print('Justin' in admins)  # 是否在站長群？

#＝＝＝＝＝＝＝＝字典dict＝＝＝＝＝＝＝＝
#字典物件是儲存鍵（Key）/值（Value）對應的物件，為dict的實例。
passwords = {'alin': 821111, 'yiwen': 830920}
passwords['liuliu'] = 1071017  #增加物件
passwords.update({'yiwen': 670723})  #增加物件
print("字典 :　", passwords)
print("alin :　", passwords['alin'])
for person in passwords:
    print(passwords[person])
print("取得字典中的鍵/值 : ", passwords.items())
passwords2 = dict(justin=123456, momor=670723, hamimi=970221)
print("字典2 :　", passwords2)
dic = {x: x**2 for x in [3, 4, 5]}
print(dic)

#＝＝＝＝＝＝＝＝Tuple＝＝＝＝＝＝＝＝
#Tuple就像是串列（List），不過串列是可變動（Mutable）物件，而Tuple是不可變動（Immutable）物件。你可以使用()來建立Tuple物件，也可以直接逗號區隔元素來建立Tuple物件。
tuple1 = ([1, 2], [3, 4])
#print("指定tuple索引0為新串列不可行",tuple1[0] = [10, 20])
tuple1[0][0] = 10
tuple1[0][1] = 20
print("更改串列索引內容qqq :　", tuple1)
