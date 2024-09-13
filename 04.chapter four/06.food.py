'''
复制列表
你经常需要根据既有列表创建全新的列表。
'''

#* 要复制列表，可以创建⼀个包含整个列表的切⽚，⽅法是同时省略起始索引和终⽌索引（[:]）。
#* 这让 Python 创建⼀个起始于第⼀个元素、终⽌于最后⼀个元素的切⽚，即复制整个列表。
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n")

#* 为了核实确实有两个列表，下⾯在每个列表中都添加⼀种⾷品，并确认每个列表都记录了相应的⼈喜欢的⾷品
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n")

#* 如果只是将 my_foods 赋给 friend_foods，就不能得到两个列表。
#* 例如，下⾯演⽰了在不使⽤切⽚的情况下复制列表的情况
my_foods = ['pizza', 'falafel', 'carrot cake']

#* 这是⾏不通的：
#* 这⾥将 my_foods 赋给 friend_foods，⽽不是将 my_foods 的副本赋给 friend_foods。
#* 这种语法实际上是让 Python 将新变量friend_foods 关联到已与 my_foods 相关联的列表，
#* 因此这两个变量指向同⼀个列表。
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)