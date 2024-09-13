'''
练习 5.3：外星⼈颜⾊1 
假设玩家在游戏中消灭了⼀个外星⼈，
请创建⼀个名为 alien_color 的变量，并将其赋值为'green'、'yellow' 或 'red'。
编写⼀条 if 语句，测试外星⼈是否是绿⾊的。
如果是，就打印⼀条消息，指出玩家获得了 5 分。
编写这个程序的两个版本，
上述条件测试在其中的⼀个版本中通过，
在另⼀个版本中未通过（未通过条件测试时没有输出）。
'''
#* 能够通过测试的版本：
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")

#* 不能通过测试的版本：
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")

print("\n----------分界线----------\n")

'''
练习 5.4：外星⼈颜⾊2 
像练习 5.3 那样设置外星⼈的颜⾊，并编写⼀个 if-else 结构。
如果外星⼈是绿⾊的，就打印⼀条消息，指出玩家因消灭该外星⼈获得了 5 分。
如果外星⼈不是绿⾊的，就打印⼀条消息，指出玩家获得了 10 分。
编写这个程序的两个版本，在⼀个版本中将执⾏ if 代码块，在另⼀个版本中将执⾏ else 代码块。
'''
#* 执行 if 代码块的版本：
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#* 执行 else 代码块的版本：
alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

print("\n----------分界线----------\n")

'''
练习 5.5：外星⼈颜⾊3 
将练习 5.4 中的 if-else 结构改为 if-elif-else 结构。
如果外星⼈是绿⾊的，就打印⼀条消息，指出玩家获得了 5 分。
如果外星⼈是⻩⾊的，就打印⼀条消息，指出玩家获得了 10 分。
如果外星⼈是红⾊的，就打印⼀条消息，指出玩家获得了 15 分。
编写这个程序的三个版本，分别在外星⼈为绿⾊、⻩⾊和红⾊时
打印⼀条消息。
'''
#* 外星⼈为绿⾊时的版本：
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

#* 外星⼈为黄⾊时的版本：
alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

#* 外星⼈为红⾊时的版本：
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

print("\n----------分界线----------\n")

'''
练习 5.6：⼈⽣的不同阶段 
设置变量 age 的值，再编写⼀个 if-elif-else 结构，根据 age 的值判断这个⼈处于⼈⽣的哪个阶段。
如果年龄⼩于 2 岁，就打印⼀条消息，指出这个⼈是婴⼉。
如果年龄为 2（含）〜4 岁，就打印⼀条消息，指出这个⼈是幼⼉。
如果年龄为 4（含）〜13 岁，就打印⼀条消息，指出这个⼈是⼉童。
如果年龄为 13（含）〜18 岁，就打印⼀条消息，指出这个⼈是少年。
如果年龄为 18（含）〜65 岁，就打印⼀条消息，指出这个⼈是中⻘年⼈。
如果年龄达到 65 岁，就打印⼀条消息，指出这个⼈是⽼年⼈。
'''
age = 25
if age < 2:
    print("婴儿")
elif age < 4:
    print("幼儿")
elif age < 13:
    print("儿童")
elif age < 18:
    print("少年")
elif age <65:
    print("中青年人")
else:
    print("老年人")

print("\n----------分界线----------\n")

'''
练习 5.7：喜欢的⽔果 
创建⼀个列表，其中包含你喜欢的⽔果，再编写⼀系列独⽴的 if 语句，检查列表中是否包含特定的⽔果。
将该列表命名为 favorite_fruits，并让其包含三种⽔果。
编写 5 条 if 语句，每条都检查某种⽔果是否在列表中。如果是，
就打印⼀条像下⾯这样的消息。
You really like bananas!
'''
favorite_fruits = ['blueberries', 'salmonberries', 'peaches']
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")
if 'peaches' in favorite_fruits:
    print("You really like peaches!")  