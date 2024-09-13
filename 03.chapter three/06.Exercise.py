'''
练习 3.8：放眼世界 
想出⾄少 5 个你想去旅游的地⽅。
将这些地⽅存储在⼀个列表中，并确保其中的元素不是按字⺟顺序排列的。
按原始排列顺序打印该列表。不要考虑输出是否整洁，只管打印原始 Python 列表就好。
使⽤ sorted() 按字⺟顺序打印这个列表，不要修改它。
再次打印该列表，核实排列顺序未变。
使⽤ sorted() 按与字⺟顺序相反的顺序打印这个列表，不要修改它。
再次打印该列表，核实排列顺序未变。
使⽤ reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
使⽤ reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
使⽤ sort() 修改该列表，使其元素按字⺟顺序排列。打印该列表，核实排列顺序确实变了。
使⽤ sort() 修改该列表，使其元素按与字⺟顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
'''
locations = ['H杭州吴山居', 'B北京潘家园', 'J吉林长白山', 'S四姑娘山', 'X西藏墨脱']
print("原始列表：")
print(locations)

print("\n")

print("sorted() 排序后列表：")
print(sorted(locations))
print("sorted() 排序后列表后，再次打印：")
print(locations)

print("\n")

print("sorted() 反向排序后列表：")
print(sorted(locations, reverse=True))
print("sorted() 反向排序后列表后，再次打印：")
print(locations)

print("\n")

locations.reverse()
print("reverse() 排序后列表：")
print(locations)

locations.reverse()
print("reverse() 再次排序后列表：")
print(locations)

print("\n")

locations.sort()
print("sort() 排序后列表：")
print(locations)

locations.sort(reverse=True)
print("sort() 反向排序后列表：")
print(locations)

print("\n----------分界线----------\n")

'''
练习 3.9：晚餐嘉宾 
选择你为完成练习 3.4〜练习 3.7 ⽽编写的⼀个程序，
在其中使⽤ len() 打印⼀条消息，指出你邀请了多少位嘉宾来共进晚餐。
'''
guests = ['任毅', '马洁', '秦琪']

name = guests[0]
print(f"{name}, please come to dinner.")

name = guests[1]
print(f"{name}, please come to dinner.")

name = guests[2]
print(f"{name}, please come to dinner.")

message = len(guests)
print(f"I have invited {message} people to dinner.")

print("\n")

guests.insert(0, '刘亦菲')
guests.insert(2, '胡歌')
guests.append('张杰')

name = guests[0]
print(f"{name}, please come to dinner.")

name = guests[1]
print(f"{name}, please come to dinner.")

name = guests[2]
print(f"{name}, please come to dinner.")

name = guests[3]
print(f"{name}, please come to dinner.")

name = guests[4]
print(f"{name}, please come to dinner.")

name = guests[5]
print(f"{name}, please come to dinner.")

message = len(guests)
print(f"I have invited {message} people to dinner.")

print("\n----------分界线----------\n")

'''
练习 3.10：尝试使⽤各个函数 
想想可存储到列表中的东⻄，如⼭川、河流、国家、城市、语⾔或你喜欢的任何东⻄。
编写⼀个程序，在其中创建⼀个包含这些元素的列表。
然后，⾄少把本章介绍的每个函数都使⽤⼀次来处理这个列表。
'''