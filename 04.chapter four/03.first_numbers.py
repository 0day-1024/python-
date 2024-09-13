'''
创建数值列表
需要存储⼀组数的原因很多。
列表⾮常适合⽤于存储数值集合，⽽ Python 提供了很多⼯具，可帮助你⾼效地处理数值列表。
'''

#* 使⽤ range() 函数
#* Python 函数 range() 让你能够轻松地⽣成⼀系列的数。
for value in range(1,5):
    print(value)

print("\n")

#* 在上个⽰例中，range() 只打印数 1〜4，这是编程语⾔中常⻅的差⼀⾏为的结果。
#* range() 函数让 Python 从指定的第⼀个值开始数，并在到达指定的第⼆个值时停⽌，
#* 因此输出不包含第⼆个值（这⾥为 5）。要打印数 1〜5，需要使⽤ range(1,6)
for value in range(1,6):
    print(value)

print("\n")

#* 使⽤ range() 创建数值列表
#* 要创建数值列表，可使⽤ list() 函数将 range() 的结果直接转换为列表。
#* 如果将 range() 作为 list() 的参数，输出将是⼀个数值列表。
numbers = list(range(1, 6))
print(numbers)

print("\n")

#* 在使⽤ range() 函数时，还可指定步⻓。
#* 为此，可以给这个函数指定第三个参数，Python 将根据这个步⻓来⽣成数。
even_numbers1 = list(range(2, 11, 2))
print(even_numbers1)

even_numbers2 = list(range(2, 12, 2))
print(even_numbers2)

print("\n")

#* 使⽤ range() 函数⼏乎能够创建任意数值集合。
#* 例如，如何创建⼀个列表，其中包含前 10 个整数（1〜10）的平⽅？
#* 在 Python 中，⽤两个星号（**）表⽰乘⽅运算。
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

#* 为了让代码更简洁，可不使⽤临时变量 square，⽽是直接将计算得到的每个值追加到列表末尾
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

print("\n")

#* 对数值列表执⾏简单的统计计算
#* 有⼏个 Python 函数可帮助你处理数值列表。
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min_num = min(digits) #* 返回列表中的最小值
print(min_num)
max_num = max(digits) #* 返回列表中的最大值
print(max_num)
sum_num = sum(digits) #* 返回列表中所有值的和
print(sum_num)

print("\n")

#* 列表推导式
#* 前⾯介绍的⽣成列表 squares 的⽅式包含三四⾏代码，⽽列表推导式让你只需编写⼀⾏代码就能⽣成这样的列表。
#* 列表推导式（list comprehension）将 for 循环和创建新元素的代码合并成⼀⾏，并⾃动追加新元素。
#* 使⽤列表推导式创建了你在前⾯看到的平⽅数列表
squares = [value ** 2 for value in range(1,11)]
print(squares)

#* 要使⽤这种语法，⾸先指定⼀个描述性的列表名，如 squares。
#* 然后指定⼀个左⽅括号，并定义⼀个表达式，⽤于⽣成要存储到列表中的值。
#* 在这个⽰例中，表达式为 value**2，它计算平⽅值。
#* 接下来，编写⼀个 for 循环，⽤于给表达式提供值，再加上右⽅括号。
#* 在这个⽰例中，for 循环为 for value in range(1,11)，它将值 1〜10 提供给表达式value**2。
#* 请注意，这⾥的 for 语句末尾没有冒号。