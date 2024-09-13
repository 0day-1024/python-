'''
遍历整个列表
你经常需要遍历列表的所有元素，对每个元素执⾏相同的操作。
'''

#* 假设我们有⼀个魔术师名单，需要将其中每个魔术师的名字都打印出来。
#* 为此，可以分别获取名单中的每个名字，但这种做法会导致许多问题。
#* 例如，很⻓的名单将包含⼤量重复的代码；每当名单的⻓度发⽣变化时，都必须修改代码。
#* 使⽤ for 循环，可让 Python 去处理每个元素，从⽽避免这些问题。
#* 下⾯使⽤ for 循环打印⼀个魔术师名单中的所有名字：
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print("\n")

#* 在 for 循环中执⾏更多的操作
#* 在 for 循环中，可以对每个元素执⾏任意操作。
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

print("\n")

#* 在 for 循环中，想包含多少⾏代码都可以。
#* 在代码⾏ for magician in magicians 后⾯，每⾏缩进的代码都是循环的⼀部分，
#* 将针对列表中的每个值执⾏⼀次。因此，可对列表中的每个值执⾏任意多的操作。
#* 下⾯再来添加⼀⾏代码，告诉每位魔术师，我们期待他/她的下⼀次表演：
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#* 在 for 循环中，想包含多少⾏代码都可以。
#* 实际上，你将发现，使⽤ for循环对每个元素执⾏众多不同的操作很有⽤。
print("\n")

#* 在 for 循环结束后执⾏⼀些操作
#* 通常想提供总结性输出或接着执⾏程序必须完成的其他任务。
#* 在 for 循环后⾯，没有缩进的代码都只执⾏⼀次，不会重复执⾏。
#* 下⾯来打印⼀条向全体魔术师致谢的消息，感谢他们的精彩表演。
#* 为了在打印给各位魔术师的消息后，打印给全体魔术师的致谢消息，我们将相应的代码放在 for 循环后⾯，且不缩进：
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

'''
避免缩进错误
Python 根据缩进来判断代码⾏与程序其他部分的关系。
Python 通过缩进让代码更易读。
当你开始编写必须正确缩进的代码时，需要注意⼀些常⻅的缩进错误。
'''
#* 忘记缩进
#* 位于 for 语句后⾯且属于循环组成部分的代码⾏，⼀定要缩进。

#* 忘记缩进额外的代码⾏
#* 有时候，虽然循环能够运⾏且不会出现错误，但结果出⼈意料。
#* 当试图在循环中执⾏多项任务，却忘记缩进其中的⼀些代码⾏时，就会出现这种情况。

#* 不必要的缩进
#* 如果你不⼩⼼缩进了⽆须缩进的代码⾏，Python 将指出这⼀点

#* 循环后不必要的缩进
#* 如果你不⼩⼼缩进了应在循环结束后执⾏的代码，这些代码将针对每个列表元素重复执⾏。
#* 在⼀些情况下，这可能导致 Python 报告语法错误，但通常只会导致逻辑错误。

#* 遗漏冒号
#* for 语句末尾的冒号告诉 Python，下⼀⾏是循环的第⼀⾏。
#* 如果不⼩⼼遗漏了冒号，将导致语法错误，