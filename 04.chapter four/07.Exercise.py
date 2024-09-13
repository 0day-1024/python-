'''
练习 4.10：切⽚ 
选择你在本章编写的⼀个程序，在末尾添加⼏⾏代码，以完成如下任务。
打印消息“The first three items in the list are:”，再使⽤切⽚来打印列表的前三个元素。
打印消息“Three items from the middle of the list are:”，再使⽤切⽚来打印列表中间的三个元素。
打印消息“The last three items in the list are:”，再使⽤切⽚来打印列表末尾的三个元素。
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("The first three items in the list are:")
for player in players[:3]:
    print(player)

print("Three items from the middle of the list are:")
for player in players[1:4]:
    print(player)

print("The last three items in the list are:")
for player in players[-3:]:
    print(player)

print("The last three items in the list are:")
for player in players[2:]:
    print(player)

print("\n----------分界线----------\n")

'''
练习 4.11：你的⽐萨，我的⽐萨 
在你为练习 4.1 编写的程序中，创建⽐萨列表的副本，并将其赋给变量 friend_pizzas，再完成如下任务。
在原来的⽐萨列表中添加⼀种⽐萨。
在列表 friend_pizzas 中添加另⼀种⽐萨。
核实有两个不同的列表。
为此，打印消息“My favorite pizzas are:”，再使⽤⼀个 for 循环来打印第⼀个列表;
打印消息“My friend's favorite pizzas are:”，再使⽤⼀个 for 循环来打印第⼆个列表。
核实新增的⽐萨被添加到了正确的列表中。
'''
pizzas = ['Pepperoni', 'Mushroom', 'Cheese']
friend_pizzas = pizzas[:]

pizzas.append('Ham')  
friend_pizzas.append('Vegetable')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")

print("\n----------分界线----------\n")

'''
练习 4.12：使⽤多个循环 
在本节中，为节省篇幅，程序 foods.py 的每个版本都没有使⽤ for 循环来打印列表。
请选择⼀个版本的foods.py，在其中编写两个 for 循环，将各个⾷品列表都打印出来。
'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)