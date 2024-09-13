'''
练习 4.3：数到 20 
使⽤⼀个 for 循环打印数 1〜20（含）。
'''
numbers = list(range(1,21)) # range(1,21) 创建一个包含 1 到 20 的列表

for number in numbers:  
    print(number)

print("\n----------分界线----------\n")

'''
练习 4.4：100 万 
创建⼀个包含数 1〜1 000 000 的列表，再使⽤⼀个for 循环将这些数打印出来。
（如果输出的时间太⻓，按 Ctrl + C 停⽌输出，或关闭输出窗⼝。）
'''
# million = list(range(1,1000001))
# for value in million:
#     print(value)

# print("\n----------分界线----------\n")

'''
练习 4.5：100 万求和 
创建⼀个包含数 1〜1 000 000 的列表，
再使⽤min() 和 max() 核实该列表确实是从 1 开始、到 1 000 000 结束的。
另外，对这个列表调⽤函数 sum()，看看 Python 将 100 万个数相加需要多⻓时间。
'''
million = list(range(1,1000001))
print(min(million))
print(max(million))
print(sum(million))

print("\n----------分界线----------\n")

'''
练习 4.6：奇数 
通过给 range() 函数指定第三个参数来创建⼀个列表，
其中包含 1〜20 的奇数；再使⽤⼀个 for 循环将这些数打印出来。
'''
numbers = list(range(1,21,2))

for number in numbers:
    print(number)

print("\n----------分界线----------\n")

'''
练习 4.7：3 的倍数 
创建⼀个列表，其中包含 3〜30 内能被 3 整除的数，
再使⽤⼀个 for 循环将这个列表中的数打印出来。
'''
threes = list(range(3,31,3))

for three in threes:
    print(three)

print("\n----------分界线----------\n")

'''
练习 4.8：⽴⽅ 
将同⼀个数乘三次称为⽴⽅。例如，在 Python 中，2的⽴⽅⽤ 2**3 表⽰。
创建⼀个列表，其中包含前 10 个整数（1〜10）的⽴⽅，再使⽤⼀个 for 循环将这些⽴⽅数打印出来。
'''
cubes = []

for cube in range(1,11):
    cubes.append(cube**3)

for cube in cubes:
    print(cube)

print("\n----------分界线----------\n")

'''
练习 4.9：⽴⽅推导式 
使⽤列表推导式⽣成⼀个列表，其中包含前 10个整数的⽴⽅。
'''
cubes = [cube**3 for cube in range(1,11)]
for cube in cubes:
    print(cube)