'''
练习 3.4：嘉宾名单 
如果你可以邀请任何⼈⼀起共进晚餐（⽆论是在世的还是故去的），你会邀请哪些⼈？
请创建⼀个列表，其中包含⾄少三个你想邀请的⼈，然后使⽤这个列表打印消息，邀请这些⼈都来与你共进晚餐。
'''
guests = ['任毅', '马洁', '秦琪', '李四']

name = guests[0]
print(f"{name}, please come to dinner.")

name = guests[1]
print(f"{name}, please come to dinner.")

name = guests[2]
print(f"{name}, please come to dinner.")

name = guests[3]
print(f"{name}, please come to dinner.")

print("\n----------分界线----------\n")

'''
练习 3.5：修改嘉宾名单 
你刚得知有位嘉宾⽆法赴约，因此需要另外邀请⼀位嘉宾。
以完成练习 3.4 时编写的程序为基础，在程序末尾添加函数调⽤print()，指出哪位嘉宾⽆法赴约。
修改嘉宾名单，将⽆法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
再次打印⼀系列消息，向名单中的每位嘉宾发出邀请。
'''
guests = ['任毅', '马洁', '秦琪', '李四']

name = guests[0]
print(f"{name}, please come to dinner.")

name = guests[1]
print(f"{name}, please come to dinner.")

name = guests[2]
print(f"{name}, please come to dinner.")

name = guests[3]
print(f"\nSorry, {name} can't make it to dinner.\n")

guests[3] = '张三'

name = guests[0]
print(f"{name}, please come to dinner.")

name = guests[1]
print(f"{name}, please come to dinner.")

name = guests[2]
print(f"{name}, please come to dinner.")

name = guests[3]
print(f"{name}, please come to dinner.")

print("\n----------分界线----------\n")

'''
练习 3.6：添加嘉宾 
你刚找到了⼀张更⼤的餐桌，可容纳更多的嘉宾就座。请想想你还想邀请哪三位嘉宾。
以完成练习 3.4 或练习 3.5 时编写的程序为基础，在程序末尾添加函数调⽤ print()，指出你找到了⼀张更⼤的餐桌。
使⽤ insert() 将⼀位新嘉宾添加到名单开头。
使⽤ insert() 将另⼀位新嘉宾添加到名单中间。
使⽤ append() 将最后⼀位新嘉宾添加到名单末尾。
打印⼀系列消息，向名单中的每位嘉宾发出邀请。
'''
print("I found a bigger table!")

guests.insert(0, '刘亦菲')
guests.insert(2, '胡歌')
guests.append('张杰')
print(guests)

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

name = guests[6]
print(f"{name}, please come to dinner.")

print("\n----------分界线----------\n")

'''
练习 3.7：缩短名单 
你刚得知新购买的餐桌⽆法及时送达，因此只能邀请两位嘉宾。
以完成练习 3.6 时编写的程序为基础，在程序末尾添加⼀⾏代码，打印⼀条你只能邀请两位嘉宾共进晚餐的消息。
使⽤ pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为⽌。
每次从名单中弹出⼀位嘉宾时，都打印⼀条消息，让该嘉宾知道你很抱歉，⽆法邀请他来共进晚餐。
对于余下两位嘉宾中的每⼀位，都打印⼀条消息，指出他依然在受邀之列。
使⽤ del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实名单在程序结束时确实是空的。
'''
print("Sorry, we can only invite two guests to dinner.")

name = guests.pop()
print(f"Sorry, {name} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name} there's no room at the table.")
print(guests)

name = guests[0]
print(f"{name}, please come to dinner.")
name = guests[1]
print(f"{name}, please come to dinner.")

del guests[0]
del guests[0]
print(guests)