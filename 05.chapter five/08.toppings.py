'''
使⽤ if 语句处理列表
结合使⽤ if 语句和列表，可完成⼀些有趣的任务：
对列表中特定的值做特殊处理；⾼
效管理不断变化的情形，如餐馆是否还有特定的⾷材；
证明代码在各种情形下都将按预期运⾏。
'''

#* 检查特殊元素
#* 本章开头通过⼀个简单的⽰例演⽰了如何处理特殊值 'bmw'——需要采⽤不同的格式打印它。
#* 现在你对条件测试和 if 语句有了⼤致的认识，下⾯来进⼀步研究如何检查列表中的特殊值，并对其做合适的处理。
#* 继续使⽤前⾯的⽐萨店⽰例。
#* 这家⽐萨店在制作⽐萨时，每添加⼀种配料都打印⼀条消息。
#* 要以极⾼的效率编写这样的代码，可以创建⼀个包含顾客所点配料的列表，
#* 并使⽤⼀个循环来指出添加到⽐萨中的配料：
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

print("\n")

#* 然⽽，如果⽐萨店的⻘椒（green peppers）⽤完了，该如何处理呢？
#* 为了妥善地处理这种情况，可在 for 循环中包含⼀条 if 语句：
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if(requested_topping == "green peppers"):
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

print("\n")

#* 确定列表⾮空
#* 到⽬前为⽌，我们对于要处理的每个列表都做了⼀个简单的假设——它们都⾄少包含⼀个元素。
#* 因为⻢上就要让⽤户来提供存储在列表中的信息，所以不能再假设循环运⾏时列表⾮空。
#* 有鉴于此，在运⾏ for 循环前确定列表⾮空很重要。
#* 下⾯在制作⽐萨前检查顾客点的配料列表是否为空。
#* 如果列表为空，就向顾客确认是否要点原味⽐萨（plain pizza）；
#* 如果列表⾮空，就像前⾯的⽰例那样制作⽐萨：
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
#* 在 if 语句中将列表名⽤作条件表达式时，
#* Python将在列表⾄少包含⼀个元素时返回 True，在列表为空时返回 False。

print("\n")

#* 使⽤多个列表
#* 顾客的要求五花⼋门，在⽐萨配料⽅⾯尤其如此。
#* 如果顾客要在⽐萨中添加炸薯条（French fries），该怎么办呢？
#* 可以使⽤列表和 if 语句来确定能否满⾜顾客的要求。
#* 我们来看看如何在制作⽐萨前拒绝怪异的配料要求。
#* 下⾯的⽰例定义了两个列表，其中第⼀个包含⽐萨店供应的配料，第⼆个则包含顾客点的配料。
#* 这次对于 requested_toppings 中的每个元素，都先检查它是否是⽐萨店供应的配料，再决定是否在⽐萨中添加它：
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")