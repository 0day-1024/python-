
#* if-elif-else 语句
#* 你经常需要检查两个以上的情形，此时可使⽤ Python 提供的 if-elifelse 语句。
#* Python 只执⾏ if-elif-else 结构中的⼀个代码块。
#* 它依次检查每个条件测试，直到遇到通过了的条件测试。
#* 条件测试通过后，Python将执⾏紧跟在它后⾯的代码，并跳过余下的条件测试。

#* 在现实世界中，需要考虑的情形通常会超过两个。
#* 例如，来看⼀个根据年龄段收费的游乐场。
#* 4 岁以下免费。
#* 4（含）〜18 岁收费 25 美元。
#* 年满 18 岁收费 40 美元。
#* 如果只使⽤⼀条 if 语句，该如何确定门票价格呢？
#* 下⾯的代码能确定⼀个⼈所属的年龄段，并打印⼀条包含门票价格的消息：
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

print("\n")

#* 为了让代码更简洁，可不在 if-elif-else 代码块中打印门票价格，
#* ⽽是只在其中设置门票价格，并在它后⾯添加⼀个函数调⽤ print()：
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

print("\n")

#* 使⽤多个 elif 代码块
#* 还可以根据需要使⽤任意数量的 elif 代码块。
#* 假设前述游乐场要给⽼年⼈打折，可再添加⼀个条件测试，判断顾客是否符合打折条件。
#* 下⾯假设年满 65 岁的⽼⼈可半价（即 20 美元）购买门票：
age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

print("\n")

#* 省略 else 代码块
#* Python 并不要求 if-elif 结构后⾯必须有 else 代码块。
#* 在⼀些情况下，else 代码块很有⽤；⽽在其他情况下，使⽤⼀条 elif 语句来处理特定的情形更清晰：
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")

print("\n")

#* 测试多个条件
#* if-elif-else 语句虽然功能强⼤，但仅适⽤于只有⼀个条件满⾜的情况：
#* 在遇到通过了的条件测试后，Python 就会跳过余下的条件测试。
#* 这种⾏为很好，效率很⾼，让你能够测试⼀个特定的条件。
#* 然⽽，有时候必须检查你关⼼的所有条件。
#* 在这种情况下，应使⽤⼀系列不包含 elif 和 else 代码块的简单 if 语句。
#* 在可能有多个条件为True，且需要在每个条件为 True 时都采取相应措施时，适合使⽤这种⽅法。

#* 下⾯再来看看前⾯的⽐萨店⽰例。
#* 如果顾客点了两种配料，就需要确保在其⽐萨中放⼊这些配料：
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

print("\n")

#* 如果像下⾯这样转⽽使⽤ if-elif-else 语句，
#* 代码将不能正确运⾏，因为只要有⼀个条件测试通过，就会跳过余下的条件测试：
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")