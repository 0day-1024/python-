'''
练习 4.1：⽐萨 
想出⾄少三种你喜欢的⽐萨，将其名称存储在⼀个列表中，再使⽤ for 循环将每种⽐萨的名称打印出来。
修改这个 for 循环，使其打印包含⽐萨名称的句⼦，⽽不仅仅是⽐萨的名称。
对于每种⽐萨都显⽰⼀⾏输出，如下所⽰。
I like pepperoni pizza.
在程序末尾添加⼀⾏代码（不包含在 for 循环中），指出你有多喜欢⽐萨。
输出应包含针对每种⽐萨的消息，还有⼀个总结性的句⼦，如下所⽰。
I really love pizza!
'''
pizzas = ['Pepperoni', 'Mushroom', 'Cheese']

for pizza in pizzas:
    print(pizza)

print("\n")

for pizza in pizzas:
    print(f"I really love {pizza} pizza!")

print("\nI really love pizza!")

print("\n----------分界线----------\n")

'''
练习 4.2：动物 
想出⾄少三种有共同特征的动物，将其名称存储在⼀个列表中，再使⽤ for 循环将每种动物的名称打印出来。
修改这个程序，使其针对每种动物都打印⼀个句⼦，如下所⽰。
A dog would make a great pet.
在程序末尾添加⼀⾏代码，指出这些动物的共同之处，如打印下⾯这样的句⼦。
Any of these animals would make a great pet!
'''
animals = ['dog', 'cat', 'bird']

for animal in animals:
    print(animal)

print("\n")

for animal in animals:
    print(f"A {animal} would make a great pet.")

print("\nAny of these animals would make a great pet!")