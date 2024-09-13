'''
修改、添加和删除元素
你创建的⼤多数列表将是动态的，这意味着列表创建后，将随着程序的运⾏增删元素。
'''

'''
修改列表元素
修改列表元素的语法与访问列表元素的语法类似。
'''
#* 要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。
#* 假设有⼀个摩托⻋列表，其中的第⼀个元素为 'honda'，那么可在创建列表后修改这个元素的值
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

print("\n----------分界线----------\n")

'''
在列表中添加元素
你可能会出于很多原因在列表中添加新元素。
'''
#* 在列表末尾添加新元素
#* 在列表中添加新元素时，最简单的⽅式是将元素追加（append）到列表末尾
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

print("\n")

#* append() ⽅法让动态地创建列表易如反掌。
#* 例如，你可以先创建⼀个空列表，再使⽤⼀系列函数调⽤ append() 添加元素。
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print("\n")

#* 在列表中插⼊元素
#* 使⽤ insert() ⽅法可在列表的任意位置添加新元素，需要指定新元素的索引和值
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')
print(motorcycles)

print("\n----------分界线----------\n")

'''
从列表中删除元素
你经常需要从列表中删除⼀个或多个元素。
'''
#* 使⽤ del 语句删除元素
#* 如果知道要删除的元素在列表中的位置，可使⽤ del 语句
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

print("\n")

#* 使⽤ del 可删除任意位置的列表元素，只需要知道其索引即可。
#* 例如，下⾯演⽰了如何删除列表 motorcycles 中的第⼆个元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

print("\n")

#* 使⽤ pop() ⽅法删除元素
#* 有时候，你要将元素从列表中删除，并接着使⽤它的值。
#* pop() ⽅法删除列表末尾的元素，并让你能够接着使⽤它。
#* 术语弹出（pop）源⾃这样的类⽐：列表就像⼀个栈，⽽删除列表末尾的元素相当于弹出栈顶元素。
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle) #* 最后打印弹出的值，以证明依然能够访问被删除的值

print("\n")

#* ⽅法 pop() 的⽤处 
#* 假设列表中的⾃⾏⻋是按购买时间存储的，就可使⽤⽅法 pop() 来打印⼀条消息，指出最后购买的是哪款⾃⾏⻋
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

print("\n")

#* 删除列表中任意位置的元素
#* 实际上，也可以使⽤ pop() 删除列表中任意位置的元素，只需要在括号中指定要删除的元素的索引即可。
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(motorcycles)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#* 每当你使⽤ pop() 时，被弹出的元素就不再在列表中了。
#* 如果不确定该使⽤ del 语句还是 pop() ⽅法，下⾯是⼀个简单的判断标准：
#* 如果要从列表中删除⼀个元素，且不再以任何⽅式使⽤它，就使⽤ del 语句;
#* 如果要在删除元素后继续使⽤它，就使⽤ pop() ⽅法。

print("\n")

#* 根据值删除元素
#* 有时候，你不知道要从列表中删除的值在哪个位置。
#* 如果只知道要删除的元素的值，可使⽤ remove() ⽅法。
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

print("\n")

#* 使⽤ remove() 从列表中删除元素后，也可继续使⽤它的值。
#* 下⾯删除值 'ducati' 并打印⼀条消息，指出将其从列表中删除的原因：
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
#* 值 'ducati' 虽然已经从列表中删除，但可通过变量 too_expensive 来访问
print(f"\nA {too_expensive.title()} is too expensive for me.")

print("\n")

#* 注意：remove() ⽅法只删除第⼀个指定的值。
#* 如果要删除的值可能在列表中出现多次，就需要使⽤循环，确保将每个值都删除。
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'ducati']
print(motorcycles)

value = 'ducati'
motorcycles.remove(value)
#motorcycles.remove(value)
print(motorcycles)