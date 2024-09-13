'''
练习 4.13：⾃助餐 
有⼀家⾃助式餐馆，只提供 5 种简单的⾷品。请想出 5 种简单的⾷品，并将其存储在⼀个元组中。
使⽤⼀个 for 循环将该餐馆提供的 5 种⾷品都打印出来。
尝试修改其中的⼀个元素，核实 Python 确实会拒绝你这样做。
餐馆调整菜单，替换了两种⾷品。
请编写⼀⾏给元组变量赋值的代码，并使⽤⼀个 for 循环将新元组的每个元素都打印出来。
'''
menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
)

print("You can choose from the following menu items:")
for item in menu_items:
    print(f"- {item}")

#menu_items[1] = "chicken" # 导致报错

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
)

print("\nOur menu has been updated.")
print("You can now choose from the following items:")

for menu_item in menu_items:
    print(f"- {menu_item}")