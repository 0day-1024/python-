'''
使⽤列表的⼀部分
在第 3 章中，你学习了如何访问单个列表元素。
在本章中，你⼀直在学习如何处理列表的所有元素。
除此之外， 你还可以处理列表的部分元素， 在Python 中称为切⽚(slice)。 
'''

#* 切⽚
#* 要创建切⽚，可指定要使⽤的第⼀个元素和最后⼀个元素的索引。
#* 与range() 函数⼀样，Python 在到达指定的第⼆个索引之前的元素时停⽌。
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print("\n")

#* 你可以⽣成列表的任意⼦集。
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

print("\n")

#* 如果没有指定第⼀个索引，Python 将⾃动从列表开头开始
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

print("\n")

#* 要让切⽚终⽌于列表末尾，也可使⽤类似的语法，省略终⽌索引
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

print("\n")

#* 负数索引返回与列表末尾有相应距离的元素，因此可以输出列表末尾的任意切⽚
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

print("\n")

#* 可在表⽰切⽚的⽅括号内指定第三个值。这个值告诉 Python 在指定范围内每隔多少元素提取⼀个。
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0::2])

print("\n")

#* 遍历切片
#* 如果要遍历列表的部分元素，可在 for 循环中使⽤切⽚。
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("\n")