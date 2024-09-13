'''
列表
'''

#* 列表（list）由⼀系列按特定顺序排列的元素组成。
#* 你不仅可以创建包含字⺟表中所有字⺟、数字 0〜9 或所有家庭成员姓名的列表，
#* 还可以将任何东⻄加⼊列表，其中的元素之间可以没有任何关系。
#* 在 Python 中，⽤⽅括号（[]）表⽰列表，⽤逗号分隔其中的元素。
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print("\n----------分界线----------\n")

#* 访问列表中的元素
#* 列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置（索引）告诉 Python 即可。
#* 要访问列表元素，可指出列表的名称，再指出元素的索引，并将后者放在⽅括号内。
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

print("\n----------分界线----------\n")

#* 还可以对任意列表元素调⽤第 2 章介绍的字符串⽅法，让元素 'trek' 的格式更标准
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

print("\n----------分界线----------\n")

#* 索引从 0 ⽽不是 1 开始
#* 在 Python 中，第⼀个列表元素的索引为 0，⽽不是 1。
#* ⼤多数编程语⾔是如此规定的，这与列表操作的底层实现有关。
#* 如果结果出乎意料，问问自己是否犯了简单⽽常⻅的差⼀错误。
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

#* 访问列表中的最后一个元素
#* Python 为访问最后⼀个列表元素提供了⼀种特殊语法。
#* 通过将索引指定为-1，可让 Python 返回最后⼀个列表元素
#* 这种约定也适⽤于其他负数索引，例如，索引 -2 返回倒数第⼆个列表元素，索引 -3 返回倒数第三个列表元素，依此类推。
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
print(bicycles[-3])

print("\n----------分界线----------\n")

#* 使⽤列表中的各个值
#* 可以像使⽤其他变量⼀样使⽤列表中的各个值。例如，可以使⽤ f 字符串根据列表中的值来创建消息。
#* 尝试从列表中提取第⼀款⾃⾏⻋，并使⽤这个值创建⼀条消息
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

print("\n----------分界线----------\n")

#* python可以随时打印列表，查看里面都有哪些元素
print(bicycles)

print("\n----------分界线----------\n")

#* python的列表可以放不同类型的数据
list1 = ["Hello"]
list1.append(66.6)
list1.append(True)
print(list1)