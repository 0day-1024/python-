'''
if 语句
理解条件测试之后，就可以开始编写 if 语句了。
if 语句有很多种，选择使⽤哪⼀种取决于要测试的条件数。
'''

#* 简单的 if 语句
#* 最简单的 if 语句只有⼀个条件测试和⼀个操作：
# if conditional_test:
#     do something

#* 假设有⼀个表⽰某个⼈年龄的变量，⽽你想知道这个⼈是否到了投票的年龄，可使⽤如下代码：
age = 19
if age >= 18:
    print("You are old enough to vote!")

print("\n")

#* 可根据需要，在紧跟在 if 语句后⾯的代码块中添加任意数量的代码⾏。
#* 下⾯在⼀个⼈已到投票年龄时再打印⼀⾏输出，问他是否登记了：
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

print("\n")

#* if-else 语句
#* 你经常需要在条件测试通过时执⾏⼀个操作，在没有通过时执⾏另⼀个操作。
#* 在这种情况下，可使⽤ Python 提供的 if-else 语句。
#* if-else 语句块类似于简单的 if 语句，但其中的 else 语句让你能够指定条件测试未通过时要执⾏的操作。
#* 下⾯的代码在⼀个⼈已到投票年龄时显⽰与前⾯相同的消息，在不到投票年龄时显⽰⼀条新消息：
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")