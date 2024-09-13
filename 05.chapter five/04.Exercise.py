'''
练习 5.1：条件测试 
编写⼀系列条件测试，将每个条件测试以及你对其结果的预测和实际结果都打印出来。
你编写的代码应类似于下⾯这样：
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
详细研究实际结果，直到你明⽩它为何为 True 或 False。
创建⾄少 10 个条件测试，⽽且结果为 True 和 False 的条件测试分别⾄少有 5 个。
'''
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\n----------分界线----------\n")

'''
练习 5.2：更多条件测试 
你并⾮只能创建 10 个条件测试。
如果想尝试做更多的⽐较，可再编写⼀些条件测试，并将它们加⼊conditional_tests.py。
对于下⾯列出的各种情况，⾄少编写两个条件测试，结果分别为 True 和 False。
检查两个字符串是否相等和不等。
使⽤ lower() ⽅法的条件测试。
涉及相等、不等、⼤于、⼩于、⼤于等于和⼩于等于的数值⽐较。
使⽤关键字 and 和 or 的条件测试。
测试特定的值是否在列表中。
测试特定的值是否不在列表中。
'''
name1 = "John"
name2 = "john"

print(name1 == "John")
print(name1 == name2)

print(name1.lower() == name2)

print("\n")

num = 1024
print(num == 1024)
print(num >= 1000)
print(num <= 1000)
print(num > 1000)
print(num < 1000)

print("\n")

num = 1024
print((num > 1000) and (num < 1500))
print((num > 500) and (num < 1000))

print((num > 500) or (num < 1000))
print((num < 500) or (num > 1500))

print("\n")

users = ['andrew', 'carolina', 'david']
print("carolina" in users)
print("Carolina" in users)