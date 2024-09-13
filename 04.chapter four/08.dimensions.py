'''
元组
列表⾮常适合⽤于存储在程序运⾏期间可能变化的数据集。
列表是可以修改的，这对于处理⽹站的⽤户列表或游戏中的⾓⾊列表⾄关重要。
然⽽，你有时候需要创建⼀系列不可修改的元素，元组可满⾜这种需求。
Python将不能修改的值称为不可变的，⽽不可变的列表称为元组（tuple）。
'''

#* 定义元组
#* 元组看起来很像列表，但使⽤圆括号⽽不是⽅括号来标识。
#* 定义元组后，就可使⽤索引来访问其元素，就像访问列表元素⼀样。
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#* 尝试修改元组 dimensions 的⼀个元素
# dimensions = (200, 50)
# dimensions[0] = 250
#* 导致 Python 返回类型错误的消息。
#* 由于试图修改元组的操作是被禁⽌的，因此 Python 指出不能给元组的元素赋值。

#* 严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。
#* 如果你要定义只包含⼀个元素的元组，必须在这个元素后⾯加上逗号
my_t = (3,)
#* 创建只包含⼀个元素的元组通常没有意义，但⾃动⽣成的元组有可能只有⼀个元素。

#* 遍历元组中的所有值
#* 像列表⼀样，也可以使⽤ for 循环来遍历元组中的所有值
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#* 修改元组变量
#* 虽然不能修改元组的元素，但可以给表⽰元组的变量赋值。
#* 例如，要修改前述矩形的尺⼨，可重新定义整个元组
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)